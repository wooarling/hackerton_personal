# models.py
from django.db import models

# 분야 (백엔드, 프론트엔드 등)
class Field(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 분야 이름 (예: 백엔드, 프론트엔드)

    def __str__(self):
        return self.name


# 질문
class Question(models.Model):
    text = models.TextField()  # 질문 내용
    fields = models.ManyToManyField(Field, related_name='questions')  # 여러 분야에 매핑됨

    def __str__(self):
        return self.text
