from rest_framework import serializers

from subscriptions.models import Subscription

from users.api_v1.serializers import CustomUserSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    This serializer provides the Subscription fields needed for it's creation
    """
    user_id = serializers.UUIDField(format='hex')

    class Meta:
        model = Subscription
        fields = (
            'id',
            'user_id',
            'monthly_fee',
            'co2_tons_per_month',
        )
        extra_kwargs = {
            'user_id': {'write_only': True},
            'monthly_fee': {'read_only': True},
            'co2_tons_per_month': {'read_only': True}
        }