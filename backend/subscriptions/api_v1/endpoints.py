from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from users.models import Subscriber

from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer, SubscriptionUpdateSerializer

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
        try:
            subscriber = Subscriber.objects.get(id=subscriber_id)
            subscriber.has_subscription = True
            co2_tons_per_year = subscriber.co2_tons_per_year
            subscriber.save()
            co2_tons_per_month =  co2_tons_per_year / 12
            # Insert Toroto's secret formula here
            monthly_fee = float(co2_tons_per_month) * 12.0
            Subscription.objects.create(**{
                'subscriber': subscriber,
                'co2_tons_per_month': co2_tons_per_month,
                'monthly_fee': monthly_fee
            })
        except Subscriber.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
 
        return Response(status.HTTP_201_CREATED)


class RetrieveSubscription(generics.RetrieveUpdateAPIView):
    throttle_classes = ()
    permission_classes = ()
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionUpdateSerializer
    lookup_field = 'id'
