from django.db import models
from jaam.projects.models import Project
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField
from jaam.journalism.models import BaseModel

class Act(BaseModel):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project)
    text = RichTextField(default='')
    image = ThumbnailerImageField(('Image'),
                                height_field='',
                                width_field='',
                                upload_to='uploads/photos/act',
                                max_length=200)

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('jaam.act.views.details', (), {
            'project_slug': self.project.slug,
            'act_slug': self.slug,
        })