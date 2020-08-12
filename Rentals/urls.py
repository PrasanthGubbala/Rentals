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

    #provider login
    path('provider_login/',views.provider_login,name='provider_login'),
    path('provider_login_check/',views.provider_login_check,name='provider_login_check'),
    path('provider_registration/',views.provider_registration,name='provider_registration'),
    path('provider_registration_save/',views.provider_registration_save,name='provider_registration_save'),

    #consumer login
    path('consumer_login/',views.consumer_login,name='consumer_login'),
    path('consumer_login_check/',views.consumer_login_check,name='consumer_login_check'),
    path('consumer_registration/',views.consumer_registration,name='consumer_registration'),
    path('consumer_registration_save/',views.consumer_registration_save,name='consumer_registration_save'),


    #provider phase
    path('provider_profile/',views.provider_profile,name='provider_profile'),
    path('provider_home/',views.provider_home,name='provider_home'),
    path('add_service/',views.add_service,name='add_service'),
    path('save_service/',views.save_service,name='save_service'),
    path('view_all_service/',views.view_all_service,name='view_all_service'),

    #consumer phase
    path('consumer_profile/',views.consumer_profile,name='consumer_profile'),
    path('consumer_home/',views.consumer_home,name='consumer_home'),
    path('available_rental_services/',views.available_rental_services,name='available_rental_services'),

    #logout ie;for both provider and consumer
    path('logout/',views.logout,name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)