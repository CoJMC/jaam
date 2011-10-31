from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Act(models.Model):
    title = models.CharField(max_length=100)
<<<<<<< HEAD
    act_code = RichTextField()
     
    def __unicode__(self):
        return self.title
=======
    act_code = RichTextField()
>>>>>>> 109f366ca961e9becfbc7478437423343cffeadc
