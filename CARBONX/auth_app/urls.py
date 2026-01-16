from django.urls import path
from .views import registration, login_view

urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login_view, name='login'),
]
