from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from jaam.journalism.models import UserProfile, Journalist, Tag, BaseModel

class TagAdmin(admin.ModelAdmin):
    pass

class BaseAdmin(admin.ModelAdmin):
    pass

class JournalistInline(admin.StackedInline):
    model = Journalist

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [JournalistInline,]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tag, TagAdmin)
