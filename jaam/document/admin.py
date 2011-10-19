from django.contrib import admin
from jaam.document.models import Document

class DocumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document, DocumentAdmin)