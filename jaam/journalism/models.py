from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created==True:
        j = Journalist()
        j.user = instance
        j.save()
        print "this works!"
    else:
        print "this also works!"