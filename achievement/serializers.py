from django.contrib.auth import get_user_model
from rest_framework import serializers
from . models import Achievement



class AchievmentSerializer(serializers.ModelSerializer):
    class Meta:
         fields = '__all__'
         model = Achievement
