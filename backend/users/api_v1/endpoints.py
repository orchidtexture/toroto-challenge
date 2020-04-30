from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from users.models import CustomUser

from .serializers import CustomUserSerializer, LogInSerializer

class RegisterUserEndpoint(APIView):
    """ Endpoint responsible for creating an user """
    throttle_classes = ()
    permission_classes = ()
    serializer_class = CustomUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['email']
        serializer.validated_data['username'] = username
        user = CustomUser.objects.create_user(**serializer.validated_data)
        
        token = Token.objects.create(user=user)
                        
        return Response({'token': token.key})


class CustomAuthToken(APIView):
    """ 
    Endpoint responsible for authenticating an user and generating a token 
    """
    throttle_classes = ()
    permission_classes = ()
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
        

class RetrieveUserList(generics.ListAPIView):
    """ Endpoint responsible for returning users list """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint responsible for retrieving, updating and destroying user instances
    """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'
