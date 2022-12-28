from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main),
    path('store', views.store),
    path('dic', views.dic),
    path('achievement', views.achievement),

    path('character', views.character),
    path('skills', views.skills),
    path('result', views.result),
    path('analysis', views.analysis),
    path('api/shop/', views.ShopAPI.as_view()),

    path('room/', views.room),
    path('room/<str:room_name>/', views.pvp)
]