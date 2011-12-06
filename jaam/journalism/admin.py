from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from jaam.journalism.models import UserProfile, Journalist, Tag, BaseModel
from django.contrib.auth.models import Group, Permission, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

class NewUserAdmin(UserAdmin):
    actions = ['promote_to_journalist', 'demote_from_journalist']
    
    def promote_to_journalist(self, request, queryset):
        for user in queryset.all():
            user.groups.add(Group.objects.get(name="Journalists"))
            user.is_staff = True
            user.save()
    
    def demote_from_journalist(self, request, queryset):
        for user in queryset.all():
            user.groups.remove(Group.objects.get(name="Journalists"))
            user.is_staff = False
            user.save()

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)