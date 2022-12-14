from rest_framework import serializers
from .models import User

class CurrentUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'profile_image', 'money']