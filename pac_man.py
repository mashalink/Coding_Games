import sys
import math
import copy

def f_print():
    if count_pac > 1:
        if my_pac[0]['flag_speed'] == 1:
            print("SPEED", my_pac[0]['pac_id'], end='|')
        else:
            print("MOVE", my_pac[0]['pac_id'], my_pac[0]['x_output'], my_pac[0]['y_output'], end='|')  
    elif count_pac == 1:
        if my_pac[0]['flag_speed'] == 1:
            print("SPEED", my_pac[0]['pac_id'])
        else:
            print("MOVE", my_pac[0]['pac_id'], my_pac[0]['x_output'], my_pac[0]['y_output'])  
    if count_pac > 2:
        if my_pac[1]['flag_speed'] == 1:
            print("SPEED", my_pac[1]['pac_id'], end='|')
        else:
            print("MOVE", my_pac[1]['pac_id'], my_pac[1]['x_output'], my_pac[1]['y_output'], end='|')
    elif count_pac == 2:
        if my_pac[1]['flag_speed'] == 1:
            print("SPEED", my_pac[1]['pac_id'])
        else:
            print("MOVE", my_pac[1]['pac_id'], my_pac[1]['x_output'], my_pac[1]['y_output'])
    if count_pac > 3:
        if my_pac[2]['flag_speed'] == 1:
            print("SPEED", my_pac[2]['pac_id'], end='|')
        else:
            print("MOVE", my_pac[2]['pac_id'], my_pac[2]['x_output'], my_pac[2]['y_output'], end='|')
    elif count_pac == 3:
        if my_pac[2]['flag_speed'] == 1:
            print("SPEED", my_pac[2]['pac_id'])
        else:
            print("MOVE", my_pac[2]['pac_id'], my_pac[2]['x_output'], my_pac[2]['y_output'])
    if count_pac > 4:
        if my_pac[3]['flag_speed'] == 1:
            print("SPEED", my_pac[3]['pac_id'], end='|')
        else:
            print("MOVE", my_pac[3]['pac_id'], my_pac[3]['x_output'], my_pac[3]['y_output'], end='|')
        if my_pac[4]['flag_speed'] == 1:
            print("SPEED", my_pac[4]['pac_id'])
        else:
            print("MOVE", my_pac[4]['pac_id'], my_pac[4]['x_output'], my_pac[4]['y_output'])
    elif count_pac == 4:
        if my_pac[3]['flag_speed'] == 1:
            print("SPEED", my_pac[3]['pac_id'])
        else:
            print("MOVE", my_pac[3]['pac_id'], my_pac[3]['x_output'], my_pac[3]['y_output'])

def how_much_point(x, y, new_row):
    if new_row[y][x] == '*':
        return(10)
    elif new_row[y][x] == '.':
        return(1)
    elif new_row[y][x] == ' ':
        return(0)
    elif '0' <= new_row[y][x] <= '4':
        return(-2)
    elif '5' <= new_row[y][x] <= '9':
        return(-3)
    elif '#' == new_row[y][x]:
        return(-1)

def next_x(x, a, width):
    if a == '-':
        if x - 1 < 0:
            x = width - 1
            return(x)
        else:
            x -= 1
            return(x)
    else:
        if x + 1 == width:
            x = 0
            return(x)
        else:
            x += 1
            return(x)

def next_y(y, a, height):
    if a == '-':
        if y - 1 < 0:
            y = height - 1
            return(y)
        else:
            y -= 1
            return(y)
    else:
        if y + 1 == height:
            y = 0
            return(y)
        else:
            y += 1
            return(y)

def next_step(point, point_zero, x, y, i, my_pac, count):   
    if my_pac[i]['save_point'] < point or (my_pac[i]['save_point'] == point and (abs(my_pac[i]['x_output'] - my_pac[i]['x']) > abs(x - my_pac[i]['x']) or abs(my_pac[i]['y_output'] - my_pac[i]['y']) > abs(y - my_pac[i]['y']))):
        my_pac[i]['save_point'] = point
        my_pac[i]['x_output'] = x
        my_pac[i]['y_output'] = y
    if my_pac[i]['save_point_zero'] < point_zero:
        my_pac[i]['save_point_zero'] = point_zero
        my_pac[i]['x_output_zero'] = x
        my_pac[i]['y_output_zero'] = y
       # print(my_pac[i]['x_output_zero'], my_pac[i]['y_output_zero'], file=sys.stderr)
             
def algoritm_1(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point):
    if count > 0:
        point_next = 0
        x_new = next_x(x, '-', width)
        point_next = how_much_point(x_new, y, new_row)
        if point_next >= 0:
            count -= 1
            if point_next == 0:
                point_zero += 1
            algoritm_1(x_new, y, my_pac, i,  new_row, count, height, width, point + point_next, point_zero, min_point)
        if count != 5 and point_next > -2:
            y_new = next_y(y, '-', height)
            point_next = how_much_point(x, y_new, new_row)
            y_new_2 = next_y(y, '+', height)
            point_next_2 = how_much_point(x, y_new_2, new_row)
            if point_next >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_3(x, y_new, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
            if point_next_2 >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_4(x, y_new_2, my_pac, i, new_row, count, height, width, point + point_next_2, point_zero, min_point)
            if point_next < 1 and point_next_2 < 1:
                if point > min_point or point_zero > min_point:
                    next_step(point, point_zero, x, y, i, my_pac, count)
                    return(1)
                return(0)
        else:
            return(0)
    else:
        if point > min_point or point_zero > min_point:
            next_step(point, point_zero, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm_2(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point):
    if count > 0:       
        point_next = 0       
        x_new = next_x(x, '+', width)
        point_next = how_much_point(x_new, y, new_row)
        if point_next >= 0:
            count -= 1
            if point_next == 0:
                point_zero += 1
            algoritm_2(x_new, y, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
        if count != 5 and point_next > -2:
            y_new = next_y(y, '-', height)
            point_next = how_much_point(x, y_new, new_row)
            y_new_2 = next_y(y, '+', height)
            point_next_2 = how_much_point(x, y_new_2, new_row)
            if point_next >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_3(x, y_new, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
            if point_next_2 >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_4(x, y_new_2, my_pac, i, new_row, count, height, width, point + point_next_2, point_zero, min_point)
            if point_next < 0 or point_next_2 < 0:
                if point > min_point or point_zero > min_point:
                    next_step(point, point_zero, x, y, i, my_pac, count)
                    return(1)
                return(0)
        else:
            return(0)
    else:
        if point > min_point or point_zero > min_point:
            next_step(point, point_zero, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm_3(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point):
    if count > 0:        
        point_next = 0        
        y_new = next_y(y, '-', height)
        point_next = how_much_point(x, y_new, new_row)
        if point_next >= 0:
            count -= 1
            if point_next == 0:
                point_zero += 1
            algoritm_3(x, y_new, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
        if count != 5 and point_next > -2:
            x_new = next_x(x, '-', width)
            point_next = how_much_point(x_new, y, new_row)
            x_new_2 = next_x(x, '+', width)
            point_next_2 = how_much_point(x_new_2, y, new_row)
            if point_next >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_1(x_new, y, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
            if point_next_2 >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_2(x_new_2, y, my_pac, i, new_row, count, height, width, point + point_next_2, point_zero, min_point)
            if point_next < 0 and point_next_2 < 0:
                if point > min_point or point_zero > min_point:
                    next_step(point, point_zero, x, y, i, my_pac, count)
                    return(1)
                return(0)
        else:
            return(0)
    else:
        if point > min_point or point_zero > min_point:
            next_step(point, point_zero, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm_4(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point): 
    if count > 0:   
        point_next = 0
        y_new = next_y(y, '+', height)
        point_next = how_much_point(x, y_new, new_row)
        if point_next >= 0:
            count -= 1
            if point_next == 0:
                point_zero += 1
            algoritm_4(x, y_new, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
        if count != 5 and point_next > -2:
            x_new = next_x(x, '-', width)
            point_next = how_much_point(x_new, y, new_row)
            x_new_2 = next_x(x, '+', width)
            point_next_2 = how_much_point(x_new_2, y, new_row)
            if point_next >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_1(x_new, y, my_pac, i, new_row, count, height, width, point + point_next, point_zero, min_point)
            if point_next_2 >= 0:
                count -= 1
                if point_next == 0:
                    point_zero += 1
                algoritm_2(x_new_2, y, my_pac, i, new_row, count, height, width, point + point_next_2, point_zero, min_point)
            if point_next < 0 and point_next_2 < 0:
                if point > min_point or point_zero > min_point:
                    next_step(point, point_zero, x, y, i, my_pac, count)
                    return(1)
                return(0)
        else:
            return(0)
    else:
        if point > min_point or point_zero > min_point:
            next_step(point, point_zero, x, y, i, my_pac, count)
            return(1)
        return(0)


def algoritm(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point):
    if i == 0:
        algoritm_1(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_2(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_3(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_4(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
    elif i  == 1:
        algoritm_2(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_1(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_4(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_3(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
    elif i == 2:
        algoritm_3(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_2(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_4(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_1(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
    elif i == 3:
        algoritm_4(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_3(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_2(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_1(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
    elif i == 4:
        algoritm_3(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_4(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_1(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
        algoritm_2(x, y, my_pac, i, new_row, count, height, width, point, point_zero, min_point)

width, height = [int(i) for i in input().split()]

row = []
for i in range(height):
    row.append(list(input()))
count_step = 0
hope_row = copy.deepcopy(row)

# game loop
while True:
    new_row = copy.deepcopy(row)
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())
    my_pac = []
    opponent_pac = []
    count_pac = 0
    count_opponent_pac = 5
    count_step += 1
    for i in range(visible_pac_count):

        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)
        mine = int(mine)
        
        if mine != 0:
            new_row[y][x] = str(count_pac)
            hope_row[y][x] = '$'
            count_pac += 1
            my_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown, 'x_output': 0, 'y_output': 0, 'save_point': 0, 'x_output_zero': 0, 'y_output_zero': 0, 'save_point_zero': 0, 'len': 0, 'flag_speed': 0, 'flag': 0})            
        else:
            count_opponent_pac += 1
            new_row[y][x] = str(count_opponent_pac)
            opponent_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown})
    visible_pellet_count = int(input()) # all pellets in sight
    len_big_pellet = height + width
    flag_for_save = 0

    for j in range(visible_pellet_count):
        # value: amount of points this pellet is worth        
        x, y, value = [int(j) for j in input().split()]
        if value == 1:
            new_row[y][x] = '.'
            print('have', file=sys.stderr)
        elif value == 10:
            new_row[y][x] = '*'
         
    for i in range(count_pac):
        x_start = my_pac[i]['x']
        y_start = my_pac[i]['y']
        count, min_point, point, point_zero = 5, 0, 0, 0
        if count_step % 10 == 1:
            my_pac[i]['flag_speed'] = 1
        if my_pac[i]['flag'] == 0:
            algoritm(x_start, y_start, my_pac, i, new_row, count, height, width, point, point_zero, min_point)
            if my_pac[i]['save_point'] == 0:
                if i == 0 or i == 4:
                    k = 1
                    while k <= height - 1:
                        my_pac[i]['x_output'] = hope_row[k].index(' ')
                        if my_pac[i]['x_output'] > -1:
                            my_pac[i]['y_output'] = k
                            break
                        k += 1
                if i == 2:
                    k = height - 1
                    while k >= 1:
                        my_pac[i]['x_output'] = hope_row[k].index(' ')
                        if my_pac[i]['x_output'] > -1:
                            my_pac[i]['y_output'] = k
                            break
                        k -= 1
                if i == 3:
                    k = height - 1
                    while k >= 1:
                        my_pac[i]['x_output'] = hope_row[k].index(' ')
                        if my_pac[i]['x_output'] > -1:
                            my_pac[i]['y_output'] = k
                            break
                        k -= 1
                if i == 0 or i == 4:
                    k = 1
                    while k <= height - 1:
                        my_pac[i]['x_output'] = hope_row[k].index(' ')
                        if my_pac[i]['x_output'] > -1:
                            my_pac[i]['y_output'] = k
                            break
                        k += 1
    f_print()