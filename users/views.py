from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout


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