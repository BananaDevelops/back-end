from django.test import TestCase
from django.http import JsonResponse
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