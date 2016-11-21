from django.shortcuts import render
from django.http import  HttpResponse
import json

from .models import *

# Create your views here.

def room_list(request):
    rooms = Room.objects.all()
    room_list = []

    for room in rooms:
        room_list.append(room.name)

    rooms_json = json.dumps(room_list)
    return HttpResponse(rooms_json, content_type='application/json')
