from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand, call_command

from website.models import Project


class Command(BaseCommand):
    help = 'Restore the initial project records only when the database is empty.'

    def handle(self, *args, **options):
        before = Project.objects.count()
        database_name = settings.DATABASES['default']['NAME']
        self.stdout.write(f'RESTORE_PROJECTS database: {database_name}')
        self.stdout.write(f'RESTORE_PROJECTS before: {before}')

        if before == 0:
            fixture = Path('website/fixtures/projects.json')
            call_command('loaddata', str(fixture), verbosity=1)

        after = Project.objects.count()
        self.stdout.write(f'RESTORE_PROJECTS created: {after - before}')
        self.stdout.write(f'RESTORE_PROJECTS after: {after}')
        self.stdout.write(
            'RESTORE_PROJECTS titles: '
            + ', '.join(Project.objects.values_list('title', flat=True))
        )