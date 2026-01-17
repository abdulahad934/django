from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile

def home(request):
    profiles = Profile.objects.all()
    CONTEXT = {
        'profiles' : profiles
    }
    return render(request, "hello.html", context=CONTEXT)



def registration(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 1️⃣ Password match check
        if password != confirm_password:
            messages.error(request, "Password did not match")
            return redirect('register')

        # 2️⃣ Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # 3️⃣ Username auto-generate from email
        base_username = email.split("@")[0]
        username = base_username
        count = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}{count}"
            count += 1

        # 4️⃣ Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # 5️⃣ Create Profile
        Profile.objects.create(
            user=user,
            Phone_number=phone
        )

        messages.success(
            request,
            "Account created successfully. Please login."
        )
        return redirect('login')

    return render(request, 'auth/registration.html')


def login_view(request):
    if request.method == "POST":
        email_or_username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email_or_username,
            password=password
        )

        if user is None:
            try:
                user_obj = User.objects.get(email=email_or_username)
                user = authenticate(
                    request,
                    username=user_obj.username,
                    password=password
                )
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')   # ✅ FIXED
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'auth/login.html')


# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully")
#     return redirect('login')
