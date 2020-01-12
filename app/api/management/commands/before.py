from django.core.management.base import BaseCommand
from api.models import Wine
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('_winemag.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rowPoints = int(row['points'])
                if not row['price']: row['price'] = 999
                rowPrice = float(row['price'])
                p = Wine(name=row['title'], description=row['description'], price=rowPrice, points=rowPoints, ratio=rowPoints/rowPrice)
                p.save()
