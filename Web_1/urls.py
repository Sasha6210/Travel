from django.urls import path, include
from .views import Register, profile


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('user/profile/', profile, name='profile'),
    path('register/', Register.as_view(), name='register')
]