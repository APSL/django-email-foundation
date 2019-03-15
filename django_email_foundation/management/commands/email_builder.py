from typing import List

from django.core.management import BaseCommand

from django_email_foundation.api import DjangoEmailFoundation


class Command(BaseCommand):
    help = 'Run a service for watch and compile the email templates'

    def handle(self, *args, **options):
        engine = DjangoEmailFoundation()
        errors = engine.perform_checks()
        if errors:
            self._show_errors(errors)
            return

        self.stdout.write(self.style.SUCCESS('Oh, yes! Punchi, punchi! Lets go!'))

        engine = DjangoEmailFoundation()
        engine.run_watch()

    def _show_errors(self, errors: List[str]):
        self.stdout.write(self.style.ERROR('Oops! Something went wrong...'))
        for error in errors:
            self.stdout.write(self.style.ERROR('  - {}'.format(error)))
        self.stdout.write('\n')
