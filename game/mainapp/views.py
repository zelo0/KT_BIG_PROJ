from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers import *
from core.models import User

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
  