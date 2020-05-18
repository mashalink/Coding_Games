import sys
import math
import copy
#wall?
#if don't have results count = 10
def f_print():
    i = 0
    while (count_pac - 1) > i:
        if my_pac[i]['flag_speed'] == 1:
            print("SPEED", my_pac[i]['pac_id'], end='|')
        elif my_pac[i]['flag_speed'] == 2:
            print("SWITCH", my_pac[i]['pac_id'], my_pac[i]['type_id_next'], end='|')
        else:
            print("MOVE", my_pac[i]['pac_id'], my_pac[i]['x_output'], my_pac[i]['y_output'], end='|')  
        i += 1
    if my_pac[i]['flag_speed'] == 1:
        print("SPEED", my_pac[i]['pac_id'])
    elif my_pac[i]['flag_speed'] == 2:
        print("SWITCH", my_pac[i]['pac_id'], my_pac[i]['type_id_next'])
    else:
        print("MOVE", my_pac[i]['pac_id'], my_pac[i]['x_output'], my_pac[i]['y_output'])

def hope_step(i, my_pac, hope_row):
    if i == 0 or i == 4:
        k = 0
        while k <= height - 1:
            if ' ' in hope_row[k]:
                my_pac[i]['x_output'] = hope_row[k].index(' ')
                my_pac[i]['y_output'] = k
                break
            k += 1
    elif i == 1:
        k = height - 1
        while k >= 1:
            if ' ' in hope_row[k]:
                my_pac[i]['x_output'] = hope_row[k].index(' ')
                my_pac[i]['y_output'] = k
                break
            k -= 1
    elif i == 2:
        k = height - 2
        while k >= 1:
            if ' ' in hope_row[k]:
                my_pac[i]['x_output'] = hope_row[k].index(' ')
                my_pac[i]['y_output'] = k
                break
            k -= 1
    elif i == 3:
        k = 1
        while k <= height - 1:
            if ' ' in hope_row[k]:
                my_pac[i]['x_output'] = hope_row[k].index(' ')
                my_pac[i]['y_output'] = k
                break
            k += 1

def how_much_point(x, y, new_row, old_x, old_y, count, count_min):
    if new_row[y][x] == '*':
        return(10)
    elif new_row[y][x] == '.':
        return(1)
    elif new_row[y][x] == ' ':
        return(0)
    elif '0' <= new_row[y][x] <= '4':
        if count > count_min:
            print('tyt', file=sys.stderr)
            new_row[old_y][old_x] = '#'
        return(-1)
    elif '5' <= new_row[y][x] <= '9':
        return(-5)
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

def next_step(point, x, y, i, my_pac, count):   
    if my_pac[i]['save_point'] < point:
        my_pac[i]['save_point'] = point
        my_pac[i]['x_output'] = x
        my_pac[i]['y_output'] = y
             
def algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point):
    if count > 0:
        point_next, point_next_1, point_next_2 = 0, 0, 0
        x_new = next_x(x, '-', width)
        point_next = how_much_point(x_new, y, new_row, x, y, count, count_min)
        if point_next >= 0:
            algoritm_1(x_new, y, my_pac, i,  new_row, count - 1, count_min, height, width, point + point_next)
        if count != 5 and point_next > -2:
            y_new = next_y(y, '-', height)
            point_next_1 = how_much_point(x, y_new, new_row, x, y, count, count_min)
            y_new_2 = next_y(y, '+', height)
            point_next_2 = how_much_point(x, y_new_2, new_row, x, y, count, count_min)
            if point_next_1 >= 0:
                algoritm_3(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1)
            if point_next_2 >= 0:
                algoritm_4(x, y_new_2, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2)
        if point_next < 1 and point_next_1 < 1 and point_next_2 < 1:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point):
    if count > 0:       
        point_next, point_next_1, point_next_2 = 0, 0, 0       
        x_new = next_x(x, '+', width)
        point_next = how_much_point(x_new, y, new_row, x, y, count, count_min)
        if point_next >= 0:
            algoritm_2(x_new, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next)
        if count != 5 and point_next > -2:
            y_new = next_y(y, '-', height)
            point_next_1 = how_much_point(x, y_new, new_row, x, y, count, count_min)
            y_new_2 = next_y(y, '+', height)
            point_next_2 = how_much_point(x, y_new_2, new_row, x, y, count, count_min)
            if point_next_1 >= 0:
                algoritm_3(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1)
            if point_next_2 >= 0:
                algoritm_4(x, y_new_2, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2)
        if point_next < 0 and point_next_1 < 0 or point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point):
    if count > 0:        
        point_next, point_next_1, point_next_2 = 0, 0, 0       
        y_new = next_y(y, '-', height)
        point_next = how_much_point(x, y_new, new_row, x, y, count, count_min)
        if point_next >= 0:
            algoritm_3(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next)
        if count != 5 and point_next > -2:
            x_new = next_x(x, '-', width)
            point_next_1 = how_much_point(x_new, y, new_row, x, y, count, count_min)
            x_new_2 = next_x(x, '+', width)
            point_next_2 = how_much_point(x_new_2, y, new_row, x, y, count, count_min)
            if point_next_1 >= 0:
                algoritm_1(x_new, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1)
            if point_next_2 >= 0:
                algoritm_2(x_new_2, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2)
        if point_next < 0 and point_next_1 < 0 and point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point): 
    if count > 0:      
        point_next, point_next_1, point_next_2 = 0, 0, 0
        y_new = next_y(y, '+', height)
        point_next = how_much_point(x, y_new, new_row, x, y, count, count_min)
        if point_next >= 0:
            algoritm_4(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next)
        if count != 5 and point_next > -2:
            x_new = next_x(x, '-', width)
            point_next_1 = how_much_point(x_new, y, new_row, x, y, count, count_min)
            x_new_2 = next_x(x, '+', width)
            point_next_2 = how_much_point(x_new_2, y, new_row, x, y, count, count_min)
            if point_next_1 >= 0:
                algoritm_1(x_new, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1)
            if point_next_2 >= 0:
                algoritm_2(x_new_2, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2)
        if point_next < 0 and point_next_1 < 0 and point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count)
            return(1)
        return(0)

def algoritm(x, y, my_pac, i, new_row, count, count_min, height, width, point):
    if height // 3 >= x and width // 2 >= y:
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point)
    elif height // 3 >= x and width // 2 <= y:
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point)
    elif height - height // 3 >= x and width // 2 >= y:
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point)
    elif height - height // 3 >= x and width // 2 <= y:
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point)
    else:
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point)



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
            print('EEE', x, y, file=sys.stderr)
            new_row[y][x] = str(count_pac)
            hope_row[y][x] = '$'
            count_pac += 1
            my_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown, 'x_output': 0, 'y_output': 0, 'save_point': -1, 'flag_speed': 0, 'flag': 0})            
        else:
            hope_row[y][x] = '$'
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
            hope_row[y][x] = '$'
        elif value == 10:
            new_row[y][x] = '*'
            hope_row[y][x] = '$'

    for i in range(count_pac):
        for j in range(count_pac):
            if j != i:
                my_pac[i]
    #for i in range(height):
    #    print(new_row[i], file=sys.stderr)
    #for i in range(height):
    #    print(hope_row[i], file=sys.stderr) 
      
    for i in range(count_pac):
        x_start = my_pac[i]['x']
        y_start = my_pac[i]['y']
        count, count_min, point = 3, 1, 0
        if my_pac[i]['ability_cooldown'] == 0:
            my_pac[i]['flag_speed'] = 1
        if my_pac[i]['flag'] == 0:
            algoritm(x_start, y_start, my_pac, i, new_row, count, count_min, height, width, point)
            if my_pac[i]['save_point'] == 0:
                count, count_min, point = 10, 8, 0
                algoritm(x_start, y_start, my_pac, i, new_row, count, count_min, height, width, point)
                if my_pac[i]['save_point'] == 0: # need to fix 
                    hope_step(i, my_pac, hope_row)
                   
    f_print()