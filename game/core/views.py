from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CurrentUserSerializer
from youtube_upload.client import YoutubeUploader
import os
from django.conf import settings

from oauth2client.tools import argparser
from googleapiclient.errors import HttpError

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


# Create your views here.
def index(request):
  return render(request, 'core/test.html')

def recommend(request):
  products = Beautyproduct.objects.all()
  return render(request, 'core/recommend.html', {'products': products})

def pve(request):
  return render(request, 'core/PvE.html')
def share(request):
  return render(request, 'core/share.html')

def file_path(filename):
  return os.path.join(settings.BASE_DIR, 'share', filename)

# def upload_to_youtube(request):
#   args = argparser.parse_args()
#   # 임의 설정
#   args.file = "game/share/test.mp4"
#   args.title = "test game"
#   args.category = "42" # SHORTS
#   args.privacyStatus = VALID_PRIVACY_STATUSES[0]
#   args.auth_host_port = 8000

#   if not os.path.exists(args.file):
#     exit("Please specify a valid file using the --file= parameter.")

#   youtube = get_authenticated_service(args)
#   try:
#     initialize_upload(youtube, args)
#   except HttpError as e:
#     print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

class CurrentUserAPI(APIView):
  def get(self, request):
    serializer = CurrentUserSerializer(request.user, context={'request': request})
    return Response(serializer.data)
