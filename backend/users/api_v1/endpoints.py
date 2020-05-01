from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


from users.models import CustomUser, Subscriptor

from .serializers import (
    CustomUserSerializer, 
    LogInSerializer, 
    SubscriptorSerializer
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


class CreateSubscriptorEndpoint(generics.CreateAPIView):
    """ Endpoint responsible for creating a user """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptorSerializer
    

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
    lookup_field = 'id'


class RetrieveSubscriptorsList(generics.ListAPIView):
    """ Endpoint responsible for returning a subscriptors list """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = Subscriptor.objects.all()
    serializer_class = SubscriptorSerializer


class RetrieveUpdateDestroySubscriptor(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint responsible for retrieving, updating and destroying subscriptor 
    instances
    """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = Subscriptor.objects.all()
    serializer_class = SubscriptorSerializer
    lookup_field = 'id'
