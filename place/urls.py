from django.urls import path
from . import views

app_name = 'place'

urlpatterns = [
    path('country-list', views.get_country, name='country_list'),
]