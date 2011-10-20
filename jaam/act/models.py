from django.db import models

# Create your models here.
class Act(models.Model):
    title = models.CharField(max_length=100)
    act_code = models.TextField()   