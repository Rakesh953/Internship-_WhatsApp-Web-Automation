"""chatproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from app1.views import *
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sinup/',sinup,name='sinup'),
    path('userlogin/',userlogin,name='userlogin'),
    path('logouted/',logouted,name='logouted'),
    path('home/',home,name='home'),
    re_path('^(?P<pk>\d+)/',views.message,name='message'),
    #path('(?<slug>\w+)/',views.sendmessage,name='sendmessage'),
    path('display/',display,name='display'),
    path('profile_detail/',profile_detail,name='profile_detail'),
    path('image/',image,name='image'),
    path('register/',register,name="register" ),
    re_path('^(?P<pk>\d+)/',views.forward,name='forward'),
    re_path('(?P<y>\d+)$/',views.delete,name='delete'),
    path('status/',status,name='status'),
    re_path('(?P<id>\d+)$/',views.req_status,name='req_status'),
    path('ok/',ok,name='ok'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
