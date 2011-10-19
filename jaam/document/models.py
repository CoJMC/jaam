from django.db import models
from jaam.jaam.models import BaseModel
from doccloud.models import Document as dcDoucment, DocumentCloudProperties

class Document(BaseModel):
    document = models.ForeignKey(dcDoucment) # should this be a foreignkey?
    