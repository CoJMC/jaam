from django.contrib import admin
from jaam.journalism.models import Journalist, Tag, BaseModel

class TagAdmin(admin.ModelAdmin):
    pass

class BaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Journalist)
admin.site.register(Tag, TagAdmin)
