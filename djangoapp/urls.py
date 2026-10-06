from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success_view, name='success_page'),  # 👈 ADD THIS ROUTE
]