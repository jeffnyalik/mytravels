from django.urls import path
# from .import views
from auths import auth_views
from hotels import hotel_views

urlpatterns = [
    # path('', views.index, name="Index page"),
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
]
