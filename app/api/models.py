from django.db import models

class Wine(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    points=models.IntegerField(blank=False, default=0)
    price=models.DecimalField(blank=False, default=0, max_digits=999, decimal_places=2)
