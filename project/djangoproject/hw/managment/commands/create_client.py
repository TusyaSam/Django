from django.core.management.base import BaseCommand
from hw.models import Client


class Command(BaseCommand):
    help = "Create client."


    def handle(self, *args, **kwargs):
        user = Client(name='John', email='john@example.com', password='secret', age=25)
        user.save()
        self.stdout.write(f'{user}')
