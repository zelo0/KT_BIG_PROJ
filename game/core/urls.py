from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recommend/', views.recommend),
    path('battle/', views.pve),
    path('api/user/', views.CurrentUserAPI.as_view()),
    path('api/achievement/', views.AchievementAPI.as_view()),
    path('api/achieveuser/', views.AchieveUserAPI.as_view()),
    path('share/', views.share)
]