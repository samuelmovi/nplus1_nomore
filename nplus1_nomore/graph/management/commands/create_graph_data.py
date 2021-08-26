import logging
import random
from decimal import Decimal
from dateutil import tz

from django.core.management.base import BaseCommand

from faker import Faker

from graph.models import Article, Comment

logger = logging.getLogger('django')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('instance_amount', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        instance_amount = kwargs['instance_amount'][0]
        
        logger.info(f'[#] Creating {instance_amount} instances of Article')
        fake = Faker()

        for i in range(1, instance_amount):
            # create country
            article = Article.objects.create(
                title=fake.bs(),
                body=fake.paragraph()
                )

            # create person
            for x in range(1, instance_amount):
                Comment.objects.create(
                    article=article,
                    text=fake.paragraph()
                )
        
        logger.info('[#] All models instances created')
