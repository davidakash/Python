from django.shortcuts import render

# Create your views here.
def deep(request):
    return render(request,'myapp/index.html') 