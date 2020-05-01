from rest_framework import serializers

from subscriptions.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    This serializer provides the Subscription fields needed for it's creation
    """
    subscriptor_id = serializers.UUIDField(format='hex', write_only=True)

    class Meta:
        model = Subscription
        fields = (
            'id',
            'subscriptor_id',
            'monthly_fee',
            'co2_tons_per_month',
        )
