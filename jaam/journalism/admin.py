from django.contrib import admin
from jaam.journalism.models import UserProfile, Tag
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
#from django.contrib.admin import SimpleListFilter

class TagAdmin(admin.ModelAdmin):
    pass

class BaseAdmin(admin.ModelAdmin):
    actions = ['publish', 'unpublish']
    save_on_top = True
    def publish(self, request, queryset):
        queryset.all().update(published=True)
    def unpublish(self, request, queryset):
        queryset.all().update(published=False)

    # All fields in the 'admin' fieldset are hidden from non-admins
    def get_fieldsets(self, request, obj=None, **kwargs):
        fieldsets = super(BaseAdmin, self).get_fieldsets(request, obj)
        if not request.user.is_superuser:
            non_admin_fieldsets = []
            for fieldset in fieldsets:
                if not fieldset[0] == 'Admin':
                    non_admin_fieldsets.append(fieldset)
            return non_admin_fieldsets
        else:
            return fieldsets

    # Removes publish and unpublish for regular journalists
    def get_actions(self, request):
        actions = super(BaseAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'publish' in actions:
                del actions['publish']
            if 'unpublish' in actions:
                del actions['unpublish']
        return actions

    # Code to change username to user_profile's full name in admin
    # from http://djangosnippets.org/snippets/1642/
    always_show_username = True

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(BaseAdmin, self).formfield_for_foreignkey(
                                                db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(BaseAdmin, self).formfield_for_manytomany(
                                                db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def get_user_label(self, user):
        name = user.get_profile().__unicode__()
        username = user.username
        if not self.always_show_username:
            return name or username
        return (name and name != username and '%s (%s)' % (name, username)
                or username)

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
