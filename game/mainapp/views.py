from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShopSerializer, ItemSerializer
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

def storePost(request) :
  if request.method=='POST':
    post = HavingItem()
    post.userID = request.POST['userID']
    post.itemID = request.POST['itemID']
    
    userPost = User()
    userPost.money = request.POST['money']
    
    post.save()
    userPost.save()