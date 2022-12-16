from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CurrentUserSerializer

# Create your views here.
def index(request):
  return render(request, 'core/test.html')

def recommend(request):
  products = Beautyproduct.objects.all()
  return render(request, 'core/recommend.html', {'products': products})

<<<<<<< HEAD
def pve(request):
  return render(request, 'core/PvE.html')
=======
def share(request):
  return render(request, 'core/share.html')

class CurrentUserAPI(APIView):
  def get(self, request):
    serializer = CurrentUserSerializer(request.user, context={'request': request})
    return Response(serializer.data)
>>>>>>> 5fda7972e03cfc6b69fb84cb7ce92ee26f6fa6d7
