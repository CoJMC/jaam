from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    pass

class Journalist(User):
    bio = models.TextField()
    major = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='/')
    facebookID = models.IntegerField()
    twitterID = models.CharField(max_length=255)