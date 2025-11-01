from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('addstudent',views.addstudent,name='addstudent'),
path('viewstudent',views.viewstudent,name='viewstudent'),
path('deletestudent/<str:stdid>/',views.deletestudent,name='deletestudent'),
path('facaltyprofile',views.facaltyprofile,name='facaltyprofile'),
path('updatefacalty',views.updatefacalty,name='updatefacalty'),
path('fleave',views.fleave,name='fleave'),
path('ffeed',views.ffeed,name='ffeed'),
path('leave',views.leave,name='leave'),
path('accept/<str:stdid>/',views.accept,name='accept'),
path('reject/<str:stdid>/',views.reject,name='reject'),
path('viewsal',views.viewsal,name='viewsal'),
path('fnfc',views.fnfc,name='fnfc'),
path('stdnfc',views.stdnfc,name='stdnfc'),
path('studentattend',views.studentattend,name='studentattend'),
path('p/<str:stdid>/',views.p,name='p'),
path('viewstdattend',views.viewstdattend ,name='viewstdattend'),
path('abt/<str:stdid>/',views.abt,name='abt'),
path('pt/<str:stdid>/',views.pt,name='pt'),

]