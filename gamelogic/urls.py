from django.urls import path
from .views import test_response, test_map

urlpatterns = [
    path('test_response/', test_response, name='test_response'),
    path('test_map/', test_map, name='test_map')
]
