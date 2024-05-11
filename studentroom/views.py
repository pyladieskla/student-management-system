from django.shortcuts import render
from django.http import HttpResponse


def get_room(request, room_id):
    return HttpResponse("You are at room: " + str(room_id))
