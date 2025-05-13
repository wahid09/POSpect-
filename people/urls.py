from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('supplier-list', views.get_supplier, name='supplier_list'),
]