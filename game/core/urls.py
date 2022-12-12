from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recommend/', views.recommend),
    path('api/user/', views.CurrentUserAPI.as_view())
]