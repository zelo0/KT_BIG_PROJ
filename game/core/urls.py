from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # 제거
    path('signin/', views.signin),
    path('recommend/', views.recommend),
]