from http.client import ResponseNotReady
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

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
    outer_box_b = [
        [0,0,0,0,0,0,2,0,0],
        [0,1,1,1,1,1,1,1,0],
        [0,1,1,1,0,0,1,1,0],
        [0,1,1,1,0,0,3,1,0],
        [0,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,1,1,0],
        [0,1,3,1,1,0,1,1,0],
        [0,1,1,1,1,0,1,1,0],
        [0,0,1,0,0,0,0,0,0],]
    response = {"Data": outer_box_b}
    return JsonResponse(response, safe="False")



# Player Movement

# TODO reset out of bounds Index Error to cannot walk there for all movements

def player_move_up(current_map):
    player_location = []
    iteration = -1
    for idx in current_map:
        iteration = iteration + 1
        for sub_idx in idx:
            
            if sub_idx == 2:
                player_location.append(iteration)
                player_location.append(idx.index(2))
    
    if current_map[player_location[0] -1][player_location[1]] == 1:
        print('proceed')
        current_map[player_location[0] -1][player_location[1]] = 2
        current_map[player_location[0]][player_location[1]] = 1
        return current_map
    elif current_map[player_location[0] -1][player_location[1]] == 0:
        print('cannot walk this way')
        return current_map
    elif current_map[player_location[0] -1][player_location[1]] == 3:
        print('monster encounter')
        current_map[player_location[0] -1][player_location[1]] = 2
        current_map[player_location[0]][player_location[1]] = 1
        monster_encounter()
        return current_map
    return current_map
    

def player_move_down(current_map):
    player_location = []
    iteration = -1
    for idx in current_map:
        iteration = iteration + 1
        for sub_idx in idx:
            
            if sub_idx == 2:
                player_location.append(iteration)
                player_location.append(idx.index(2))
            
    if current_map[player_location[0] + 1][player_location[1]] == 1:
        print('proceed')
        current_map[player_location[0] +1][player_location[1]] = 2
        current_map[player_location[0]][player_location[1]] = 1
        return current_map
    elif current_map[player_location[0] -1][player_location[1]] == 0:
        print('cannot walk this way')
        return current_map
    elif current_map[player_location[0] + 1][player_location[1]] == 3:
        print('monster encounter')
        current_map[player_location[0] -1][player_location[1]] = 2
        current_map[player_location[0]][player_location[1]] = 1
        monster_encounter()
        return current_map
    return current_map

def player_move_left(current_map):
    player_location = []
    iteration = -1
    for idx in current_map:
        iteration = iteration + 1
        for sub_idx in idx:
            
            if sub_idx == 2:
                player_location.append(iteration)
                player_location.append(idx.index(2))
            
    if current_map[player_location[0]][player_location[1]-1] == 1:
        print('proceed')
        current_map[player_location[0]][player_location[1]-1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        return current_map
    elif current_map[player_location[0]][player_location[1]-1] == 0:
        print('cannot walk this way')
        return current_map
    elif current_map[player_location[0]][player_location[1]-1] == 3:
        print('monster encounter')
        current_map[player_location[0]][player_location[1]-1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        monster_encounter()
        return current_map
    return current_map

def player_move_right(current_map):
    player_location = []
    iteration = -1
    for idx in current_map:
        iteration = iteration + 1
        for sub_idx in idx:
            
            if sub_idx == 2:
                player_location.append(iteration)
                player_location.append(idx.index(2))
    
    if current_map[player_location[0]][player_location[1]+1] == 1:
        print('proceed')
        current_map[player_location[0]][player_location[1]+1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        return current_map
    elif current_map[player_location[0]][player_location[1]+1] == 0:
        print('cannot walk this way')
        return current_map
    elif current_map[player_location[0]][player_location[1]+1] == 3:
        print('monster encounter')
        current_map[player_location[0]][player_location[1]+1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        monster_encounter()
        return current_map
    return current_map

def player_movement(response):
    
    # response = json.loads(request.body)
    # command = response['message']
    # command.lower()
    if response['message'] == 'move up':
        return player_move_up(response['map'])
        
    elif response['message'] == 'move down':
        return player_move_down(response['map'])
    elif response['message'] == 'move left':
        return player_move_left(response['map'])
    elif response['message'] == 'move right':
        return player_move_right(response['map'])


# Monster Encounter

def player_attack(request):
    pass

def monster_attack(reqeust):
    pass

def monster_encounter():
    pass

def player_use_item(request):
    pass


# World actions

def player_use_item(request):
    pass


def player_equip():
    pass

def player_equip_weapon(request):
    pass

def player_equip_item(request):
    pass


def world_intro():
    return 'this is how you play the game'


def command_validator(message):
    command_list = ['quit','move left','move right','move up', 'move down']
    if message in command_list:
        return True
    return False


def run_game(response):
    if 'move' in response['message']:
        response['map'] = player_movement(response)
    if 'equip' in response['message']:    
        player_equip(response)
    return response
    
                
@csrf_exempt
def game_logic(request):
    response = json.loads(request.body)

    world_intro()

    valid = command_validator(response['message'])
    
    if valid:
        response = run_game(response)    
    else:
        return JsonResponse('please use valid command!!!!', safe="False")
    return JsonResponse(response, safe="False")