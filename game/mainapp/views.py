from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShopSerializer

# Create your views here.
def main(request):
  return render(request, 'mainapp/main.html')

def store(request):
  return render(request, 'mainapp/store.html')

def dic(request):
  return render(request, 'mainapp/dic.html')

def achievement(request):
  return render(request, 'mainapp/achievement.html')

def character(request):
  return render(request, 'mainapp/character.html')

def skills(request):
  return render(request, 'mainapp/skills.html')

class CurrentUserAPI(APIView):
  def get(self, request):
    serializer = ShopSerializer(request.user, context={'request': request})
    return Response(serializer.data)