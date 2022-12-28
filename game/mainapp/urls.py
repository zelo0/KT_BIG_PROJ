from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main', views.main),
    path('store', views.store),
    path('dic', views.dic),
    path('achievement', views.achievement),
    path('analysis', views.analysis),

    path('character', views.character),
    path('skills', views.skills),
    path('api/shop/', views.shopAPI.as_view()),
    path('api/item/', views.ItemAPI.as_view()),
    path('api/store-post/', views.StoreAPI.as_view()),
    path('api/store-money/', views.StoreAPI.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)