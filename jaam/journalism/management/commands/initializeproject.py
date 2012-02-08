from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class Command(BaseCommand):
    help = 'Creates Journalist group and assigns default permissions'

    def handle(self, *args, **options):
    
        journalist_group, created = Group.objects.get_or_create(name='Journalists')
        if created:
            journalist_group.permissions.add(
                # jaam.act
                Permission.objects.get(codename='add_act'), Permission.objects.get(codename='change_act'), Permission.objects.get(codename='delete_act'),
                # jaam.blog
                Permission.objects.get(codename='add_blog'), Permission.objects.get(codename='change_blog'), Permission.objects.get(codename='delete_blog'),
                Permission.objects.get(codename='add_blogpost'), Permission.objects.get(codename='change_blogpost'), Permission.objects.get(codename='delete_blogpost'),
                # jaam.journalism
                Permission.objects.get(codename='add_tag'), Permission.objects.get(codename='change_tag'), Permission.objects.get(codename='delete_tag'),
                Permission.objects.get(codename='add_userprofile'), Permission.objects.get(codename='change_userprofile'), Permission.objects.get(codename='delete_userprofile'),
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
                Permission.objects.get(codename='add_documentcloudproperties'), Permission.objects.get(codename='change_documentcloudproperties'), Permission.objects.get(codename='delete_documentcloudproperties'),
            )