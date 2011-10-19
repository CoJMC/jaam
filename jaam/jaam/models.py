from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    pass

class Journalist(User):
    pass