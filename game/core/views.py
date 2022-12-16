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

def share(request):
  return render(request, 'core/share.html')

class CurrentUserAPI(APIView):
  def get(self, request):
    serializer = CurrentUserSerializer(request.user, context={'request': request})
    return Response(serializer.data)
