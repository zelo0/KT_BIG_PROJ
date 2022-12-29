from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers import *
from core.models import User
from .serializers import ShopSerializer
import redis


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

def analysis(request):
  return render(request, 'mainapp/analysis.html')

class shopAPI(APIView):
  def get(self, request):
    shop_list = Shop.objects.all()
    serializer = ShopSerializer(shop_list, many=True)
    return Response(serializer.data)
  
class ItemAPI(APIView):
  def get(self, request):
    Item_list = Item.objects.prefetch_related('history').all()
    serializer = ItemSerializer(Item_list, many=True)
    return Response(serializer.data)
  
class StoreAPI(APIView) :
  def post(self, request) :
    Post = StorePostSerializer(data=request.data)
    print('post 요청')
    print(Post)
    if Post.is_valid() :
      print('post alive')
      Post.save()
      return Response(Post.data)
    else :
      print('post dead')
      return Response(Post.data)
    
  def patch(self, request) :
    value = int(request.data.__getitem__('money'))
    data = request.user.money - value
    request.user.money = data
    request.user.save()
    return Response()
    
class HavingItemAPI(APIView):
  def get(self, request):
    HavingItem_list = HavingItem.objects.all()
    serializer = HavingItemSerializer(HavingItem_list, many=True)
    return Response(serializer.data)
  
class WearingItemAPI(APIView):
  def get(self, request):
    Wearing_list = wearing.objects.all()
    serializer = WearingSerializer(Wearing_list, many=True)
    return Response(serializer.data)
  
def result(request):
  left_eye_cnt = request.GET.get('left_eye', 0)
  right_eye_cnt = request.GET.get('right_eye', 0)
  mouth_cnt = request.GET.get('mouth', 0)
  return render(request, 'mainapp/result.html', {
    'left_eye_cnt': left_eye_cnt,
    'right_eye_cnt': right_eye_cnt,
    'mouth_cnt': mouth_cnt
  })

def find_room(request):
  return render(request, 'mainapp/find-room.html')

# 대기실
def wait_room(request, room_name):
  # 방 목록 저장 redis
  redis_client = redis.StrictRedis.from_url("rediss://red-cegkhc02i3mkhvoakgh0:Z6M9PSoaNV0aOv0XR2y3CmJ8TpYGGGfQ@singapore-redis.render.com:6379/10", encoding="utf-8", decode_responses=True)
  # 대기실에 들어오는 사람이 없으면 
  redis_client.expire(room_name, 60 * 10) # 단위(초) - 10분 뒤에 방 삭제
  redis_client.sadd(room_name, request.user.username)
  players_in_room =  redis_client.smembers(room_name)
  print(players_in_room)
  return render(request, 'mainapp/wait-room.html', {
    'players_in_room': players_in_room,
    'room_name': room_name,
  })

def pvp(request, room_name):
  return render(request, 'mainapp/pvp.html', {
    'room_name': room_name,
    'player_name': request.user.username
  })
