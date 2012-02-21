from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from jaam.journalism.models import BaseModel, User
from ckeditor.fields import RichTextField

class ProjectLocation(models.Model):
    location = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.location

class Project(BaseModel):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=250)
    primaryColor = models.CharField(max_length=7,default="FF0000")
    accentColor = models.CharField(max_length=7, default="FFFFFF")
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    locations = models.ManyToManyField(ProjectLocation)
    coverGallery = models.ForeignKey('photos.PhotoGallery', null=True, blank=True, related_name='+')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.projects.views.details', (), {
            'project_slug': self.slug,
        })

    @property
    def journalists(self):
        return User.objects.filter(
            pk__in=self.photo_set.all().values_list('journalist', flat=True).query
        )

@receiver(pre_save, sender=Project)
def add_pound(instance, **kwargs):
    if len(instance.primaryColor) < 7:
        instance.primaryColor = "#" + instance.primaryColor.upper()
    if len(instance.accentColor) < 7:
        instance.accentColor = "#" + instance.accentColor.upper()
