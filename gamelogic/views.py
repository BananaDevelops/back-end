from os import name
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
Monster = apps.get_model('backend_main', 'Monster')
Player = apps.get_model('backend_main', 'Player')


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

def player_move_up(response):
    current_map = response['map']
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
        encounter_success = monster_encounter(response['player'])
        if encounter_success:
            current_map[player_location[0] -1][player_location[1]] = 2
            current_map[player_location[0]][player_location[1]] = 1
            return current_map
    return current_map
    

def player_move_down(response):
    current_map = response['map']
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
        encounter_success = monster_encounter(response['player'])
        if encounter_success:
            current_map[player_location[0] +1][player_location[1]] = 2
            current_map[player_location[0]][player_location[1]] = 1
            return current_map
        print('monster encounter complete')
        return current_map
    return current_map

def player_move_left(response):
    current_map = response['map']
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
        encounter_success = monster_encounter(response['player'])
        if encounter_success:
            current_map[player_location[0]][player_location[1]-1] = 2
            current_map[player_location[0]][player_location[1]] = 1
            return current_map
        print('monster encounter complete')
        return current_map
    return current_map

def player_move_right(response):
    current_map = response['map']
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
        encounter_success = monster_encounter(response['player'])
        if encounter_success:
            current_map[player_location[0]][player_location[1]+1] = 2
            current_map[player_location[0]][player_location[1]] = 1
            return current_map
    return current_map

def player_movement(response):
    
    # response = json.loads(request.body)
    # command = response['message']
    # command.lower()
    if response['message'] == 'move up':
        return player_move_up(response)
        
    elif response['message'] == 'move down':
        return player_move_down(response)
    elif response['message'] == 'move left':
        return player_move_left(response)
    elif response['message'] == 'move right':
        return player_move_right(response)


# Monster Encounter

def player_attack(monster_health, player):
    # TODO add player weapon to player damage Ex.(player.damage + player.weapon.damage)
    monster_health -= player.damage + 20
    return monster_health

def monster_attack(player_health, monster):
    player_health -= monster.damage
    return player_health

def monster_encounter(player):
    print('monster encounter initial')
    monster = Monster.objects.get()
    current_player = Player.objects.get(name=player['name'])

    monster_health = monster.health
    player_health = current_player.health

    while monster_health >0 and player_health >0:
        monster_health = player_attack(monster_health, current_player)
        player_health = monster_attack(player_health, monster)
        print('monster_encounter', monster_health, player_health)

    if player_health <= 0:
        print("player is dead")
        return False
    if monster_health <= 0:
        print('monster dead')
        return True
    

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
        response['message'] = 'please use valid command!!!!'
        return JsonResponse(response, safe="False")
    return JsonResponse(response, safe="False")