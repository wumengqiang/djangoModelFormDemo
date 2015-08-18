from django.db import models
from django.contrib.auth import get_user_model 
from django.conf import settings
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=8000)
    tagName = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

class Tag(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    tagname = models.CharField(max_length=20)

