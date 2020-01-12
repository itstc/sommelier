from django.core.management.base import BaseCommand
from api.models import Wine
from ._data import wines

class Command(BaseCommand):
    def handle(self, *args, **options):
        for wd in wines*5:
            w = Wine(name=wd[0], description=wd[1], points=wd[2], price=wd[3])
            w.save()
