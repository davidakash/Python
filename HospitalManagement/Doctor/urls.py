from django.urls import path
from . import views
urlpatterns = [
    path('',views.log),
    path('about/',views.about, name = 'About'),
]
