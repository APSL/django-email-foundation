from django.core.management import BaseCommand

from django_email_foundation.api import DjangoEmailFoundation


class Command(BaseCommand):
    help = 'Install the node required packages.'

    def handle(self, *args, **options):
        engine = DjangoEmailFoundation()
        success = engine.install_required_packages
        if not success:
            self.stdout.write(self.style.ERROR(
                'Oops! Something went wrong... :('))
