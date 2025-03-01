"""
URL configuration for Travel project.

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
from django.urls import path, re_path, include
from . import settings
from django.conf.urls.static import static
from Web_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    re_path(r'^course/(?P<id>\d+)/', views.course),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('coursess/', views.coursess),
    path('new_message/', views.new_message),
    path('users/', include('Web_1.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
