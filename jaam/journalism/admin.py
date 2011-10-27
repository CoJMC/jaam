from django.contrib import admin
from jaam.journalism.models import BaseModel
from jaam.journalism.models import Journalist


class BaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Journalist)
