from rest_framework import serializers

from subscriptions.models import Subscription

from users.api_v1.serializers import CustomUserSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    This serializer provides the Subscription fields needed for it's creation
    """
    user = CustomUserSerializer()
    class Meta:
        model = Subscription
        fields = (
            'id',
            'user',
            'monthly_fee',
            'co2_tons_per_month',
        )