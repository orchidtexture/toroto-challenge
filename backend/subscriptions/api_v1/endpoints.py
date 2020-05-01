from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from users.models import Subscriber

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
        subscriber_id = serializer.validated_data.pop("subscriber_id")
        print(bool(serializer.validated_data))
        try:
            subscriber = Subscriber.objects.get(id=subscriber_id)
            Subscription.objects.create(**{'subscriber': subscriber})
        except Subscriber.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
 
        return Response(status.HTTP_201_CREATED)

