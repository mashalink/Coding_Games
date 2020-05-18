import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle to grab it and use your team id to determine towards where you need to throw it.
# Use the Wingardium spell to move things around at your leisure, the more magic you put it, the further they'll move.

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left

my_goal = {'state': 0, 'goal_x': 0, 'goal_y': 0}
opponent_goal = {'state': 0, 'goal_x': 0, 'goal_y': 0}
 
# MY left, OPPONENT right
if my_team_id == 1:
    my_goal['goal_x'] = 16000
    my_goal['goal_y'] = 3750
    my_goal['state'] = 0
    opponent_goal['goal_x'] = 0
    opponent_goal['goal_y'] = 3750
    opponent_goal['state'] = 1
# MY right, OPPONENT left
else:
    my_goal['goal_x'] = 0
    my_goal['goal_y'] = 3750
    my_goal['state'] = 1
    opponent_goal['goal_x'] = 16000
    opponent_goal['goal_y'] = 3750
    opponent_goal['state'] = 0
                    
# game loop
turn = 0

while True:
    turn += 1
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    
    wizard = []
    opponent_wizard = []
    snaffle = []
    bludger = []
    goal_warning = {'state': 0, 'entity_id': 0} 
    goal_score = {'state': 0, 'entity_id': 0}
    num_snaffle = 0
   
    flag = 0
    flag2 = 0
    min_lenght = 16000
    min_lenght2 = 16000
    min_lenght_wiz = 16000
    min_lenght_wiz2 = 16000
    x_min_for_wiz = 0
    y_min_for_wiz = 0
    x_min_for_wiz2 = 0
    y_min_for_wiz2 = 0
    
    for i in range(entities):
        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)
        
        if (entity_type == "WIZARD"):
            wizard.append({'entity_id': entity_id, 'entity_type': entity_type, 'x': x, 'y': y, 'vx': vx, 'vy': vy, 'state': state})
        
        if (entity_type == "OPPONENT_WIZARD"):
            opponent_wizard.append({'entity_id': entity_id, 'entity_type': entity_type, 'x': x, 'y': y, 'vx': vx, 'vy': vy, 'state': state})
            
        if (entity_type == "SNAFFLE"):
            snaffle.append({'entity_id': entity_id, 'entity_type': entity_type, 'x': x, 'y': y, 'vx': vx, 'vy': vy, 'state': state})
            
            num_snaffle += 1        
            
            p = ((wizard[0]['x'] - x) ** 2 + (wizard[0]['y'] - y) ** 2) ** 0.5
            p2 = ((wizard[1]['x'] - x) ** 2 + (wizard[1]['y'] - y) ** 2) ** 0.5          
            if p < p2 :
                if p < min_lenght_wiz:
                    min_lenght_wiz = p
                    x_min_for_wiz = x
                    y_min_for_wiz = y
                    id_for_wiz = entity_id
                elif p2 < min_lenght_wiz2:
                    min_lenght_wiz2 = p2
                    x_min_for_wiz2 = x
                    y_min_for_wiz2 = y
                    id_for_wiz2 = entity_id           
            else:
                if p2 < min_lenght_wiz2:
                    min_lenght_wiz2 = p2
                    x_min_for_wiz2 = x
                    y_min_for_wiz2 = y
                    id_for_wiz2 = entity_id
                elif p < min_lenght_wiz:
                    min_lenght_wiz = p
                    x_min_for_wiz = x
                    y_min_for_wiz = y
                    id_for_wiz = entity_id
                    
            p = ((my_goal['goal_x'] - x) ** 2 + (my_goal['goal_y'] - y) ** 2) ** 0.5
            if p < min_lenght2 and ((x != x_min_for_wiz and y != y_min_for_wiz) or (x != x_min_for_wiz2 and y != y_min_for_wiz2)):
                min_lenght2 = p
                id_wizarium2 = entity_id           
            p = ((opponent_goal['goal_x'] - x) ** 2 + (opponent_goal['goal_y'] - y) ** 2) ** 0.5
            if p < min_lenght and ((x != x_min_for_wiz and y != y_min_for_wiz) or (x != x_min_for_wiz2 and y != y_min_for_wiz2)):
                min_lenght = p
                id_wizarium = entity_id
            
        if (entity_type == "BLUDGER"):
            bludger.append({'entity_id': entity_id, 'entity_type': entity_type, 'x': x, 'y': y, 'vx': vx, 'vy': vy, 'state': state})
            
    if wizard[0]['state'] != 0 and ((wizard[0]['x'] < 8000 and my_goal['goal_x'] == 0) or (wizard[0]['x'] > 8000 and my_goal['goal_x'] == 16000)):       
        if my_goal['goal_x'] == 0:           
            if wizard[0]['y'] < 3000:
                len = abs(opponent_goal['goal_x'] - wizard[0]['x'])
                x_push = int(wizard[0]['y'] / my_goal['goal_y'] * len) + wizard[0]['x']
                print("THROW", x_push, 0, '500')       
            elif wizard[0]['y'] > 4500:
                len = abs(opponent_goal['goal_x'] - wizard[0]['x'])
                x_push = int(my_goal['goal_y'] / wizard[0]['y'] * len) + wizard[0]['x']
                print("THROW", x_push, 7500, '500')
            elif wizard[1]['state'] == 0 and 3000 < ((wizard[0]['x'] - wizard[1]['x']) ** 2 + (wizard[0]['y'] - wizard[1]['y']) ** 2) ** 0.5:
                print("THROW", wizard[1]['x'], wizard[1]['y'], '500')
            else:
                print("THROW", wizard[0]['x'] + 3000, wizard[0]['y'], '500')       
        else:           
            if wizard[0]['y'] < 3000:
                x_push = int(wizard[0]['y'] / my_goal['goal_y'] * wizard[0]['x']) - wizard[0]['x']
                print("THROW", x_push, 0, '500')       
            elif wizard[0]['y'] > 4500:
                x_push = int(my_goal['goal_y'] / wizard[0]['y'] * wizard[0]['x']) - wizard[0]['x']
                print("THROW", x_push, 7500, '500')
            elif wizard[1]['state'] == 0 and 3000 < ((wizard[0]['x'] - wizard[1]['x']) ** 2 + (wizard[0]['y'] - wizard[1]['y']) ** 2) ** 0.5:
                print("THROW", wizard[1]['x'], wizard[1]['y'], '500')
            else:
                print("THROW", wizard[0]['x'] - 3000, wizard[0]['y'], '500')    
    elif wizard[0]['state'] != 0:
        print("THROW", opponent_goal['goal_x'], opponent_goal['goal_y'], '500')  
    else:
        if opponent_wizard[0]['state'] != 0 and my_magic > 65 and ((wizard[1]['x'] < 8000 and my_goal['goal_x'] == 0) or (wizard[1]['x'] > 8000 and my_goal['goal_x'] == 16000)):
            if opponent_wizard[0]['x'] < 8000 and my_goal['goal_x'] == 0:
                if opponent_wizard[0]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] + 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] + 5000, 7500, 10)
            else:
                if opponent_wizard[0]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] - 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] - 5000, 7500, 10)
            flag = 1
        elif opponent_wizard[1]['state'] != 0 and my_magic > 10 and ((wizard[1]['x'] < 8000 and my_goal['goal_x'] == 0) or (wizard[1]['x'] > 8000 and my_goal['goal_x'] == 16000)):
            if opponent_wizard[1]['x'] < 8000 and my_goal['goal_x'] == 0:
                if opponent_wizard[1]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] + 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] + 5000, 7500, 10)
            else:
                if opponent_wizard[1]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] - 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] - 5000, 7500, 10)
            flag2 = 1
        elif my_magic > min_lenght / 100:
            print("WINGARDIUM", id_wizarium, opponent_goal['goal_x'], opponent_goal['goal_y'], my_magic)
        elif my_magic > 50:
            print("WINGARDIUM", id_wizarium2, opponent_goal['goal_x'], opponent_goal['goal_y'], my_magic)
        elif min_lenght_wiz == 16000:
            print("MOVE", x_min_for_wiz2, y_min_for_wiz2, '150')
        else:
            print("MOVE", x_min_for_wiz, y_min_for_wiz, '150')
    
    if wizard[1]['state'] != 0 and ((wizard[1]['x'] < 8000 and my_goal['goal_x'] == 0) or (wizard[1]['x'] > 8000 and my_goal['goal_x'] == 16000)):
        if my_goal['goal_x'] == 0:           
            if wizard[1]['y'] < 3000:
                len = abs(opponent_goal['goal_x'] - wizard[1]['x'])
                x_push = int(wizard[1]['y'] / my_goal['goal_y'] * len) + wizard[1]['x']
                print("THROW", x_push, 0, '500')       
            elif wizard[1]['y'] > 4500:
                len = abs(opponent_goal['goal_x'] - wizard[1]['x'])
                x_push = int(my_goal['goal_y'] / wizard[1]['y'] * len) + wizard[1]['x']
                print("THROW", x_push, 7500, '500')
            elif wizard[0]['state'] == 0 and 3000 < ((wizard[0]['x'] - wizard[1]['x']) ** 2 + (wizard[0]['y'] - wizard[1]['y']) ** 2) ** 0.5:
                print("THROW", wizard[0]['x'], wizard[0]['y'], '500')
            else:
                print("THROW", wizard[1]['x'] + 3000, wizard[1]['y'], '500')       
        else:           
            if wizard[1]['y'] < 3000:
                x_push = int(wizard[1]['y'] / my_goal['goal_y'] * wizard[1]['x']) - wizard[1]['x']
                print("THROW", x_push, 0, '500')       
            elif wizard[0]['y'] > 4500:
                x_push = int(my_goal['goal_y'] / wizard[1]['y'] * wizard[1]['x']) - wizard[1]['x']
                print("THROW", x_push, 7500, '500') 
            elif wizard[0]['state'] == 0 and 3000 < ((wizard[0]['x'] - wizard[1]['x']) ** 2 + (wizard[0]['y'] - wizard[1]['y']) ** 2) ** 0.5:
                print("THROW", wizard[0]['x'], wizard[0]['y'], '500')
            else:
                print("THROW", wizard[1]['x'] - 3000, wizard[1]['y'], '500')   
    elif wizard[1]['state'] != 0:
        print("THROW", opponent_goal['goal_x'], opponent_goal['goal_y'], '500')   
    else: 
        if opponent_wizard[0]['state'] != 0 and my_magic > 65 and flag == 0 and ((wizard[0]['x'] < 8000 and my_goal['goal_x'] == 0) or (wizard[0]['x'] > 8000 and my_goal['goal_x'] == 16000)):
            if opponent_wizard[0]['x'] < 8000 and my_goal['goal_x'] == 0:
                if opponent_wizard[0]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] + 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] + 5000, 7500, 10)
            else:
                if opponent_wizard[0]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] - 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[0]['entity_id'], opponent_wizard[0]['x'] - 5000, 7500, 10)
        elif opponent_wizard[1]['state'] != 0 and my_magic > 10 and flag2 == 0 and ((wizard[1]['x'] < 8000 and my_goal['goal_x'] == 0) or (wizard[1]['x'] > 8000 and my_goal['goal_x'] == 16000)):
            if opponent_wizard[1]['x'] < 8000 and my_goal['goal_x'] == 0:
                if opponent_wizard[1]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] + 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] + 5000, 7500, 10)
            else:
                if opponent_wizard[1]['x'] <= 3500:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] - 5000, 0, 10)
                else:
                    print("WINGARDIUM", opponent_wizard[1]['entity_id'], opponent_wizard[1]['x'] - 5000, 7500, 10)
        elif my_magic > min_lenght / 100 or my_magic > 50:
            print("WINGARDIUM", id_wizarium, opponent_goal['goal_x'], opponent_goal['goal_y'], my_magic)
        elif my_magic > 50:
            print("WINGARDIUM", id_wizarium2, opponent_goal['goal_x'], opponent_goal['goal_y'], my_magic)    
        elif min_lenght_wiz2 == 16000:
            print("MOVE", x_min_for_wiz, y_min_for_wiz, '150')
        elif num_snaffle:
            print("MOVE", x_min_for_wiz2, y_min_for_wiz2, '150')