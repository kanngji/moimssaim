import datetime
import os
# from django.core.files.storage import FileSystemStorage

from uuid import uuid4

from django.db import models


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('맛집', '맛집'),
        ('공연', '공연'),
        ('버스킹', '버스킹'),
        ('장소', '장소'),
        ('기타','기타'),
    ]
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    title = models.CharField(max_length=200)

    imgfile = models.ImageField(null=True, upload_to='promotion', blank=True) 
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    discription = models.CharField(max_length=200)
    create_date=models.DateTimeField(null=True)
    meet_date=models.CharField(max_length=200)

    def __str__(self):
        return self.title