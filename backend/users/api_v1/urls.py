from django.urls import path

from users.api_v1 import endpoints

urlpatterns = [
    # {% url 'api_v1_users:users' %}
    path(
        route='subscriptors/',
        view=endpoints.RetrieveSubscriptorsList.as_view(),
        name='subscriptors_list'
    ),
    path(
        route='users/staff/register/',
        view=endpoints.RegisterStaffUserEndpoint.as_view(),
        name='staff_register'
    ),
    path(
        route='users/<uuid:id>/',
        view=endpoints.RetrieveUpdateDestroyStaff.as_view(),
        name='staff_retrieve'
    ),

    path(
        route='users/subscriptors/',
        view=endpoints.CreateSubscriptorEndpoint.as_view(),
        name='subscriptors'
    ),
    path(
        route='users/login/',
        view=endpoints.CustomAuthToken.as_view(),
        name='user_login'
    ),
    path(
        route='subscriptors/<uuid:id>/',
        view=endpoints.RetrieveUpdateDestroySubscriptor.as_view(),
        name='subscriptor_retrieve'
    ),
]
