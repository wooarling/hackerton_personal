from django.db import models
from django.conf import settings  # 추가

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', '프론트엔드'),
        ('backend', '백엔드'),
        ('ai', '인공지능'),
        ('iot', '사물인터넷'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 수정
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)  # 수정

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"
