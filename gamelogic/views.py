from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
Monster = apps.get_model('backend_main', 'Monster')
Player = apps.get_model('backend_main', 'Player')
Weapon = apps.get_model('backend_main', 'Weapon')


def map_build(request):
    print('inside map')
    outer_box = []
    for _ in range(9):
        inner_box = []
        for _ in range(9):
            inner_box.append(0)
        outer_box.append(inner_box)
    outer_box[3][0] = 0 # wall
    outer_box[3][0] = 1 # empty space
    outer_box[3][1] = 2 # player
    outer_box[3][2] = 3 # monster
    outer_box_b = [
        [0,0,0,0,0,0,2,0,0],
        [0,1,1,1,1,1,1,4,0],
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
    response['prompt'] = 'Moved Up'
    
    if current_map[player_location[0] - 1][player_location[1]] == 1:
        print('proceed')
        current_map[player_location[0] - 1][player_location[1]] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response
    elif current_map[player_location[0] - 1][player_location[1]] == 0:
        print('cannot walk this way')
        response['map'] = current_map
        return response
    elif current_map[player_location[0] - 1][player_location[1]] == 3:
        print('monster encounter')
        encounter_success = monster_encounter_initial(response)
        if encounter_success:
            current_map[player_location[0] -1][player_location[1]] = 2
            current_map[player_location[0]][player_location[1]] = 1
            response['map'] = current_map
            return response
    elif current_map[player_location[0] - 1][player_location[1]] == 4:
        response['prompt'] = 'YOU HAVE FOUND A WEAPON'
        response['player']['inventory'] = pick_up(response)
        response['map'] = current_map
        return response
    response['map'] = current_map
    return response
    
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
    response['prompt'] = 'Moved Down'
    
    if current_map[player_location[0] + 1][player_location[1]] == 1:
        print('proceed')
        current_map[player_location[0] +1][player_location[1]] = 2
        current_map[player_location[0]][player_location[1]] = 1
        print(response['prompt'])
        response['map'] = current_map
        return response
    elif current_map[player_location[0] +1][player_location[1]] == 0:
        print('cannot walk this way')
        response['map'] = current_map
        return response
    elif current_map[player_location[0] + 1][player_location[1]] == 3:
        print('monster encounter')
        encounter_success = monster_encounter_initial(response)
        if encounter_success:
            current_map[player_location[0] +1][player_location[1]] = 2
            current_map[player_location[0]][player_location[1]] = 1
            response['map'] = current_map
            return response
        print('monster encounter complete')
        response['map'] = current_map
        return response
    elif current_map[player_location[0] + 1][player_location[1]] == 4:
        response['prompt'] = 'YOU HAVE FOUND A WEAPON'
        response['player']['inventory'] = pick_up(response)
        response['map'] = current_map
        return response
    response['map'] = current_map
    return response

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

    response['prompt'] = 'Moved Left'

    if current_map[player_location[0]][player_location[1]-1] == 1:
        print('proceed')
        current_map[player_location[0]][player_location[1]-1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response
    elif current_map[player_location[0]][player_location[1]-1] == 0:
        print('cannot walk this way')
        response['map'] = current_map
        return response
    elif current_map[player_location[0]][player_location[1]-1] == 3:
        print('monster encounter')
        encounter_success = monster_encounter_initial(response)
        if encounter_success:
            current_map[player_location[0]][player_location[1]-1] = 2
            current_map[player_location[0]][player_location[1]] = 1
            response['map'] = current_map
            return response
        print('monster encounter complete')
        response['map'] = current_map
        return response
    elif current_map[player_location[0]][player_location[1]-1] == 4:
        response['prompt'] = 'YOU HAVE FOUND A WEAPON'
        response['player']['inventory'] = pick_up(response)
        response['map'] = current_map
        return response

    response['map'] = current_map
    return response

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
    
    response['prompt'] = 'Moved Right'

    if current_map[player_location[0]][player_location[1]+1] == 1:
        print('proceed')
        current_map[player_location[0]][player_location[1]+1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response
    elif current_map[player_location[0]][player_location[1]+1] == 0:
        print('cannot walk this way')
        response['map'] = current_map
        return response
    elif current_map[player_location[0]][player_location[1]+1] == 3:
        print('monster encounter')
        encounter_success = monster_encounter_initial(response)
        if encounter_success:
            current_map[player_location[0]][player_location[1]+1] = 2
            current_map[player_location[0]][player_location[1]] = 1
            response['map'] = current_map
            return response
    elif current_map[player_location[0]][player_location[1]+1] == 4:
        response['prompt'] = 'YOU HAVE FOUND A WEAPON'
        # weapon = Weapon.objects.get()
        # response['player']['inventory'].append(weapon)
        # print(response['player']['inventory'])
        # pick_up(response)
        current_map[player_location[0]][player_location[1]+1] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response
    response['map'] = current_map
    return response

def player_movement(response):
    if response['message'] == 'move up':
        response = player_move_up(response)
        return response
    if response['message'] == 'move down':
        response = player_move_down (response)
        return response
    if response['message'] == 'move left':
        response = player_move_left (response)
        return response
    if response['message'] == 'move right':
        response = player_move_right (response)
        return response

# Monster Encounter

def player_attack(monster, player):
    # TODO add player weapon to player damage Ex.(player.damage + player.weapon.damage)
    monster_health = monster.health
    monster_health -= player['damage']
    monster.health = monster_health
    return monster

def monster_attack(response, monster):
    player_health = response['player']['health']
    player_health -= monster.damage
    response['player']['health'] = player_health
    return response

def monster_encounter_initial(response):
    response['prompt'] = 'MONSTER ENCOUNTERED! READY YOUR WEAPON!'
    response['player']['combat'] = True
    print(response)
    return response

# def run_true():
#     return True


def monster_encounter(response):
    print('monster encounter initial')
    monster = Monster.objects.get()
    print(monster)
    # current_player = Player.objects.get(name=response['player']['name'])
    current_player = response['player']
    player_health = current_player['health']

    # if response['message'] == 'run':
    #     response['player']['combat'] = False
    #     response['prompt'] = 'You ran away!!'
    #     # location function
    #     # set current map location to value 3
    #     # run_true()
    #     player_move_up(response)

    
    if response['message'] == 'attack':
        monster = player_attack(monster, current_player)
        monster.save()
    if monster.health > 0:
        print(monster.health)
        response = monster_attack(response, monster)
        player_health = response['player']['health']
    print('monster_encounter', monster.health, player_health)

    response['prompt'] = 'Attack round complete.'

    if player_health <= 0:
        print("player is dead")
        response['player']['combat'] = False
        response['prompt'] = "You are dead! GAME OVER!"
        return response
    if monster.health <= 0:
        response['player']['combat'] = False
        print('monster dead')
        return response
    return response
    

def player_use_item(request):
    pass


# World actions

def pick_up(response):
    weapon = Weapon.objects.get()
    print(weapon)
    # inventory = response['player']['inventory']
    # inventory.append(weapon)
    response['player']['inventory'] = [weapon]
    print('pickin up somethin')
    return response['player']['inventory']
    
    

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


def command_validator(message,combat=False):
    command_list = ['quit','move left','move right','move up', 'move down','attack',]
    attack_list = ['attack','use item']
    if message in command_list:
        if combat:
            if message in attack_list:
                return True
            return False
            
        return True
    
    return False


def run_game(response):
    if 'move' in response['message']:
        response = player_movement(response)
    if 'equip' in response['message']:    
        player_equip(response)
    if 'attack' in response['message']:
        if response['player']['combat'] == False:
            response['prompt'] = 'Swing and a miss nothing to hit.'
        return response
    
    if 'run':
        pass
    if 'quit' in response['message']:
        # response['quit'] = True
        response['prompt'] = 'Thank you for playing. Come back and see us.'
        response['player'] = ''
        return response
    return response
    
                
@csrf_exempt
def game_logic(request):
    response = json.loads(request.body)

    world_intro()

    valid = command_validator(response['message'],response['player']['combat'])

    if valid:
        if response['player']['combat']:
            print('attack phase')
    

            response = monster_encounter(response)
                
           
            return JsonResponse(response, safe="False")
        response = run_game(response)    
    else:
        response['prompt'] = 'Please use valid command!'
        return JsonResponse(response, safe="False")
    return JsonResponse(response, safe="False")