from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path(
        "api/v1/auth/",
        TokenObtainPairView.as_view(),
        name="auth_get_token",
    ),
    path("api/v1/auth/refresh/", TokenRefreshView.as_view(), name="auth_refresh_token"),
]

if settings.ENV != "test":
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.ENV == "local":
    urlpatterns.append(path("", TemplateView.as_view(template_name="home.html")))
    urlpatterns += static(settings.COV_URL, document_root=settings.COV_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
