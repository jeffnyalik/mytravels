from django.contrib.auth.models import(
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin)
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False, blank=True, null=True)
    is_customer = models.BooleanField(default=False,blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        app_label = "api"


class Supplier(CustomUser):
    name = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True,max_length=20)
    address = models.CharField(blank=True, null=True, max_length=200)
    # is_supplier = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Suppliers"
        app_label = "api"

    def __str__(self) -> str:
        return self.name
    
class Customer(CustomUser):
    name = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True,max_length=20)
    address = models.CharField(blank=True, null=True, max_length=200)
    # is_customer = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Customers"
        app_label = "api"

    def __str__(self) -> str:
        return self.name