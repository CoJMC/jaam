from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class BaseModel(models.Model):
    pass

class Journalist(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    bio = RichTextField(null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='/', null = True, blank=True)
    facebookID = models.IntegerField(null=True, blank=True)
    twitterID = models.CharField(max_length=255, null=True, blank=True)