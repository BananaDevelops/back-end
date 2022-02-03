def monster_encounter_initial(response):
    response['prompt'] = 'MONSTER ENCOUNTERED! READY YOUR WEAPON!'
    response['player']['combat'] = True
    print(response)
    return response

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


def pick_up(inventory):
    # THIS IS COMMENTED OUT FOR TESTING
    # weapon = Weapon.objects.get()
    weapon = {"type":"sword", "damage":10}
    print(weapon)
    inventory.append(weapon)
    # response['player']['inventory'] = [weapon]
    # print('pickin up somethin')
    return inventory