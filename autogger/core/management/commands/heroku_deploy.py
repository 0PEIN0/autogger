from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):
    help = _('Perform heroku deployment operations.')

    def migrate_project_apps(self):
        try:
            call_command('makemigrations')
            call_command('migrate')
        except CommandError as ex:
            print('MIGRATION ERROR: {message}'.format(message=ex.message))

    def reset_data(self):
        call_command('flush', '--no-input')

    def handle(self, *args, **options):
        # self.reset_data()
        self.migrate_project_apps()
