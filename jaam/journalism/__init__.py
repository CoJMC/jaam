from django.contrib.auth.models import Group
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission, User

journalist_group, created = Group.objects.get_or_create(name='Journalists')
journalist_group.permissions.add(
    # jaam.act
    Permission.objects.get(codename='add_act'), Permission.objects.get(codename='change_act'), Permission.objects.get(codename='delete_act'),
    # jaam.blog
    Permission.objects.get(codename='add_blog'), Permission.objects.get(codename='change_blog'), Permission.objects.get(codename='delete_blog'),
    Permission.objects.get(codename='add_blogpost'), Permission.objects.get(codename='change_blogpost'), Permission.objects.get(codename='delete_blogpost'),
    # jaam.journalism
    Permission.objects.get(codename='add_tag'), Permission.objects.get(codename='change_tag'), Permission.objects.get(codename='delete_tag'),
    Permission.objects.get(codename='add_userprofile'), Permission.objects.get(codename='change_userprofile'), Permission.objects.get(codename='delete_userprofile'),
    Permission.objects.get(codename='add_journalist'), Permission.objects.get(codename='change_journalist'), Permission.objects.get(codename='delete_journalist'),
    # jaam.photos
    Permission.objects.get(codename='add_photo'), Permission.objects.get(codename='change_photo'), Permission.objects.get(codename='delete_photo'),
    Permission.objects.get(codename='add_photogallery'), Permission.objects.get(codename='change_photogallery'), Permission.objects.get(codename='delete_photogallery'),
    Permission.objects.get(codename='add_photogalleryitem'), Permission.objects.get(codename='change_photogalleryitem'), Permission.objects.get(codename='delete_photogalleryitem'),
    # jaam.projects
    Permission.objects.get(codename='add_project'), Permission.objects.get(codename='change_project'), Permission.objects.get(codename='delete_project'),
    Permission.objects.get(codename='add_projectlocation'), Permission.objects.get(codename='change_projectlocation'), Permission.objects.get(codename='delete_projectlocation'),
    # jaam.stories
    Permission.objects.get(codename='add_story'), Permission.objects.get(codename='change_story'), Permission.objects.get(codename='delete_story'),
    # jaa.videos
    Permission.objects.get(codename='add_video'), Permission.objects.get(codename='change_video'), Permission.objects.get(codename='delete_video'),
    Permission.objects.get(codename='add_videogallery'), Permission.objects.get(codename='change_videogallery'), Permission.objects.get(codename='delete_videogallery'),
    Permission.objects.get(codename='add_videogalleryitem'), Permission.objects.get(codename='change_videogalleryitem'), Permission.objects.get(codename='delete_videogalleryitem'),
    
    # comments
    Permission.objects.get(codename='add_comment'), Permission.objects.get(codename='change_comment'), Permission.objects.get(codename='delete_comment'),
    Permission.objects.get(codename='add_commentflag'), Permission.objects.get(codename='change_commentflag'), Permission.objects.get(codename='delete_commentflag'),
    Permission.objects.get(codename='can_moderate'),
    # doccloud
    Permission.objects.get(codename='add_document'), Permission.objects.get(codename='change_document'), Permission.objects.get(codename='delete_document'),
    Permission.objects.get(codename='add_documentcloudproperties'), Permission.objects.get(codename='change_documentcloudproperties'), Permission.objects.get(codename='delete_documentcloudproperties'),)


@receiver(m2m_changed, sender=User.groups.through)
def make_journalist_staff(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action=='post_add':
        if instance.groups.filter(name='Journalists').count() == 1:
            instance.is_staff = True
    if action=='post_clear':
        if instance.groups.filter(name='Journalists').count() == 0:
            instance.is_staff = False
    instance.save()

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class NewUserAdmin(UserAdmin):
    actions = ['promote_to_journalist', 'demote_from_journalist']
    
    def promote_to_journalist(self, request, queryset):
        for user in queryset.all():
            user.groups.add(journalist_group)
            user.is_staff = True
            user.save()
    
    def demote_from_journalist(self, request, queryset):
        for user in queryset.all():
            user.groups.remove(journalist_group)
            user.is_staff = False
            user.save()
    
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)