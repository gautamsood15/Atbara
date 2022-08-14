from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpassword']
        
        if cpass != password:
            messages.warning(request, ''' Password Doesn't match  ''')
            return redirect("signup")

        else:
            if email and username and password:
                a = User.objects.create_user(username, email, password)
                if a:
                    messages.success(request, 'You have signed up successfully')
                    return redirect('login')

    return render(request, 'signup.html', {})

def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            messages.warning(request, 'Please First Create your Account or Account details are wrong')
            return redirect('login')

    return render(request, 'login.html', {})
