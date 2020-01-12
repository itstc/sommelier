from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .models import Wine

# Create your views here.
@api_view(["GET"])
def wines(request):

    data = {
        "wines": [
            'best wine',
            "okay wine",
            'bad wine',
        ]
    }

    return JsonResponse(data)
    
@api_view(["GET"])
def notes(request):

    notes = {
        "earthy": 2,
        "fruity": 3,
        "floral": 1
    }

    data = {
            "notes": notes,        
    }

    return JsonResponse(data)

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


