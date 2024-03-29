from django.shortcuts import render
from rest_framework import generics
from .models import Activities
from .serializers import ActivitiesSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class ActivityList(generics.ListAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer



class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer

class Login(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
    
