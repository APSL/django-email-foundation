from django.core.management import BaseCommand

from django_email_foundation.api import DjangoEmailFoundation, Checks


class Command(BaseCommand):
    help = 'Create the necessary folders inside the template path and it add a basic layout.'

    def handle(self, *args, **options):
        checks = Checks()
        if not checks.templates_source_path():
            self.stdout.write(self.style.ERROR('You must to define the templates source path.'))
            return

        self.stdout.write('Creating folders...')
        engine = DjangoEmailFoundation()
        error = engine.create_basic_structure()

        if error:
            self.stderr.write(self.style.ERROR(error))
        else:
            self.stdout.write(self.style.SUCCESS('Done!'))
