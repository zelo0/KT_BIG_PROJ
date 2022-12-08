from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'core/test.html')

def signin(request):
  return render(request, 'core/signin.html')

def recommend(request):
  return render(request, 'core/recommend.html')