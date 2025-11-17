from django.urls import path
from .views import register_page, login_page, logout_view, RegisterView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_view, name='logout'),
    
    # API용 URL
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/login/', LoginView.as_view(), name='api_login'),
]
