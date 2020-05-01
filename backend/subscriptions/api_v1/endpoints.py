from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from users.models import Subscriptor

from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer

class CreateSubscription(APIView):
    """ Endpoint responsible for creating a subscription """
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscriptor_id = serializer.validated_data.pop("subscriptor_id")
        print(bool(serializer.validated_data))
        try:
            subscriptor = Subscriptor.objects.get(id=subscriptor_id)
            Subscription.objects.create(**{'subscriptor': subscriptor})
        except Subscriptor.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
 
        return Response(status.HTTP_201_CREATED)
