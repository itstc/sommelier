from rest_framework import serializers
from . import models

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wine
        fields = ["name", "description", "points", "price"]
