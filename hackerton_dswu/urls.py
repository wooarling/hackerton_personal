from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('board.urls')),  # 루트에서 게시글 관련 URL
    path('admin/', admin.site.urls),
    path('quiz/', include('it_test.urls')),  
    path('accounts/', include('accounts.urls')),  # 로그인/회원가입/로그아웃
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "hackerton_dswu" / "static")
