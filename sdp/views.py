import csv
from django.http import *
from django.shortcuts import *
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import socket
socket.getaddrinfo('localhost', 8080)

def login(request):
    return render(request,'LoginPage.html')

def navbar(request):
    return render(request,'Navbar.html')

# def login1(request):
#     if request.method == 'POST':
#         em = request.POST.get('emailinput')
#         pass1 = request.POST.get('passwordinput')

#         user=authenticate(request,email=em,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect("home")
#         else:
#             return HttpResponse("Incorrect credintials")
#     else:
#         return render(request, 'LoginPage.html')

def login1(request):
    if request.method == 'POST':
        name1 = request.POST.get('nameinput')
        pass1 = request.POST.get('passwordinput')
        
        print("UserName:", name1)
        print("Password:", pass1)

        if Article.objects.filter(name=name1, password=pass1).exists():
            return redirect("home")
        else:
            # messages.success(request,("There was incorrect username or password"))
            return redirect("login")
            # return HttpResponse("username or password is not correct")
    else:
        return render(request, 'LoginPage.html')

def signup(request):
    return render(request,'Register.html')

def signup1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Article.objects.filter(email=email).exists():
            return HttpResponse("Email is already Registered Please try with another Email")

        my_user=Article.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        my_user.save()
        return redirect('login')
    return render(request,'Register.html')

def logout1(request):
    logout(request)
    return redirect('login')

def carbook(request):
    return render(request,'BookCar.html')

# @login_required(login_url='login')
def home(request):
    return render(request,'Home.html')

def takerentcar(request):
    return render(request,'Takerentcar.html')

def car1(request):
    return render(request,'car1.html')

def car2(request):
    return render(request,'car2.html')

def car(request):
    return render(request,'car.html')

def car3(request):
    return render(request,'car3.html')

def car4(request):
    return render(request,'car4.html')

def car5(request):
    return render(request,'car5.html')

def car6(request):
    return render(request,'car6.html')

def car7(request):
    return render(request,'car7.html')

def car8(request):
    return render(request,'car8.html')

def car9(request):
    return render(request,'car9.html')

def car10(request):
    return render(request,'car10.html')
def feedback(request):
    return render(request,"Feedback.html")

def feedback1(request):
    FirstName=request.POST.get('FirstName')
    LastName=request.POST.get('LastName')
    Email=request.POST.get('Email')
    Comment=request.POST.get('Comment')

    neww=feed.objects.create(FirstName=FirstName,LastName=LastName,Email=Email,Comment=Comment)
    neww.save()
    return HttpResponse("<center><h3>Thanks for your Feedback</h3></center")

# def logout(request):
#     return redirect('home')


def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        t = request.POST.get('hours')
        phonenumber = request.POST.get('phonenumber')

        if Caruserinfo.objects.filter(email=email).exists():
            return render(request,"ForButton.html")

        # Creating the Caruserinfo object
        car_user_info = Caruserinfo.objects.create(name=name, email=email, phonenumber=phonenumber,t=t)

        # Sending email to the user
        subject = 'Hello User'  
        message_body = '<h1 text-align:center>you have successfully booked a car<h1>'
        send_mail(
            subject,
            message_body,
            '200030959cseh@gmail.com',
            [email],
            fail_silently=False,
        )
        print(f'Sent email to {email}')

    return render(request, 'ForButton.html')

