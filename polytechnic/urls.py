"""
URL configuration for polytechnic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.myurls')),
    path('adminzone/',include(('adminzone.adurls','adminzone'),namespace='adminzone')),
    path('facaltyzone/',include(('facaltyzone.furls','facaltyzone'),namespace='facaltyzone')),
    path('studentzone/',include(('studentzone.stdurls','studentzone'),namespace='studentzone'))
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)