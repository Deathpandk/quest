from django.urls import include, path

from .v1.router import API_V1_ROUTER

urlpatterns = [
    path("v1/", include(API_V1_ROUTER.urls)),
]
