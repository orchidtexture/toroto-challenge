from django.urls import path

from users.api_v1 import endpoints

urlpatterns = [
    # {% url 'api_v1_users:users' %}
    path(
        route='users/',
        view=endpoints.CreateUser.as_view(),
        name='user_create'
    ),

]
