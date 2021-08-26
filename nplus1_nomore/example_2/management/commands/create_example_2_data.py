import logging
import random
from dateutil import tz

from django.core.management.base import BaseCommand

from faker import Faker

from example_2.models import Country, Author, Book

logger = logging.getLogger('django')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('instance_amount', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        # instantiate faker
        fake = Faker()

        instance_amount = kwargs['instance_amount'][0]

        if not instance_amount:
            instance_amount = random.randint(5, 10)

        logger.info('[#] Creating countries')

        countries = [ Country(name='Spain'), Country(name='UK'), Country(name='USA')]
        # save instances
        for x in countries:
            x.save()
        
        logger.info(f'[#] Creating {instance_amount} instances of Author')
        
        authors = []
        for i in range(1, instance_amount):
            data = {
                'name': fake.name(),
                'country': countries[random.randint(0,2)]
            }
            authors.append(Author.objects.create(**data))
            logger.debug(f'Created Author {i}/{instance_amount}: {authors[-1]}')
        
        logger.info('[#] All instances of Report created')
        logger.info('[#] Creating instances of Expenses for each report')

        for instance in authors:
            logger.info(f'[#] Creating Books for {instance}')
            all_expenses = [ Book(author=instance,title=fake.bs()) for x in range(instance_amount) ]
            # create instances
            Book.objects.bulk_create(all_expenses)
        
        logger.info('[#] All models instances created')
