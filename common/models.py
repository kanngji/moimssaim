from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
    address = models.TextField(max_length=255)

    def __str__(self):
        return self.name