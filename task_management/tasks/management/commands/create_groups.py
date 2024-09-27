from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create Project Manager group'

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name='Project Manager')
        self.stdout.write(self.style.SUCCESS('Project Manager group created successfully'))
