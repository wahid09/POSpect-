from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.get_login, name='login'),
    path('logout', views.get_logout, name="logout")
]