from django.db import models
from django.contrib.auth.models import User

#create models here
class Profile(models.Model):
    user = models.OneToOneField(User)
    blurb = models.CharField(max_length=1000)