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
    response = {"Data": outer_box}
    return JsonResponse(response, safe="False")



# Player Movement

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

def player_movement(message,current_map):
    
    # response = json.loads(request.body)
    # command = response['message']
    # command.lower()
    if message == 'move up':
        return player_move_up(current_map)
    elif message == 'move down':
        return player_move_down(current_map)
    elif message == 'move left':
        return player_move_left(current_map)
    elif message == 'move right':
        return player_move_right(current_map)


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


def run_game(message):
    world_intro()
    new_game = True
    
    while new_game:
        if 'move' in message:
            return player_movement(message)
        if 'equip' in message:    
            player_equip(message)
        if 'quit' in message:
            break
        
@csrf_exempt
def game_logic(request):
    response = json.loads(request.body)
    message = response['message']
    valid = command_validator(message)
    if valid:
        run_game(message)    
    else:
        return JsonResponse('please use valid command!!!!', safe="False")
    return JsonResponse(message, safe="False")