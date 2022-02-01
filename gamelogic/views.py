from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
import json

def map_build(request):
    outer_box = []
    for _ in range(9):
        inner_box = []
        for _ in range(9):
            inner_box.append(0)
        outer_box.append(inner_box)
    outer_box[3][0] = 1
    outer_box[3][1] = 2
    outer_box[3][2] = 3
    response = {"Data": outer_box}
    return JsonResponse(response, safe="False")

def game_logic(request):
    response = json.loads(request.body)
    message = response['message']
    message_json = {"Data": message}
    print(message_json)
    return JsonResponse(message_json, safe="False")

