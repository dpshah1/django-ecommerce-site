from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import *


# Create your views here.
def login_user(request):
    return render(request, 'pages/login.html')

def verify_login(request):
    if request.method == 'POST':
        username = request.POST.get('usernameInput')
        password = request.POST.get('passwordInput')

        print(f"Username = {username}")
        print(f"Password = {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            print("Logged in successfully")
            return redirect('/shop/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("Invalid login credentials 😂😂")

def logout_user(request):
    logout(request)
    return redirect('../../')

def signup_user(request):
    return render(request, 'pages/signup.html')

def create_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        full_name = request.POST.get('fullName')
        email = request.POST.get('emailForm')

        print(username)
        print(password)
        print(full_name)
        print(full_name)

        user = User.objects.create_user(username=username, password=password)
        customer = Customer(user=user, name=full_name, email=email)
        customer.save()

        login(request, user=user)
        print("Created account successfully")
        return redirect('/shop/')




