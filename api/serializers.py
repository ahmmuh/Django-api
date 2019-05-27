from django.contrib.auth import get_user_model
from rest_framework import serializers


from . models import Activities

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Activities




