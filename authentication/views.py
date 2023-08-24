from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import items

def home(request):
    return render(request, 'authentication/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        myuser = User.objects.create_user(username=username, password=password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email

        myuser.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect('signin')
    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return redirect('/home/')
        else:
            redirect('signin')

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    return redirect('/signin')


def change_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        obj = get_object_or_404(User, username=username)
        obj.set_password(new_password)
        obj.save()
        messages.success(request, "Password changed successfully!")
        return redirect('/signin/')
    return render(request, 'authentication/change_password.html')

    


