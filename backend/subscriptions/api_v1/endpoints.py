from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import CustomUser

from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer

class CreateSubscription(APIView):
    """ Endpoint responsible for creating a subscription """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data.pop("user_id")
        print(bool(serializer.validated_data))
        try:
            print(user_id)
            user = CustomUser.objects.get(id=user_id)
            Subscription.objects.create(**{'user': user})
        except CustomUser.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
 
        return Response(status.HTTP_201_CREATED)
