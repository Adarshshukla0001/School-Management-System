from django.contrib import admin
from . models import Student,Leave,Feed,SNfc,SAttend
# Register your models here.
admin.site.register(Student)
admin.site.register(Leave)
admin.site.register(Feed)
admin.site.register(SNfc)
admin.site.register(SAttend)