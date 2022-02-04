from django.urls import path
from .views import map_build, game_logic

urlpatterns = [
    # path('test_response/', test_response, name='test_response'),
    path('test_map/', map_build, name='test_map'),
    path('test_game_logic/', game_logic, name='test_game_logic'),
]
