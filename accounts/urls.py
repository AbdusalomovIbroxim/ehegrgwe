from django.urls import path
from .views import UserProfileView, UserUpdateView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('me/', UserProfileView.as_view(), name='user-profile'),
    path('me/update/', UserUpdateView.as_view(), name='user-update'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
]
