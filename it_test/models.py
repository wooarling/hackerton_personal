# models.py
from django.db import models

# 분야 (예: 백엔드, 프론트엔드 등)
class Field(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# 질문 (각 질문은 하나 이상의 분야에 속할 수 있음)
class Question(models.Model):
    text = models.CharField(max_length=255)
    fields = models.ManyToManyField(Field)

    def __str__(self):
        return self.text

# 사용자 응답 (각 질문에 대한 사용자의 응답을 저장)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10)  # '예' 또는 '아니오'

    def __str__(self):
        return f"Q{self.question.id}: {self.answer}"
