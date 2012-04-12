from django.contrib import admin
from jaam.act.models import Act
from jaam.journalism.admin import BaseAdmin

class ActAdmin(BaseAdmin):
    list_display = ('__unicode__', 'project', 'text',)
    list_filter = ('project',)
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, { 'fields':
            ('project', 'title', 'slug', 'image', 'text', 'tags') }),
        ('Admin', { 'fields':
            ('published',) }),
    )

    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Act, ActAdmin)
