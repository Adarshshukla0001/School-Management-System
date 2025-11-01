from django.contrib import admin
from . models import Facalty,Nfc,Attend,Salary
# Register your models here.

admin.site.register(Facalty),
admin.site.register(Nfc),
admin.site.register(Attend),
admin.site.register(Salary)