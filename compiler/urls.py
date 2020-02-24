from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index2.html',views.index2,name='index2'),
    path('compile.html',views.compile,name='compile'),
    

]