from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate 
from .models import Youtuber
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


def youtuber(request):
    check = Youtuber.objects.filter(youtuber=request.user)
    if not check:
        youtuber = Youtuber.objects.create(youtuber=request.user)
        if youtuber:
            return redirect("upload")
    else:
        return redirect("index")
    
    return HttpResponse("Youtuber Created")


def upload(request):
    return render(request, 'upload.html', {})


def create_channel(request):
    if request.method == 'POST':
        file = request.FILES['file']
        channelname = request.POST['channelname']
        youtuber = Youtuber.objects.filter(youtuber=request.user).update(channel_name=channelname,youtubeimage=file)
        if youtuber:
            return JsonResponse({
                'success':True,
                #'link':'channel'
            })
    context ={}
    youtuber = Youtuber.objects.filter(youtuber=request.user)
    if youtuber:
        context = {"success":"hai"}
    return render(request,'createchannel.html',context)