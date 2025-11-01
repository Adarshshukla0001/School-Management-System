from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('stdfeed',views.stdfeed,name='stdfeed'),
    path('stdleave',views.stdleave,name='stdleave'),
    path('updatestudent',views.updatestudent,name='updatestudent'),
    path('stdnfc',views.stdnfc,name='stdnfc')
    ]