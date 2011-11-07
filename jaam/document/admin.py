from django.contrib import admin
from jaam.document.models import Document
from jaam.journalism.admin import BaseAdmin

class DocumentAdmin(BaseAdmin):
    list_display = ('__unicode__', 'title',)
    list_filter = ('title',)

admin.site.register(Document, DocumentAdmin)