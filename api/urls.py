"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Project-Planner API",
        default_version='v1',
        description="Project-Planner API Endpoints",
        terms_of_service="",
        contact=openapi.Contact(email="info@planner.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(),
)


urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name= 'Project-PlannerAPI-Docs'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name= 'Project-Planner-API-Docs'),
    path('admin/', admin.site.urls),
    path('api/',include('Account.urls')),
    path('api/',include('Project.urls')),
    path("api/", include('djoser.urls')),
    path('', include('social_accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
