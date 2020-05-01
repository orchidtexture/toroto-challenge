from django.urls import path

from subscriptions.api_v1 import endpoints

urlpatterns = [
    path(
        route='subscriptions/',
        view=endpoints.CreateSubscription.as_view(),
        name='subscription_create'
    ),
]
