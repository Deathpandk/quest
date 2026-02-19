from django.contrib import admin
from django.urls import include, path

from api.router import API_V1_ROUTER

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(API_V1_ROUTER.urls)),
]
