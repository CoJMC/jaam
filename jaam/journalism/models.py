from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class BaseModel(models.Model):
    pass

class Journalist(User):
    bio = models.TextField()
    major = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='/')
    facebookID = models.IntegerField()
    twitterID = models.CharField(max_length=255)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created==True:
        print "this works!"
    else:
        print "this also works!"
