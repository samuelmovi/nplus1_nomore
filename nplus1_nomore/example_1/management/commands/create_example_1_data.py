import logging
import random
from decimal import Decimal
from dateutil import tz

from django.core.management.base import BaseCommand

from faker import Faker

from example_1.models import Reports, Expenses

logger = logging.getLogger('django')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('instance_amount', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        instance_amount = kwargs['instance_amount'][0]

        if not instance_amount:
            instance_amount = random.randint(5, 10)
        
        logger.info(f'[#] Creating {instance_amount} instances of Report')
        fake = Faker()

        reports = []
        for i in range(1, instance_amount):
            data = {
                'name': fake.company(),
                'submitted_date': fake.date_time()
            }
            reports.append(Reports.objects.create(**data))
            logger.debug(f'Created Report {i}/{instance_amount}: {reports[-1]}')
        
        logger.info('[#] All instances of Report created')
        logger.info('[#] Creating instances of Expenses for each report')

        for instance in reports:
            logger.info(f'[#] Creating expenses for {instance}')
            all_expenses = [ Expenses(report=instance,amount=Decimal(random.randint(100, 100000)/100)) for x in range(instance_amount) ]
            # create instances
            Expenses.objects.bulk_create(all_expenses)
        
        logger.info('[#] All models instances created')
