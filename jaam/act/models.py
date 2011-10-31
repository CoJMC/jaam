from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Act(models.Model):
    title = models.CharField(max_length=100)
    act_code = RichTextField()

    def __unicode__(self):
        return self.title
