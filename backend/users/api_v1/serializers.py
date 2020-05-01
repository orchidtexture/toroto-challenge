from django.contrib.auth import authenticate

from rest_framework import serializers

from subscriptions.api_v1.serializers import SubscriptionSerializer

from users.models import CustomUser, Subscriber


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
            'password',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'username': {'read_only': True},
            'password': {'write_only': True},
            'id': {'read_only': True},
        }
        partial = True


class SubscriberSerializer(serializers.ModelSerializer):
    """
    This serializer provides the Subscribe fields needed for it's creation
    """
    subscription = SubscriptionSerializer(required=False)
    class Meta:
        model = Subscriber
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'co2_tons_per_year',
            'has_subscription',
            'subscription'
        )
        extra_kwargs = {
            'co2_tons_per_year': {'required': True}
        }
        partial = True


    # def update(self, instance, validated_data):
    #     email = validated_data.get('email')
    #     first_name = validated_data.get('first_name')
    #     last_name = validated_data.get('last_name')
    #     co2_tons_per_year = validated_data.get('co2_tons_per_year')
    #     instance.email = email
    #     instance.first_name = first_name
    #     instance.last_name = last_name
    #     instance.co2_tons_per_year = co2_tons_per_year
    #     if validated_data.get('has_subscription') is True:
    #         subscription_data = validated_data.pop('subscription')
    #         print(subscription_data.get('monthly_fee'))
    #         instance.subscription.monthly_fee = subscription_data.get(
    #             'monthly_fee', 
    #             instance.subscription.monthly_fee
    #         )
    #         instance.subscription.co2_tons_per_month = subscription_data.get(
    #             'co2_tons_per_month', 
    #             instance.subscription.co2_tons_per_month
    #         )
    #     for key, value in validated_data.items():
    #         print(key, value)

    #     return super(SubscriberSerializer, self).update(instance, validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('has_subscription') is True:
            nested_serializer = self.fields['subscription']
            nested_instance = instance.subscription
            # note the data is `pop`ed
            nested_data = dict(validated_data.pop('subscription'))
            print(nested_data)
            print(nested_instance)
            nested_serializer.update(nested_instance, nested_data)
            print(nested_serializer.data)
        # this will not throw an exception,
        # as `profile` is not part of `validated_data`
        return super(SubscriberSerializer, self).update(instance, validated_data)


class LogInSerializer(serializers.Serializer):
    """ Serializer for user Login """
    email = serializers.CharField(label="Email")
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
