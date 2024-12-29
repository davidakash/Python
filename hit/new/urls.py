from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_page, name ='Login'),
    path('new/',views.go ),
    path('about/',views.went,name='Home'),
    path('contact/',views.goes),
    path('image/',views.add_items),
    path('logout/',views.log_out),
]