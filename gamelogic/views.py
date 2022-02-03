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

def player_location_finder(map):
    player_location = []
    for index,idx in enumerate(map):
        for index_b,sub_idx in enumerate(idx): 
            if sub_idx == 2:
                player_location.append(index)
                player_location.append(index_b)
    return player_location

def player_move(response, direction):
    current_map = response['map']
    player_location = player_location_finder(current_map)

    direction_addants = []
    if direction == "up":
        direction_addants.extend([-1,0])
    if direction == "down":
        direction_addants.extend([1,0])
    if direction == "left":
        direction_addants.extend([0,-1])
    if direction == "right":
        direction_addants.extend([0,1])

    future_y=player_location[0] + direction_addants[0]
    future_x=player_location[1] + direction_addants[1]
    future_position_value = current_map[future_y][future_x]


    # If the player moved into a wall
    if future_position_value == 0:
        response['prompt']='cannot walk this way'
        response['map'] = current_map
        return response

    # If the player moved toward an open space
    elif future_position_value == 1:
        response['prompt'] = f'Moved {direction}'
        current_map[future_y][future_x] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response

    # If the player moved into a monster
    elif future_position_value == 3:
        response['prompt'] = 'monster encounter'
        response = monster_encounter_initial(response)
        current_map[future_y][future_x] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response

    # If the player moved into an item space
    elif future_position_value == 4:
        response['prompt'] = 'YOU HAVE FOUND A WEAPON'
        response['player']['inventory'] = pick_up(response['player']['inventory'])
        current_map[future_y][future_x] = 2
        current_map[player_location[0]][player_location[1]] = 1
        response['map'] = current_map
        return response
    response['map'] = current_map
    return response

def player_movement(response):
    if response['message'] == 'move up':
        response = player_move(response, "up")
        return response

    if response['message'] == 'move down':
        response = player_move(response, "down")
        return response

    if response['message'] == 'move left':
        response = player_move(response, "left")
        return response

    if response['message'] == 'move right':
        response = player_move(response, "right")
        return response

# Monster Encounter

def player_attack(monster, player):
    # TODO add player weapon to player damage Ex.(player.damage + player.weapon.damage)
    monster_health = monster.health
    monster_health -= player['damage'] + player['left_hand']['damage']
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

    response['prompt'] = f'Attack round complete. Monster Health: {monster.health}'

    if player_health <= 0:
        print("player is dead")
        response['player']['combat'] = False
        response['prompt'] = "You are dead! GAME OVER!"
        return response
    if monster.health <= 0:
        response['player']['combat'] = False
        print('monster dead')
        response['prompt'] = "Monster is dead"
        return response
    return response

# World actions
    
def pick_up(inventory):
    # THIS IS COMMENTED OUT FOR TESTING
    # weapon = Weapon.objects.get()
    weapon = {"type":"sword", "damage":20}
    print(weapon)
    inventory.append(weapon)
    # response['player']['inventory'] = [weapon]
    # print('pickin up somethin')
    return inventory   

def player_equip(response):
    if "weapon" in response['message']:
        response = player_equip_weapon(response)
        return response
    if "item" in response['message']:
        response = "item"
        return response

def player_equip_weapon(response):
    if len(response['player']['inventory']) > 0:
        search_term = ''
        if "sword" in response['message']:
            search_term = 'sword'
        if "left" in response['message']:
            for index,weapon in enumerate(response['player']['inventory']):
                item_removed_inventory = []
                if weapon['type'] == search_term:
                    response['player']['left_hand']= weapon
                    response['prompt'] = f'You equipped a {search_term}'
                else:
                    item_removed_inventory.append(weapon)
                response['player']['inventory']= item_removed_inventory 
                return response
        if "right" in response['message']:
            return "No rightey"
    return "no weapon"

def world_intro():
    return 'this is how you play the game'

def command_validator(message,combat=False):
    command_list = ['quit','move left','move right','move up', 'move down','attack', 'equip weapon sword left']
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