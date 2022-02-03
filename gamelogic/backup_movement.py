# # Player Movement

# # TODO reset out of bounds Index Error to cannot walk there for all movements

# def player_move_up(response):
#     current_map = response['map']
#     player_location = []
#     iteration = -1
#     for idx in current_map:
#         iteration = iteration + 1
#         for sub_idx in idx:
            
#             if sub_idx == 2:
#                 player_location.append(iteration)
#                 player_location.append(idx.index(2))
#     response['prompt'] = 'Moved Up'
    
#     if current_map[player_location[0] - 1][player_location[1]] == 1:
#         print('proceed')
#         current_map[player_location[0] - 1][player_location[1]] = 2
#         current_map[player_location[0]][player_location[1]] = 1
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0] - 1][player_location[1]] == 0:
#         print('cannot walk this way')
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0] - 1][player_location[1]] == 3:
#         print('monster encounter')
#         encounter_success = monster_encounter_initial(response)
#         if encounter_success:
#             current_map[player_location[0] -1][player_location[1]] = 2
#             current_map[player_location[0]][player_location[1]] = 1
#             response['map'] = current_map
#             return response
#     elif current_map[player_location[0] - 1][player_location[1]] == 4:
#         response['prompt'] = 'YOU HAVE FOUND A WEAPON'
#         response['player']['inventory'] = pick_up(response)
#         response['map'] = current_map
#         return response
#     response['map'] = current_map
#     return response
    
# def player_move_down(response):
#     current_map = response['map']
#     player_location = []
#     iteration = -1
#     for idx in current_map:
#         iteration = iteration + 1
#         for sub_idx in idx:
            
#             if sub_idx == 2:
#                 player_location.append(iteration)
#                 player_location.append(idx.index(2))
#     response['prompt'] = 'Moved Down'
    
#     if current_map[player_location[0] + 1][player_location[1]] == 1:
#         print('proceed')
#         current_map[player_location[0] +1][player_location[1]] = 2
#         current_map[player_location[0]][player_location[1]] = 1
#         print(response['prompt'])
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0] +1][player_location[1]] == 0:
#         print('cannot walk this way')
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0] + 1][player_location[1]] == 3:
#         print('monster encounter')
#         encounter_success = monster_encounter_initial(response)
#         if encounter_success:
#             current_map[player_location[0] +1][player_location[1]] = 2
#             current_map[player_location[0]][player_location[1]] = 1
#             response['map'] = current_map
#             return response
#         print('monster encounter complete')
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0] + 1][player_location[1]] == 4:
#         response['prompt'] = 'YOU HAVE FOUND A WEAPON'
#         response['player']['inventory'] = pick_up(response)
#         response['map'] = current_map
#         return response
#     response['map'] = current_map
#     return response

# def player_move_left(response):
#     current_map = response['map']
#     player_location = []
#     iteration = -1
#     for idx in current_map:
#         iteration = iteration + 1
#         for sub_idx in idx:
            
#             if sub_idx == 2:
#                 player_location.append(iteration)
#                 player_location.append(idx.index(2))

#     response['prompt'] = 'Moved Left'

#     if current_map[player_location[0]][player_location[1]-1] == 1:
#         print('proceed')
#         current_map[player_location[0]][player_location[1]-1] = 2
#         current_map[player_location[0]][player_location[1]] = 1
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0]][player_location[1]-1] == 0:
#         print('cannot walk this way')
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0]][player_location[1]-1] == 3:
#         print('monster encounter')
#         encounter_success = monster_encounter_initial(response)
#         if encounter_success:
#             current_map[player_location[0]][player_location[1]-1] = 2
#             current_map[player_location[0]][player_location[1]] = 1
#             response['map'] = current_map
#             return response
#         print('monster encounter complete')
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0]][player_location[1]-1] == 4:
#         response['prompt'] = 'YOU HAVE FOUND A WEAPON'
#         response['player']['inventory'] = pick_up(response)
#         response['map'] = current_map
#         return response

#     response['map'] = current_map
#     return response

# def player_move_right(response):
#     current_map = response['map']
#     player_location = []
#     iteration = -1
#     for idx in current_map:
#         iteration = iteration + 1
#         for sub_idx in idx:
            
#             if sub_idx == 2:
#                 player_location.append(iteration)
#                 player_location.append(idx.index(2))
    
#     response['prompt'] = 'Moved Right'

#     if current_map[player_location[0]][player_location[1]+1] == 1:
#         print('proceed')
#         current_map[player_location[0]][player_location[1]+1] = 2
#         current_map[player_location[0]][player_location[1]] = 1
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0]][player_location[1]+1] == 0:
#         print('cannot walk this way')
#         response['map'] = current_map
#         return response
#     elif current_map[player_location[0]][player_location[1]+1] == 3:
#         print('monster encounter')
#         encounter_success = monster_encounter_initial(response)
#         if encounter_success:
#             current_map[player_location[0]][player_location[1]+1] = 2
#             current_map[player_location[0]][player_location[1]] = 1
#             response['map'] = current_map
#             return response
#     elif current_map[player_location[0]][player_location[1]+1] == 4:
#         response['prompt'] = 'YOU HAVE FOUND A WEAPON'
#         # weapon = Weapon.objects.get()
#         # response['player']['inventory'].append(weapon)
#         # print(response['player']['inventory'])
#         # pick_up(response)
#         current_map[player_location[0]][player_location[1]+1] = 2
#         current_map[player_location[0]][player_location[1]] = 1
#         response['map'] = current_map
#         return response
#     response['map'] = current_map
#     return response

# def player_movement(response):
#     if response['message'] == 'move up':
#         response = player_move_up(response)
#         return response
#     if response['message'] == 'move down':
#         response = player_move_down (response)
#         return response
#     if response['message'] == 'move left':
#         response = player_move_left (response)
#         return response
#     if response['message'] == 'move right':
#         response = player_move_right (response)
#         return response