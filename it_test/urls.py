from django.urls import path
from . import views

app_name = 'it_test'  # ← 반드시 추가

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('test/', views.test_page, name='test_page'),
    path('questions/', views.get_questions, name='get_questions'),
    path('submit/', views.submit_test, name='submit_test'),
    path('result/', views.result_page, name='result_page'),
]
