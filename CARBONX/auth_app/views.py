from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile   # যদি Profile model থাকে

def registration(request):
    if request.method == "POST":
        
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Password match check
        if password != confirm_password:
            messages.error(request, "Password did not match")
            return redirect('register')

        # Username exists check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # Email exists check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create Profile (phone save)
        Profile.objects.create(
            user=user,
            Phone_number=phone
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'auth/registration.html')


def login_view(request):
    return render(request, 'auth/login.html')
