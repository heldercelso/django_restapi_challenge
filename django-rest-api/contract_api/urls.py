from contract_api import views
from django.urls import path


urlpatterns = [
    path('contracts', views.contract_list, name='contracts'),
    path('contract/<pk>', views.contract_detail, name='contract'),

    path('deposits', views.deposit_list, name='deposits'),
    path('deposit/<pk>', views.deposit_detail, name='deposit'),

    path('withdraws', views.withdraw_list, name='withdraws'),
    path('withdraw/<pk>', views.withdraw_detail, name='withdraw'),
]