import logging

from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line
# File path for GIS dataset


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        logging.info('[#] Starting Django server with "nplusone" enabled')
        settings = '--settings=nplus1_nomore.settings.nplusone'

        execute_from_command_line(['python', 'manage.py', settings])

