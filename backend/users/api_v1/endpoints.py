from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_object_or_404


from users.models import CustomUser, Subscriber

from .serializers import (
    CustomUserSerializer, 
    LogInSerializer, 
    SubscriberSerializer
)


class RegisterStaffUserEndpoint(APIView):
    """ Endpoint responsible for creating a Toroto staff user """
    throttle_classes = ()
    permission_classes = ()
    serializer_class = CustomUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['email']
        serializer.validated_data['username'] = username
        serializer.validated_data['toroto_staff'] = True
        user = CustomUser.objects.create_user(**serializer.validated_data)
        
        token = Token.objects.create(user=user)
                        
        return Response({'token': token.key})


class CreateSubscriberEndpoint(generics.CreateAPIView):
    """ Endpoint responsible for creating a subscriber """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriberSerializer
    

class CustomAuthToken(APIView):
    """ 
    Endpoint responsible for authenticating an user and generating a token 
    """
    throttle_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(user)
        if not created:
            token.delete()
            token = Token.objects.create(user=user)
        return Response({
            'token': token.key
        })


class RetrieveUpdateDestroyStaff(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint responsible for retrieving, updating and destroying Staff 
    instances
    """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, email=self.request.user.email)
        return obj


class RetrieveSubscribersList(generics.ListAPIView):
    """ Endpoint responsible for returning a subscribers list """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class RetrieveUpdateDestroySubscriber(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint responsible for retrieving, updating and destroying subscriber 
    instances
    """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    lookup_field = 'id'

