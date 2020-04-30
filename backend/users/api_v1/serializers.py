from rest_framework import serializers

from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    This serializer provides the CustomUser fields needed for it's creation
    """
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'co2_tons_per_year'
        )
        extra_kwargs = {
            'username': {'read_only': True},
            'co2_tons_per_year': {'required': True}
        }
        partial = True
