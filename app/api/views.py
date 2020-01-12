from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .models import Wine
from .serializers import WineSerializer
from .constants import PAGE_SIZE

# Create your views here.
@api_view(["GET"])
def wines(request):
    pageParam = int(request.GET.get('page', '0'))
    wineList = Wine.objects.order_by('-points')[pageParam * PAGE_SIZE:pageParam * PAGE_SIZE + PAGE_SIZE]
    serializer = WineSerializer(wineList, many=True)
    return JsonResponse(serializer.data, safe=False)
    
@api_view(["GET"])
def notes(request):
    pageParam = int(request.GET.get('page', '0'))
    body = json.loads(request.body)
    wineList = Wine.objects.filter(description__contains=body.get('note', '')).order_by('-points')[pageParam * PAGE_SIZE:pageParam * PAGE_SIZE + PAGE_SIZE]
    serializer = WineSerializer(wineList, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def value(request):

    data = {
        "wines": [
            "okay wine",
            "best wine",
            "bad wine",
        ]
    }
    
    return JsonResponse(data)


