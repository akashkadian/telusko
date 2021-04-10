from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        a1 = request.POST['first_name']
        a2 = request.POST['last_name']
        a3 = request.POST['username']
        a4 = request.POST['email']
        a5 = request.POST['password1']
        a6 = request.POST['password2']
        if a5 == a6:
            if User.objects.filter(username=a3).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=a4).exists():
                messages.info(request, 'Email already exists')
            else:
                user1= User.objects.create_user(username=a3, email=a4, password=a5, first_name=a1, last_name=a2)
                user1.save()
                messages.info(request, 'User registered successfully')
                return redirect('/')
        else:
            messages.info(request, 'Password unmatched!')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method== 'POST':
        z1 = request.POST['username']
        z2 = request.POST['password']
        user5 = auth.authenticate(request, username= z1, password= z2)
        if user5 is not None:
            auth.login(request, user5)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

