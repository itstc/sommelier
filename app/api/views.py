from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .models import Wine
from .serializers import WineSerializer

# Create your views here.
@api_view(["GET"])
def wines(request):
    wineList = Wine.objects.all()
    serializer = WineSerializer(wineList, many=True)
    return JsonResponse(serializer.data, safe=False)
    

