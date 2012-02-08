from django.contrib import admin
from jaam.journalism.models import UserProfile, Tag
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
#from django.contrib.admin import SimpleListFilter

class TagAdmin(admin.ModelAdmin):
    pass

class BaseAdmin(admin.ModelAdmin):
    pass

#class UserProfileInline(admin.TabularInline):
#    model = UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

# Uh yeah, this isn't supported until django-1.4
#class IsJournalistFilter(SimpleListFilter):
#    title = _('is journalist')
#    parameter_name = 'is_journalist'
#
#    def lookups(self, request, model_admin):
#        return (
#            ('true', _('is journalist')),
#            ('false', _('is not journalist')),
#        )
#
#    def queryset(self, request, queryset):
#        if self.value() == 'true':
#            return queryset.filter(birthday__year__gte=1980,
#                                    birthday__year__lte=1989)
#            # lol what goes here?
#        if self.value() == 'false':
#            return queryset.filter(birthday__year__gte=1990,
#                                   birthday__year__lte=1999)
#            # lol what goes here?

class NewUserAdmin(UserAdmin):
    actions = ['promote_to_journalist', 'demote_from_journalist']
    #list_filter = UserAdmin.list_filter + (IsJournalistFilter,)
    # not sure how to do this...
    list_filter = UserAdmin.list_filter + ('groups__name',)
    #inlines = UserAdmin.inlines + [UserProfileInline]

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