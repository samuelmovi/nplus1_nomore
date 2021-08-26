import logging
import random
from decimal import Decimal
from dateutil import tz

from django.core.management.base import BaseCommand

from faker import Faker

from example_3.models import Reports, Expenses

logger = logging.getLogger('django')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('instance_amount', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        instance_amount = kwargs['instance_amount'][0]
        
        logger.info(f'[#] Creating {instance_amount} instances of Report')
        fake = Faker()

        reports = []
        for i in range(1, instance_amount):
            reports.append(Reports.objects.create(name=fake.company()))
            logger.debug(f'Created Report {i}/{instance_amount}: {reports[-1]}')
        
        logger.info('[#] All instances of Report created')
        logger.info('[#] Creating instances of Expenses for each report')

        for instance in reports:
            logger.info(f'[#] Creating expenses for {instance}')
            # create instances
            # TODO: improve, this is really slow
            all_expenses = [ Expenses(amount=Decimal(random.randint(100, 100000)/100)) for x in range(instance_amount) ]
            for expense in all_expenses:
                expense.save()
            # add to expense instance
            instance.expenses.set(all_expenses)
            instance.save()
        
        logger.info('[#] All models instances created')
