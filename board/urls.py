from django.urls import path
from .views import post_list, post_detail, post_update, post_delete, post_like_toggle, post_create  # <-- post_create 추가

app_name = 'board'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),  # 새 글 작성 URL
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/update/', post_update, name='post_update'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
    path('<int:pk>/like-toggle/', post_like_toggle, name='post_like_toggle'),
]





