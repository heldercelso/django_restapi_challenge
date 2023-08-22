from plans_api import views
from django.urls import  path

urlpatterns = [
    path('plans', views.plans_list, name='plans'),
    path('plan/<pk>', views.plans_detail, name='plan'),
]