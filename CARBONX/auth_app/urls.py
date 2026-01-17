from django.urls import path
from .views import registration, login_view, home

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', registration, name='register'),
    path('login/', login_view, name='login'),
]
