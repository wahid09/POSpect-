from django.db import models


# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=50, null=False, blank=False)
    phone_code = models.CharField(max_length=8, null=True, blank=True)
    capital = models.CharField(max_length=30, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    region = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return f"{self.country_name} - {self.region}"


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")
    state_name = models.CharField(max_length=20, null=False, blank=False)
    state_code = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country} - {self.state_name}"
