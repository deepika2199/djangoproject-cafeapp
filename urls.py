from django.contrib import admin
from django.urls import path,include
from travello import views

urlpatterns = [
    
    path('', views.index, name='travello')

]