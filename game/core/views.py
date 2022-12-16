from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
  return render(request, 'core/test.html')

def recommend(request):
  products = Beautyproduct.objects.all()
  return render(request, 'core/recommend.html', {'products': products})

def pve(request):
  return render(request, 'core/PvE.html')