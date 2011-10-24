from django.db import models
from jaam.journalism.models import BaseModel
from doccloud.models import Document as dcDoucment, DocumentCloudProperties

class Document(BaseModel):
    title = models.CharField(max_length=255)
    document = models.ForeignKey(dcDoucment) # should this be a foreignkey?

    def __unicode__(self):
        return self.title
