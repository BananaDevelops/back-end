# from gamelogic.views import run_game
from gamelogic.move_player import player_move, player_location_finder, player_movement
import pytest

def test_is_player_move():
  assert player_move

def test_is_player_finder():
  assert player_location_finder

def test_is_player_movement():
  assert player_movement

@pytest.mark.skip()
def test_is_run_game():
  assert run_game

def test_player_finder():
  map_array = [[0,0,2],[1,1,0]]
  actual = player_location_finder(map_array)
  expected = [0,2]
  assert actual == expected

def test_player_move_down():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":''}
  direction = "down"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'Moved down'}
  assert actual == expected

def test_player_move_up():
  response_object = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":''}
  direction = "up"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'Moved up'}
  assert actual == expected

def test_player_move_left():
  response_object = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":''}
  direction = "left"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,1,0,0],[1,1,2,1,1,1]], "prompt":'Moved left'}
  assert actual == expected

def test_player_move_right():
  response_object = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":''}
  direction = "right"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,1,2,1]], "prompt":'Moved right'}
  assert actual == expected

def test_player_move_right_cant():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":''}
  direction = "right"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'cannot walk this way'}
  assert actual == expected

def test_player_move_down_item():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,4,1,1]], "prompt":'', 'player':{"inventory":[]}}
  direction = "down"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'YOU HAVE FOUND A WEAPON', 'player':{"inventory":[{"type":"sword", "damage":10}]}}
  assert actual == expected

def test_player_move_down_monster():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,3,1,1]], "prompt":'', "player":{"combat":False}}
  direction = "down"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'MONSTER ENCOUNTERED! READY YOUR WEAPON!', "player":{"combat":True}}
  assert actual == expected

def test_player_movement_down():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'', "message":"move down"}
  actual = player_movement(response_object)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'Moved down', "message":"move down"}
  assert actual == expected

def test_player_movement_up():
  response_object = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'', "message": "move up"}
  actual = player_movement(response_object)
  expected = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'Moved up', "message": "move up"}
  assert actual == expected

def test_player_movement_left():
  response_object = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'', "message": "move left"}
  actual = player_movement(response_object)
  expected = {"map":[[0,0,0,1,0,0],[1,1,2,1,1,1]], "prompt":'Moved left', "message": "move left"}
  assert actual == expected

def test_player_movement_right():
  response_object = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'', "message": "move right"}
  actual = player_movement(response_object)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,1,2,1]], "prompt":'Moved right', "message": "move right"}
  assert actual == expected

def test_player_movement_right_cant():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'', "message": "move right" }
  direction = "right"
  actual = player_move(response_object,direction)
  expected = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'cannot walk this way', "message": "move right"}
  assert actual == expected

@pytest.mark.skip()
def test_run_game_move_down():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'', "message":"move down"}
  actual = run_game(response_object)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'Moved down', "message":"move down"}
  assert actual == expected

@pytest.mark.skip()
def test_run_game_down_monster():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,3,1,1]], "prompt":'', "player":{"combat":False}, "message":"move down"}
  actual = run_game(response_object)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'MONSTER ENCOUNTERED! READY YOUR WEAPON!', "player":{"combat":True}, "message":"move down"}
  assert actual == expected

@pytest.mark.skip()
def test_run_game_down_item():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,4,1,1]], "prompt":'', 'player':{"inventory":[]}, "message":"move down"}
  actual = run_game(response_object)
  expected = {"map":[[0,0,0,1,0,0],[1,1,1,2,1,1]], "prompt":'YOU HAVE FOUND A WEAPON', 'player':{"inventory":[{"type":"sword", "damage":10}]}, "message":"move down"}
  assert actual == expected

@pytest.mark.skip()
def test_run_game_attack_no_combat():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'', "message":"attack", "player":{"combat":False},}
  actual = run_game(response_object)
  expected = {"map":[[0,0,0,2,0,0],[1,1,1,1,1,1]], "prompt":'Swing and a miss nothing to hit.', "message":"attack", "player":{"combat":False},}
  assert actual == expected

@pytest.mark.skip()
def test_run_game_equip_item():
  response_object = {"map":[[0,0,0,2,0,0],[1,1,1,4,1,1]], "prompt":'', 'player':{"inventory":[{"type":"sword", "damage":10}], "left_hand":{}}, "message":"equip weapon sword left"}
  actual = run_game(response_object)
  expected = {"map":[[0,0,0,2,0,0],[1,1,1,4,1,1]], "prompt":'You equipped a sword', 'player':{"inventory":[], "left_hand":{"type":"sword", "damage":10}}, "message":"equip weapon sword left"}
  assert actual == expected