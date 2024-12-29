from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .models import * 
from .forms import *
# Create your views here
Foods = Food_items.objects.all()

def go(request):
    Foods = Food_items.objects.all()
    return render(request,'NEW/index.html',{'Items':Foods})
def went(request):
    SoftDrinks =Soft_drinks.objects.all()
    return render(request,'NEW/about.html',{'Menu':SoftDrinks})
def goes(request):
    if request.method == "POST":
        data=Bill_Items_Forms(request.POST,request.FILES)
        if data.is_valid:
            print(request.POST)
            data.save()
    return render(request,'NEW/contact.html',{'Bill':Bill_Items_Forms()})

def add_items(request):
    if request.method == "POST":
        data=Soft_drinks_Forms(request.POST,request.FILES)
        if data.is_valid:
            print(request.POST)
    return render(request,'NEW/image.html',{'dada':Soft_drinks_Forms()})

def login_page(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],password = request.POST['password'])

        if user is not None:
             print(user)
             login(request,user)
             return redirect('Home')
    return render(request,'NEW/login.html')

def log_out(request):
    logout(request)
    return redirect('Login')