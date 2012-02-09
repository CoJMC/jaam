from django.contrib import admin
from jaam.act.models import Act
from jaam.journalism.admin import BaseAdmin

class ActAdmin(BaseAdmin):
    list_display = ('__unicode__', 'title')
    list_filter = ('project',)
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, { 'fields':
            ('project', 'title', 'slug', 'act_code', 'tags') }),
        ('Admin', { 'fields':
            ('published',) }),
    )
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        return super(ActAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Act, ActAdmin)