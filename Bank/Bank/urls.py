"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from cash.views import *

router = DefaultRouter()
router.register(r'api',BankProducts)
router.register(r'file',acc)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Product/',include(router.urls))
    # path('Product/<id>/',json_data.as_view()),
]
