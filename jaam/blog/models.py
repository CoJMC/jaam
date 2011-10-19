from django.db import models
from jaam.journalism.models import BaseModel

class BlogPost(BaseModel):
    blog
    headline
    description
    body
    author
    pass

class Blog(BaseModel):
    project
    title
    subtitle
    description
    pass