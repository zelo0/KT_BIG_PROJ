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

def result(request):
  left_eye_cnt = request.GET.get('left_eye', 0)
  right_eye_cnt = request.GET.get('right_eye', 0)
  mouth_cnt = request.GET.get('mouth', 0)
  return render(request, 'mainapp/result.html', {
    'left_eye_cnt': left_eye_cnt,
    'right_eye_cnt': right_eye_cnt,
    'mouth_cnt': mouth_cnt
  })
class ShopAPI(APIView):
  def get(self, request):
    shop_list = Shop.objects.prefetch_related('item').all()
    serializer = ShopSerializer(shop_list, many=True)
    return Response(serializer.data)

def room(request):
  return render(request, 'mainapp/room-share.html')

def pvp(request, room_name):
  return render(request, 'mainapp/pvp.html', {
    'room_name': room_name,
    'player_name': request.user.username
  })