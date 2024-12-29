from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
# from.forms import *
# from .models import hospital as H
# Create your views here.

def about(request):
    return render(request,'about.html')



def log(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
             print(user)
             login(request,user)
             return redirect('About')
    return render(request,'login.html')

# def doc(request):
#     return render(request,'base.html')

# def home(request):
#     if request.method == "POST":
#         data=Patient_forms(request.POST,request.FILES)
#         if data.is_valid:
#             print(request.POST)
#             data.save()
#     return render(request,'Home.html',{'OP':Patient_forms()})

# def update_page(request,id):
#     data=H.objects.get(id=id)
#     data1=Patient_forms(request.POST,request.FILES,instance=data)
#     print(data1)
#     if request.method == "POST":
#         data.Name=request.POST['Name']
#         data.Age=request.POSt['Age']
#         data.Gender=request.POST['Gender']
#         data.save()
#         return redirect("redir")
#     return render(request,'update.html',{'detailes':data})

# def Delete_page(request,id):
#     data=H.objects.get(id=id)
#     data.delete()
#     return redirect("redir")

# def list_page(request):
#     data=H.objects.all()
#     return render(request,'list.html',{'detailes':data})