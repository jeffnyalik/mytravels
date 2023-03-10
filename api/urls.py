from django.urls import path
# from .import views
from auths import auth_views
from hotels import hotel_views
from flights import flight_views
from bookings import booking_views
from .import views

urlpatterns = [
    path('', views.index, name="Index page"),
    path('vendor-register', auth_views.SupplierRegistrationView.as_view(), name='vendor-register'),
    path('vendor-login', auth_views.SupplierLoginView.as_view(), name='vendor-login'),
    path('customer-register', auth_views.CustomerRegistrationView.as_view(), name='customer-register'),
    path('customer-login', auth_views.CustomerLoginView.as_view(), name='customer-login'),

    #Hotel and Rooms, Room type path
    path('hotels/', hotel_views.HotelView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', hotel_views.HotelDetail.as_view(), name='hotel-detail'),
    path('rooms/', hotel_views.RoomView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', hotel_views.RoomDetail.as_view(), name='room-detail'),
    path('room_types/', hotel_views.RoomTypeView.as_view(), name='room-type-list'),
    path('room_types/<int:pk>/', hotel_views.RoomTypeDetailView.as_view(), name='room-type-detail'),

    #Flights path
    path('flights/', flight_views.FlightView.as_view(), name='flights-list'),
    path('flights/<int:pk>/', flight_views.FlightDetailView.as_view(), name='flights-detail'),

    #bookings path
    path('bookings/', booking_views.ListBookingsApiView.as_view(), name='bookings-list'),
    path('bookings/<int:hotel_id>/rooms/<int:room_id>/book/', booking_views.BookingApiView.as_view(), name='bookings'),
    path('customer-bookings/', booking_views.CustomerBookingView.as_view(), name='customer-bookings'),

]
