from rest_framework import serializers

from subscriptions.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    This serializer provides the Subscription fields needed for it's creation
    """
    subscriber_id = serializers.UUIDField(format='hex', write_only=True)

    class Meta:
        model = Subscription
        fields = (
            'id',
            'subscriber_id',
            'monthly_fee',
            'co2_tons_per_month',
        )
        extra_kwargs = {
            'id': {'read_only': True}
        }


class SubscriptionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = (
            'monthly_fee',
            'co2_tons_per_month'
        )

