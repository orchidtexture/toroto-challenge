from django.urls import path

from users.api_v1 import endpoints

urlpatterns = [
    # {% url 'api_v1_users:users' %}
    path(
        route='users/',
        view=endpoints.RetrieveUserList.as_view(),
        name='users_list'
    ),
    path(
        route='users/register/',
        view=endpoints.RegisterUserEndpoint.as_view(),
        name='user_register'
    ),
    path(
        route='users/login/',
        view=endpoints.CustomAuthToken.as_view(),
        name='user_login'
    ),
    path(
        route='users/<id>/',
        view=endpoints.RetrieveUpdateDestroyUser.as_view(),
        name='user_retrieve'
    ),
]
