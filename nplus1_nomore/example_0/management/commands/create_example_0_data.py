import logging
import random
from decimal import Decimal
from dateutil import tz

from django.core.management.base import BaseCommand

from faker import Faker

from example_0.models import Country, Person

logger = logging.getLogger('django')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('instance_amount', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        instance_amount = kwargs['instance_amount'][0]
        
        logger.info(f'[#] Creating {instance_amount} instances of Person and Country')
        fake = Faker()

        for i in range(1, instance_amount):
            # create country
            country = Country.objects.create(name=fake.bank_country())

            # create person
            person = Person.objects.create(
                name=fake.name(),
                country=country
            )
        
        logger.info('[#] All models instances created')
