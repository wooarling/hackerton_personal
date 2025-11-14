from django.urls import path
from .views import RegisterView, LogoutView, LoginView, TokenRefreshViewCustom, profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),       # 회원가입
    path('login/', LoginView.as_view(), name='login'),                 # JWT 로그인
    path('refresh/', TokenRefreshViewCustom.as_view(), name='token_refresh'),  # 토큰 재발급
    path('logout/', LogoutView.as_view(), name='logout'),             # 로그아웃
    path('profile/', profile, name='profile'),                        # 로그인 상태 확인
]

