#!/usr/bin/env python3
import sys
import math
import copy

def f_print():
    print("MOVE", my_pac[0]['pac_id'], my_pac[0]['x_output'], my_pac[0]['y_output'], end='|')  
    if count_pac > 2:
        print("MOVE", my_pac[1]['pac_id'], my_pac[1]['x_output'], my_pac[1]['y_output'], end='|')
    elif count_pac == 2:
        print("MOVE", my_pac[1]['pac_id'], my_pac[1]['x_output'], my_pac[1]['y_output'])
    if count_pac > 3:
        print("MOVE", my_pac[2]['pac_id'], my_pac[2]['x_output'], my_pac[2]['y_output'], end='|')
    elif count_pac == 3:
        print("MOVE", my_pac[2]['pac_id'], my_pac[2]['x_output'], my_pac[2]['y_output'])
    if count_pac > 4:
        print("MOVE", my_pac[3]['pac_id'], my_pac[3]['x_output'], my_pac[3]['y_output'], end='|')
        print("MOVE", my_pac[4]['pac_id'], my_pac[4]['x_output'], my_pac[4]['y_output'])
    elif count_pac == 4:
        print("MOVE", my_pac[3]['pac_id'], my_pac[3]['x_output'], my_pac[3]['y_output'])

def how_much_point(x, y, new_row):
    if new_row[y][x] == '*':
        return(10)
    elif new_row[y][x] == '.':
        return(1)
    elif new_row[y][x] == ' ':
        return(0)
    elif '0' <= new_row[y][x] <= '9':
        return(-20)
    else:
        return(0)

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

def next_step(point, x, y, i, my_pac):
    if my_pac[i]['save_point'] < point:
        my_pac[i]['save_point'] = point
        my_pac[i]['x_output'] = x
        my_pac[i]['y_output'] = y

def algoritm(x, y, my_pac, i, new_row, count, height, width, point):

    if count > 0:
        point_a = how_much_point(next_x(x, '-', width), y, new_row)
        point_b = how_much_point(next_x(x, '+', width), y, new_row)
        point_c = how_much_point(x, next_y(y, '-', height), new_row)
        point_d = how_much_point(x, next_y(y, '+', height), new_row)

        count -= 1
        algoritm(next_x(x, '-', width), y, my_pac, i,  new_row, count, height, width, point + point_a)
        algoritm(next_x(x, '+', width), y, my_pac, i, new_row, count, height, width, point + point_b)
        algoritm(x, next_y(y, '-', height), my_pac, i, new_row, count, height, width, point + point_c)
        algoritm(x, next_y(y, '+', height), my_pac, i, new_row, count, height, width, point + point_d)
    else: 
        next_step(point, x, y, i, my_pac)

# Grab the pellets as fast as you can!

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
print(width, height, file=sys.stderr)
row = []
for i in range(height):
    row.append(list(input()))  # one line of the grid: space " " is floor, pound "#" is wall

# game loop
while True:
    new_row = copy.deepcopy(row)
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight
    my_pac = []
    opponent_pac = []
    count_pac = 0
    count_opponent_pac = 5

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
            count_pac += 1
            my_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown, 'x_output': 0, 'y_output': 0, 'save_point': 0, 'x_output_standart': 0, 'y_output_standart': 0})
        else:
            count_opponent_pac += 1
            new_row[y][x] = str(count_opponent_pac)
            opponent_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown})

    visible_pellet_count = int(input()) # all pellets in sight
    lenght_1 = width + height

    for j in range(visible_pellet_count):
        # value: amount of points this pellet is worth        
        x, y, value = [int(j) for j in input().split()]
        if value == 1:
                new_row[y][x] = '.'
        elif value == 10:
                new_row[y][x] = '*'
        for i in range(count_pac):
            len_min = abs(my_pac[i]['x'] - x) + abs(my_pac[i]['y'] - y)
            if len_min < lenght_1:
                my_pac[i]['x_output_standart'] = x
                my_pac[i]['y_output_standart'] = y
                lenght_1 = len_min

    for i in range(count_pac):
        x = my_pac[i]['x']
        y = my_pac[i]['y']
        count = 3
        point = 0
        algoritm(x, y, my_pac, i, new_row, count, height, width, point)
        if my_pac[i]['save_point'] == 0:
            my_pac[i]['x_output'] = my_pac[i]['x_output_standart']
            my_pac[i]['y_output'] = my_pac[i]['y_output_standart']
    f_print()