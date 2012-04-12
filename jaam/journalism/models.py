from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField
import social_auth.signals
from jaam.journalism.middleware import _show_unpublished
#from jaam.photos.models import Photo
from django.forms import ModelForm

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])

class PublishedObjectsManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        #raise Exception
        if _show_unpublished():
            return super(PublishedObjectsManager, self).get_query_set().order_by('pk')
        else:
            return super(PublishedObjectsManager, self).get_query_set().order_by('pk').filter(published=True)

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

    #objects = models.Manager() # didn't know I explicitly needed this
    #published_objects = PublishedObjectsManager()
    #objects = published_objects
    all_objects = models.Manager()
    objects = PublishedObjectsManager()
    published_objects = objects

    class Meta:
        abstract = True

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    avatar = ThumbnailerImageField(('Personal Photo'),
                                height_field='',
                                width_field='',
                                upload_to='/',
                                max_length=200,
                                null = True,
                                blank = True)
    full_name = models.CharField(max_length=255, blank=True)
    profile_set = models.BooleanField(default = False)

    # Only for journalists
    bio = RichTextField(null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        if self.full_name == "":
            return self.user.username
        else:
            return self.full_name

    def is_journalist(self):
        return self.user.groups.filter(name='Journalists').count() > 0
    
   # def get_photos(self):
        #HELP HERE
    #    return Photo.objects.filter(
     #       pk__in=self.project.photo_set.all().values_list('journalist', flat=True).query
      #  )

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

@receiver(social_auth.signals.pre_update)
def create_full_name(sender, user, response, details, **kwargs):
    user.userprofile.avatar = "http://graph.facebook.com/" + response.get('id', '') + "/picture?type=large"
    user.email = response.get('email', '')
    user.userprofile.full_name = user.get_full_name()
    user.userprofile.save()
    user.save()
    return True
