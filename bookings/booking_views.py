import html
from io import BytesIO
from serializers.booking_serializer import *
from bookings.booking_model import *
from rest_framework import generics
from custom_permissions.permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db import transaction
from decimal import Decimal
from rest_framework import permissions
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

import os
from datetime import datetime
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from dotenv import load_dotenv
load_dotenv()
from xhtml2pdf import pisa
import random




class ListBookingsApiView(generics.ListAPIView):
    serializer_class = BookingSerizer
    queryset = Booking.objects.all()


class CustomerBookingView(generics.ListAPIView):
    serializer_class = BookingSerizer
    permission_classes = [IsCustomer]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_customer:
            return Booking.objects.filter(user=user)
        elif user.is_admin:
            return Booking.objects.all()
        elif user.is_superuser:
            return Booking.objects.all()
        else:
            return Booking.objects.none()
        

class BookingApiView(generics.CreateAPIView):
    serializer_class = BookingSerizer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        user = self.request.user
        if user.IsCustomer:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
        
    @transaction.atomic
    def create(self, request, room_id, hotel_id, *args, **kwargs):
        try:
            hotel = get_object_or_404(Hotel, id=hotel_id)
            room = get_object_or_404(Room, id=room_id, hotel=hotel)
            percentage = get_object_or_404(Percentage, hotel=hotel)
            
        except Room.DoesNotExist:
            return Response({'message': 'Room does not exist in this hotel.'}, status=status.HTTP_404_NOT_FOUND)
        # if room.is_booked:
        #     return Response({'message': 'This room is already booked.'}, status=status.HTTP_400_BAD_REQUEST)

        room.is_booked = True
        room.save()
    

        # Calculate paid amount and round off to 2 decimal places
        paid_amount = round(room.price * Decimal(percentage.value) / Decimal('100.0'), 2)
        paid_amount = paid_amount.quantize(Decimal('0.001'))
        remaining = round(room.price - paid_amount, 2)

        print(remaining)

        deposit_paid = True
        request.data['paid_amount'] = paid_amount
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save(user=request.user, room=room, paid_amount=paid_amount, deposit_paid=deposit_paid)

        # Update the balance field of the booking object
        booking.balance = remaining
        booking.save()

        ## Generate customer invoice
        # invoice_number = 'INV-001'
        invoice_number = 'INV-MYTRAVELS-' + str(random.randint(1, 999)).zfill(3)
        invoice_date = datetime.now().strftime('%Y-%m-%d')

        invoice = {
            'customer': request.user,
            'invoice_number': invoice_number,
            'invoice_date': invoice_date,
            'amount': paid_amount,
            'price': booking.room.price,
            'balance': remaining,
            'check_in': booking.check_in,
            'check_out': booking.check_out,
            'hotel': room.hotel.hotel_name,
            'room': room.room_type.name,
            'currency': 'USD',
            'status': 'paid',
            'notes': f'Payment for {room.room_type} at {room.hotel.hotel_name}.'
        }

        print(invoice)
        # Render the invoice as a PDF or HTML file
        invoice_html = render_to_string('book_pdf/invoice.html', {'invoice': invoice})
        pdf_file = BytesIO()
        pisa.CreatePDF(invoice_html.encode('UTF-8'), pdf_file)
        pdf_file.seek(0)
        invoice_pdf = pdf_file.read()
        # invoice_pdf = html(string=invoice_html).write_pdf()


        # Send the invoice via email to the customer
        email_subject = 'Invoice for hotel room booking'
        email_body = 'Please find attached the invoice for your hotel room booking.'
        email_from = os.getenv('DEFAULT_FROM_EMAIL')
        email_to = [request.user.email]
        text_content = strip_tags(invoice_html)

        # # email_message = EmailMessage(email_subject, email_body, email_from, email_to)
        email_message = EmailMultiAlternatives(email_subject, email_body, email_from, email_to)

        # email_message.attach('invoice.pdf', invoice_pdf, 'application/pdf')
        # email_message.attach_alternative(invoice_html, 'text/html')
        # # Attach the invoice PDF to the email message
        invoice_pdf_name = 'invoice-{}.pdf'.format(booking.id)
        email_message.attach(invoice_pdf_name, invoice_pdf, 'application/pdf')
        email_message.send()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

