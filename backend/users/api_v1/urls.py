from django.urls import path

from users.api_v1 import endpoints

urlpatterns = [
    # {% url 'api_v1_users:users' %}
    path(
        route='subscribers/',
        view=endpoints.RetrieveSubscribersList.as_view(),
        name='subscribers_list'
    ),
    path(
        route='users/staff/register/',
        view=endpoints.RegisterStaffUserEndpoint.as_view(),
        name='staff_register'
    ),
    path(
        route='users/',
        view=endpoints.RetrieveUpdateDestroyStaff.as_view(),
        name='staff_retrieve'
    ),

    path(
        route='subscribers/new/',
        view=endpoints.CreateSubscriberEndpoint.as_view(),
        name='subscribers'
    ),
    path(
        route='users/login/',
        view=endpoints.CustomAuthToken.as_view(),
        name='user_login'
    ),
    path(
        route='subscribers/<uuid:id>/',
        view=endpoints.RetrieveUpdateDestroySubscriber.as_view(),
        name='subscriber_retrieve'
    ),
]
