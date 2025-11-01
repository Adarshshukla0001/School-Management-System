from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('facaltylogin',views.facaltylogin,name='facaltylogin'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('validateuser',views.validateuser,name='validateuser'),
    path('validatefacalty',views.validatefacalty,name='validatefacalty'),
    path('validatestudent',views.validatestudent,name='validatestudent')
    
]