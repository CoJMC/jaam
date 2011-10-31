from django.db import models
from jaam.journalism.models import BaseModel, Journalist
from jaam.projects.models import Project

class Video(BaseModel):
    journalist = models.ForeignKey(Journalist)
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=100)
    caption = models.TextField(null=True, blank=True)
    videoUrl = models.CharField(max_length=200,)
    videoId = models.CharField(max_length = 200 ,editable=False)
    
    def __unicode__(self):
        return self.title
    
    def scrapeVideoId(self):
        stringUrl = self.videoUrl.__str__()
        
        #check to see which link type
        split_location = stringUrl.find('v=')
        
        if split_location != -1:
            first_split = split_location +2
            foundId = self.videoUrl[first_split:]
            if foundId.find('&') != -1:
                return foundId[0:foundId.find('&')]
            else:
                return foundId
        
        else:
            first_split = stringUrl.find('be/') + 3
            return self.videoUrl[first_split:]    
        
    
    def save(self, *args, **kwargs):
        #code to execute pre-save
        print 'test'
        self.videoId = self.scrapeVideoId()
        
        #parent's save function
        super(Video, self).save(*args, **kwargs)
        
        #code to execute post-save

class VideoGallery(BaseModel):
    title = models.CharField(max_length=100)
    introduction = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project)
    class Meta:
        verbose_name = "video gallery"
        verbose_name_plural = "video galleries"

    def __unicode__(self):
        return self.title