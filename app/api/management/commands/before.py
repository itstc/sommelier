from django.core.management.base import BaseCommand
from api.models import Wine

class Command(BaseCommand):
    def handle(self, *args, **options):
        wines = [
            Wine(name="red", description="a red wine", points=70, price=420.99),
            Wine(name="white", description="a white wine", points=60, price=100.99),
            Wine(name="pink", description="a pink wine", points=50, price=200.99),
        ] 

        for wine in wines:
            wine.save()
