from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addfacalty',views.addfacalty,name='addfacalty'),
    path('viewfacalty',views.viewfacalty,name='viewfacalty'),
    path('deletefacalty/<str:fid>/',views.deletefacalty,name='deletefacalty'),
    path('facaltynfc',views.facaltynfc,name='facaltynfc'),
    path('facaltyattend',views.facaltyattend,name='facaltyattend'),
    path('present/<str:fid>/',views.present,name='present'),
    path('viewfattend',views.viewfattend ,name='viewfattend'),
    path('ab/<str:fid>/',views.ab,name='ab'),
    path('pr/<str:fid>/',views.pr,name='pr'),
    path('sal',views.sal,name='sal'),
    path('addsal/<str:fid>/',views.addsal,name='addsal'),
    path('sendsal',views.sendsal,name='sendsal'),
    path('send/<str:fid>/',views.send,name='send'),
    path('leave',views.leave,name='leave'),
    path('accept/<str:fid>/',views.accept,name='accept'),
    path('reject/<str:fid>/',views.reject,name='reject'),
    path('ffeed',views.ffeed,name='ffeed'),
    path('stdfeed',views.stdfeed,name='stdfeed')
]