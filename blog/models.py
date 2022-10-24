from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# class : 첫 번째 글자 대문자
# function : 두 번째 글자 대문자

class Post(models.Model):
    title = models.CharField(max_length=30) # 글자수 제한 가능
    content = models.TextField() # 글자수 제한 없음

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} {self.create_at}'