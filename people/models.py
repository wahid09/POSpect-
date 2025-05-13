from django.db import models
from django.core.validators import RegexValidator
from place.models import Country, State


# Create your models here.

class Suppliers(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="suppliers")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="suppliers")
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^01[0-9]{9}$',
        message="Phone number must be entered in the format: '01XXXXXXXXX' (11 digits, Bangladeshi format)."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=True)
    address = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "supplier"
        verbose_name_plural = "suppliers"

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"


class Customer(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="customers")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="customers")
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^01[0-9]{9}$',
        message="Phone number must be entered in the format: '01XXXXXXXXX' (11 digits, Bangladeshi format)."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=True)
    address = models.TextField()
    image = models.ImageField(upload_to="customer_image", blank=True, null=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country} - {self.name} - {self.phone_number}"


class Warehouse(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="warehouses")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="warehouses")
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^01[0-9]{9}$',
        message="Phone number must be entered in the format: '01XXXXXXXXX' (11 digits, Bangladeshi format)."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country} - {self.name} - {self.phone_number}"
