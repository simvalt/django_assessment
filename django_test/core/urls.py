"""core URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("user.urls")),
    path("payments/", include("payments.urls")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #for views with templates
    path("", TemplateView.as_view(template_name="_home.html"), name="home"),
    path("users/", include("django.contrib.auth.urls")), 
]
