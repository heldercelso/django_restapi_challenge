from django.contrib import admin

from .models import Contract, Deposit, Withdraw

admin.site.register(Contract)
admin.site.register(Deposit)
admin.site.register(Withdraw)