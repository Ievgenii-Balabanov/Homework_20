from django.urls import include, path

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", ObtainAuthToken.as_view()),
    path("", include("snippets.urls")),
]
