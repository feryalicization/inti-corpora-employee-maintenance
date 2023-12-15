from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


schema_view = get_schema_view(
    openapi.Info(
        title="Emoloyee Maintenance API",
        default_version='v1',
        description="API for test PT Inti Corpora Teknologi",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('employee', EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('api/token', obtain_auth_token, name='api_token'),
    path('api/register', UserRegistrationView.as_view(), name='user_register'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]