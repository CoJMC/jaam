from django.contrib import admin
from jaam.document.models import Document
from jaam.journalism.admin import BaseAdmin

class DocumentAdmin(BaseAdmin):
    pass

admin.site.register(Document, DocumentAdmin)