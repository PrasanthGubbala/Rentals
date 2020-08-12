"""Rentals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('admin/', admin.site.urls),
    #main phase
    path('',views.main,name='main'),
    path('provider_login/',views.provider_login,name='provider_login'),
    path('provider_login_check/',views.provider_login_check,name='provider_login_check'),
    path('provider_registration/',views.provider_registration,name='provider_registration'),
    path('provider_registration_save/',views.provider_registration_save,name='provider_registration_save'),

    #provider phase
    path('provider_profile/',views.provider_profile,name='provider_profile'),
    path('provider_home/',views.provider_home,name='provider_home'),
    path('add_service/',views.add_service,name='add_service'),
    path('save_service/',views.save_service,name='save_service'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)