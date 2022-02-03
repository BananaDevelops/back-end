import imp
from urllib import response
from django.test import TestCase
from django.http import JsonResponse
from .views import run_game
import json

# Create your tests here.
def test_map(request):
    response = []
    for i in range(9):
        inner_box = []
        for _ in range(9):
            inner_box.append('o')
        response.append(inner_box)
    response_b = {"Data": response}
    return JsonResponse(response_b, safe="False")

def test_response(request):
    response = json.loads(request.body)
    print(request.body)
    print(response)
    response_text = response['text'].upper()
    response_b = {"response":response_text}

    return JsonResponse(response_b,safe="False")

def test_move_down(TestCase):
    response_object = {
    "player":{"id": 167,"name": "polo","health": 100,"damage": 1,"inventory": [],"left_hand": {},"right_hand": {},"combat": False,"end_game": False},
"map":"[[0,0,0,0,0,0,2,0,0],[0,1,1,1,1,1,1,4,0],[0,1,1,1,0,0,1,1,0],[0,1,1,1,0,0,3,1,0],[0,1,1,1,1,1,1,1,0],[0,1,1,0,0,0,1,1,0],[0,1,3,1,1,0,1,1,0],[0,1,1,1,1,0,1,1,0],[0,0,1,0,0,0,0,0,0],]",
"message":"move down",
"prompt":""
}
    actual = run_game(response_object)
    expected = {
    "player":{"id": 167,"name": "polo","health": 100,"damage": 1,"inventory": [],"left_hand": {},"right_hand": {},"combat": False,"end_game": False},
"map":"[[0,0,0,0,0,0,1,0,0],[0,1,1,1,1,1,2,4,0],[0,1,1,1,0,0,1,1,0],[0,1,1,1,0,0,3,1,0],[0,1,1,1,1,1,1,1,0],[0,1,1,0,0,0,1,1,0],[0,1,3,1,1,0,1,1,0],[0,1,1,1,1,0,1,1,0],[0,0,1,0,0,0,0,0,0],]",
"message":"move down","prompt":"Moved Down"
}
    assert actual == expected
