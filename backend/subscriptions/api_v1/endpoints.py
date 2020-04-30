from rest_framework import generics

from subscriptions.models import Subscription

from .serializers import SubscriptionSerializer

class CreateSubscription(generics.ListCreateAPIView):
    """ Endpoint responsible for creating a subscription """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class RetrieveUpdateDestroySubscription(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint responsible for retrieving, updating and destroying Subscription 
    instances
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'id'
