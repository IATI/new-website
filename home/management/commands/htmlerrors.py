from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.test import Client

from wagtail.core.models import Page


class Command(BaseCommand):
    """Management command that identifies pages with malformed content."""

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('pks', nargs='+', type=int)

    def handle(self, **options):
        """Handle the htmlerrors command."""
        invalid_page_ids = []
        invalid_page_errors = []
        pages = Page.objects.all()
        client = Client()
        # use any existing super user account
        user = User.objects.get(username='russell')
        client.force_login(user)

        for page in pages:
            id = page.id
            if int(id) in options['pks']:
                # print statement to assure the script is running
                print(id)
                url = f'/cms/pages/{id}/edit/'
                try:
                    response = client.get(url)
                except Exception as e:
                    invalid_page_ids.append(id)
                    invalid_page_errors.append({'id': id, 'error': e})

        print(invalid_page_ids)
        print(invalid_page_errors)
