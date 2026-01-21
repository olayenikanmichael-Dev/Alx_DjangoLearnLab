from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Create default groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Get the Article model
        Article = apps.get_model('users', 'Article')

        # Create groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Get permissions
        can_view = Permission.objects.get(codename='can_view', content_type__app_label='users')
        can_create = Permission.objects.get(codename='can_create', content_type__app_label='users')
        can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='users')
        can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='users')

        # Assign permissions
        editors.permissions.set([can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS('Groups and permissions successfully created'))
