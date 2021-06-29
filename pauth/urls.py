from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .customize.views import PObtainTokenPairView
from .views import RegisterView, ChangePasswordView, HelloView
from django.contrib.auth import views as auth_views

from rest_framework import routers

urlpatterns = [
    path('token/', PObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', RegisterView.as_view()),
    path('changepassword/', ChangePasswordView.as_view(), name="auth_change_password"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('test/', HelloView.as_view()),
]