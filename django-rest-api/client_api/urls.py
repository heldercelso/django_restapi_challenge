from client_api import views
from django.urls import  path

urlpatterns = [
    path('clients', views.client_list, name='clients'),
    path('client/<pk>', views.client_detail, name='client'),
]