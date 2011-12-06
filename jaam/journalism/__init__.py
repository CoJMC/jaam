from django.contrib.auth.models import Group
from django.db.models.signals import m2m_changed, post_syncdb
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import pdb

@receiver(m2m_changed, sender=User.groups.through)
def make_journalist_staff(sender, instance, action, reverse, model, pk_set, **kwargs):
    print action
    journalist_group_pk = Group.objects.get(name='Journalists').pk
    if action=='pre_add':
        if instance.groups.filter(name='Journalists').count() == 0:
            if journalist_group_pk in pk_set:
                instance.is_staff = True
# this code is close to being right
# pending this upstream django bug:
# https://code.djangoproject.com/ticket/16073
#
#    if action=='pre_remove':
#        pdb.set_trace()
#        if instance.groups.filter(name='Journalists').count() == 1:
#            if pk_set is not None and journalist_group_pk not in pk_set:
#                instance.is_staff = False
    instance.save()

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

@receiver(post_syncdb)
def add_actions_to_user_admin(**kwargs):
    admin.site.unregister(User)
    admin.site.register(User, NewUserAdmin)