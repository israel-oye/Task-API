from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    path('register', views.register_user, name='register_view'),
    path('login', TokenObtainPairView.as_view(), name='login_view'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token', TokenVerifyView.as_view(), name='token_verify'),
]