from django.conf import settings

from rest_framework import generics
from rest_framework import status, filters
from rest_framework.response import Response

from users.models import CustomUser

from .serializers import CustomUserSerializer

class CreateUser(generics.ListCreateAPIView):
    """ Endpoint responsible for creating an user """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint responsible for retrieving, updating and destroying user instances
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'
