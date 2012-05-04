from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.contrib import admin

class Command(BaseCommand):
    help = 'Helps debug profile issues'

    def handle(self, *args, **options):
        users = User.objects.all()
        for u in users:
            try:
                user.get_profile()
            except:
                print u
                print u.username