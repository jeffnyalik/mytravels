from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Index page"),
    path('vendor-register', views.SupplierRegistrationView.as_view(), name='vendor-register'),
    path('vendor-login', views.SupplierLoginView.as_view(), name='vendor-login'),
    path('customer-register', views.CustomerRegistrationView.as_view(), name='customer-register'),
    path('customer-login', views.CustomerLoginView.as_view(), name='customer-login')
]
