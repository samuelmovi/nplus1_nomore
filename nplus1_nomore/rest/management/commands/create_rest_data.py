import logging
import random

from django.core.management.base import BaseCommand

from faker import Faker

from rest.models import GrandParent,Parent, Child

logger = logging.getLogger('django')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('instance_amount', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        instance_amount = kwargs['instance_amount'][0]
        # instantiate faker
        fake = Faker()

        logger.info('[#] Creating Grandparents')

        grandparents = [ GrandParent.objects.create(name=fake.name()) for x in range(int(instance_amount/4))]

        logger.info(f'[#] Creating instances of Parent')

        parents = [ 
            Parent.objects.create(
                name=fake.name(), 
                parent=grandparents[random.randint(0,len(grandparents))]
                ) for x in range(int(instance_amount/2))
            ]

        logger.info(f'[#] Creating instances of Child')

        for x in range(instance_amount):
            p = parents[random.randint(0,2)]
            Child.objects.create(
                name=fake.name(), 
                parent=p, 
                grandparent=p.parent
                )
        
        logger.info('[#] All models instances created')
