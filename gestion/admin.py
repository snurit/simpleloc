from django.contrib import admin
from .models import Option, Contract, Apartment, Customer

admin.site.register(Option)
admin.site.register(Contract)
admin.site.register(Apartment)
admin.site.register(Customer)