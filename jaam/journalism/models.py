from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from social_auth.signals import pre_update

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])

class PublishedObjectsManager(models.Manager):
    def get_query_set(self):
        return super(PublishedObjectsManager, self).get_query_set().filter(published=True)

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager() # little bugger, didn't know I explicitly needed this
    published_objects = PublishedObjectsManager()

    class Meta:
        abstract = True

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    # TODO: make the avatar a thumbnail field
    avatar = models.ImageField(upload_to='/', null = True, blank=True)
    full_name = models.CharField(max_length=255, blank=True)

    # Only for journalists
    bio = RichTextField(null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return self.user.username

    def is_journalist(self):
        return self.user.groups.filter(name='Journalists').count() > 0
    
    def __unicode__(self):
        return self.full_name

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.journalism.views.user_profile', (), {
            'username': self.user.username
        })

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created==True:
            user_profile = UserProfile()
            user_profile.user = instance
            user_profile.save()
            
@receiver(pre_update)
def create_full_name(sender, user, response, details, **kwargs):
    user.email = response.get('email', '')
    user.userprofile.full_name = user.get_full_name()
    user.userprofile.save()
    user.save()
    return True