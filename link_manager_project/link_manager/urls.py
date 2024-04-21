from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token

from .views import LinkListCreateAPIView, LinkDetailAPIView, CollectionListCreateAPIView, CollectionDetailAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Link Manager API",
        default_version='v1',
        description="API для хранения ссылок пользователя",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@linkmanager.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/links/', LinkListCreateAPIView.as_view(), name='link-list-create'),
    path('api/links/<int:pk>/', LinkDetailAPIView.as_view(), name='link-detail'),
    path('api/collections/', CollectionListCreateAPIView.as_view(), name='collection-list-create'),
    path('api/collections/<int:pk>/', CollectionDetailAPIView.as_view(), name='collection-detail'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
