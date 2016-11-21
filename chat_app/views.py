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


def send_message(request, room_pk):
    response = {}

    content = request.GET.get('content', None)
    user = request.GET.get('user', None)

    if content is not None and user is not None:
        try:
            room = Room.objects.get(pk=room_pk)
            room.send_message(user, content)
            response['status'] = "OK"

        except Room.DoesNotExist:
            response['status'] = "ERROR"

    else:
        response['status'] = "ERROR"

    response_json = json.dumps(response)
    return HttpResponse(response_json, content_type='application/json')


def view_messages(request, room_pk):
    response = {}

    try:
        room = Room.objects.get(pk=room_pk)
        messages = room.messages.all().order_by('-pk')[:10].reverse()
        response['messages'] = []

        for message in messages:
            new_message = {}
            new_message['user'] = message.user
            new_message['date'] = str(message.date)
            new_message['content'] = message.content

            response['messages'].append(new_message)

        response['status'] = "OK"

    except Room.DoesNotExist:
        response['status'] = "ERROR"

    response_json = json.dumps(response)
    return HttpResponse(response_json, content_type='application/json')
