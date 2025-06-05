from django.apps import AppConfig
from django.db.models.signals import post_migrate

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # change if your app name is different

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_migrate

        def create_groups(sender, **kwargs):
            groups = ['RegisteredUser', 'Admin']
            for group in groups:
                Group.objects.get_or_create(name=group)

        post_migrate.connect(create_groups, sender=self)
