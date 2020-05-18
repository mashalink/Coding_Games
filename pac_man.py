import sys
import math
import copy

def f_print():
    i = 0
    while (count_pac - 1) > i:
        if my_pac[i]['flag_speed'] == 1:
            print("SPEED", my_pac[i]['pac_id'], end='|')
        elif my_pac[i]['flag_speed'] == 2:
            print("SWITCH", my_pac[i]['pac_id'], my_pac[i]['flag'], end='|')
        else:
            print("MOVE", my_pac[i]['pac_id'], my_pac[i]['x_output'], my_pac[i]['y_output'], end='|')  
        i += 1
    if my_pac[i]['flag_speed'] == 1:
        print("SPEED", my_pac[i]['pac_id'])
    elif my_pac[i]['flag_speed'] == 2:
        print("SWITCH", my_pac[i]['pac_id'], my_pac[i]['flag'])
    else:
        print("MOVE", my_pac[i]['pac_id'], my_pac[i]['x_output'], my_pac[i]['y_output'])

def if_neighbor(i, my_pac, hope_row):
    n = my_pac[i]['neighbor']
    if my_pac[i]['x'] <= my_pac[n]['x'] and my_pac[i]['y'] < my_pac[n]['y']:
        k = 0
        while k <= height - 1:
            if '.' in hope_row[k]:
                a = 0
                while a <= width - 1:
                    if hope_row[k][a] == '.':
                        if a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k < my_pac[n]['y']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k += 1
        k = 0
        while k <= height - 1:
            if ' ' in hope_row[k]:
                a = 0
                while a <= width - 1:
                    if hope_row[k][a] == ' ':
                        if a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k < my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k += 1
    elif my_pac[i]['x'] < my_pac[n]['x'] and my_pac[i]['y'] >= my_pac[n]['y']:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == '.':
                        if a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k >= my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
        k = height - 1
        while k >= 0:
            if  ' ' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        if a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k >= my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
    elif my_pac[i]['x'] > my_pac[n]['x'] and my_pac[i]['y'] <= my_pac[n]['y']:
        k = 0
        while k <= height - 1:
            if '.' in hope_row[k]:
                a = 0
                while a < width:
                    if hope_row[k][a] == '.':
                        if a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k <= my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k += 1
        k = 0
        while k <= height - 1:
            if ' ' in hope_row[k]:
                a = 0
                while a < width:
                    if hope_row[k][a] == ' ':
                        if a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k <= my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k += 1
    elif my_pac[i]['x'] >= my_pac[n]['x'] and my_pac[i]['y'] > my_pac[n]['y']:
        k =  height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = 0
                while a < width:
                    if hope_row[k][a] == '.':
                        if a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k > my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k -= 1
        k =  height - 1
        while k >= 0:
            if ' ' in hope_row[k]:
                a = 0
                while a < width:
                    if hope_row[k][a] == ' ':
                        if a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2 and k > my_pac[i]['x']:
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k -= 1
    else:
        return(0)

def hope_step(i, my_pac, hope_row):
    c = width / 3
    d = height / 2
    e = width - c

    if my_pac[i]['x'] <= c and my_pac[i]['y'] <= d:
        k = 0
        while k <= height - 1:
            if '.' in hope_row[k]:
                a = int(c)
                while a >= 0:
                    if hope_row[k][a] == '.':
                        print('tyt!!!', a, k, file=sys.stderr)
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k += 1
        k = 0
        while k <= height - 1:
            if ' ' in hope_row[k]:
                a = int(c)
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        print('tyt2', file=sys.stderr)
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k += 1

    elif c < my_pac[i]['x'] < e and my_pac[i]['y'] <= d:
        k = 0
        while k < height - 1:
            if '.' in hope_row[k]:
                a = int(c)
                while a < e:
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a += 1
            k += 1
        k = 0
        while k < height - 1:
            if ' ' in hope_row[k]:
                a = int(c)
                while a < e:
                    if hope_row[k][a] == ' ':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a += 1
            k += 1
    
    elif my_pac[i]['x'] > e and my_pac[i]['y'] <= d:
        k = 0
        while k < height - 1:
            if '.' in hope_row[k]:
                a = width - 1
                while a > e:
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k += 1
        k = 0
        while k < height - 1:
            if ' ' in hope_row[k]:
                a = width - 1
                while a > e:
                    if hope_row[k][a] == ' ':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k += 1

    elif my_pac[i]['x'] < c and my_pac[i]['y'] > d:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = int(c)
                while a >= 0:
                    if hope_row[k][a] == '.':
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
        k = height - 1
        while k >= 0:
            if ' ' in hope_row[k]:
                a = int(c)
                while a >= 0:
                    if hope_row[k][a] == ' ':
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1

    elif c < my_pac[i]['x'] < e and my_pac[i]['y'] > d:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = int(c)
                while a < e:
                    if hope_row[k][a] == '.':
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k -= 1
        k = height - 1
        while k >= 0:
            if ' ' in hope_row[k]:
                a = int(c)
                while a < e:
                    if hope_row[k][a] == ' ':
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k -= 1
    elif my_pac[i]['x'] > e and my_pac[i]['y'] > d:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = width - 1
                while a > e:
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k -= 1
        height - 1
        while k >= 0:
            if ' ' in hope_row[k]:
                a = width - 1
                while a > e:
                    if hope_row[k][a] == ' ':
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1

    if my_pac[i]['y'] <= d:
        k = 0
        while k < height - 1:
            if '.' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k += 1
        k = 0
        while k < height - 1:
            if ' ' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k += 1
    else:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k -= 1
        k = height - 1
        while k >= 0:
            if ' ' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1

def how_much_point(x, y, new_row, old_x, old_y, count, count_min, flag):
    if new_row[y][x] == '*':
        return(10)
    elif new_row[y][x] == '.':
        return(1)
    elif new_row[y][x] == ' ':
        return(0)
    elif '0' <= new_row[y][x] <= '4':
        if count > count_min - 2:
            new_row[old_y][old_x] = '#'
        return(-1)
    elif new_row[y][x] == 'P' or new_row[y][x] == 'R' or new_row[y][x] == 'S':
        for j in range(count_opponent_pac):
            if opponent_pac[j]['x'] == x and y == opponent_pac[j]['y']:
                k = j
        if new_row[y][x] == 'P' and my_pac[i]['type_id'] == "SCISSORS" and count > count_min - 2 and my_pac[i]['speed_turns_left'] and  opponent_pac[k]['speed_turns_left'] == 0:
            return(5)
        if new_row[y][x] == 'R' and my_pac[i]['type_id'] == "PAPER" and count > count_min - 2 and my_pac[i]['speed_turns_left'] and  opponent_pac[k]['speed_turns_left'] == 0:
            return(5)
        if new_row[y][x] == 'S' and my_pac[i]['type_id'] == "ROCK" and count > count_min - 2  and my_pac[i]['speed_turns_left'] and  opponent_pac[k]['speed_turns_left'] == 0:
            return(5)
        if my_pac[i]['ability_cooldown'] == 0 and new_row[y][x] == 'P' and my_pac[i]['type_id'] == "ROCK" and count >= count_min - 5:
            flag = 'SCISSORS'
            next_step(point, x, y, i, my_pac, count, flag)
            return(-5)  
        if my_pac[i]['ability_cooldown'] == 0 and new_row[y][x] == 'R' and my_pac[i]['type_id'] == "SCISSORS" and count >= count_min - 5:
            flag = 'PAPER'
            next_step(point, x, y, i, my_pac, count, flag)
            return(-5)  
        if my_pac[i]['ability_cooldown'] == 0 and new_row[y][x] == 'S' and my_pac[i]['type_id'] == "PAPER" and count >= count_min - 5:
            flag = 'ROCK'
            next_step(point, x, y, i, my_pac, count, flag)
            return(-5)    
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

def next_step(point, x, y, i, my_pac, count, flag): 
    if flag != 'NEXT':
        my_pac[i]['flag'] = flag
    elif my_pac[i]['save_point'] < point or (my_pac[i]['save_point'] <= point and my_pac[i]['len'] > abs(my_pac[i]['x'] - x) + abs(my_pac[i]['y'] - y)):
        my_pac[i]['save_point'] = point
        my_pac[i]['len'] = abs(my_pac[i]['x'] - x) + abs(my_pac[i]['y'] - y)
        my_pac[i]['x_output'] = x
        my_pac[i]['y_output'] = y
             
def algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag):
    if count > 0:
        point_next, point_next_1, point_next_2 = 0, 0, 0
        x_new = next_x(x, '-', width)
        point_next = how_much_point(x_new, y, new_row, x, y, count, count_min, flag)
        y_new = next_y(y, '-', height)
        point_next_1 = how_much_point(x, y_new, new_row, x, y, count, count_min, flag)
        y_new_2 = next_y(y, '+', height)
        point_next_2 = how_much_point(x, y_new_2, new_row, x, y, count, count_min, flag)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            algoritm_1(x_new, y, my_pac, i,  new_row, count - 1, count_min, height, width, point + point_next, flag)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                algoritm_3(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1, flag)
            if point_next_2 >= 0:
                algoritm_4(x, y_new_2, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2, flag)
        if point_next < 1 and point_next_1 < 1 and point_next_2 < 1:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag)
            return(1)
        return(0)

def algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag):
    if count > 0:       
        point_next, point_next_1, point_next_2 = 0, 0, 0       
        x_new = next_x(x, '+', width)
        point_next = how_much_point(x_new, y, new_row, x, y, count, count_min, flag)
        y_new = next_y(y, '-', height)
        point_next_1 = how_much_point(x, y_new, new_row, x, y, count, count_min, flag)
        y_new_2 = next_y(y, '+', height)
        point_next_2 = how_much_point(x, y_new_2, new_row, x, y, count, count_min, flag)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            algoritm_2(x_new, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next, flag)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                algoritm_3(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1, flag)
            if point_next_2 >= 0:
                algoritm_4(x, y_new_2, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2, flag)
        if point_next < 0 and point_next_1 < 0 or point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag)
            return(1)
        return(0)

def algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag):
    if count > 0:        
        point_next, point_next_1, point_next_2 = 0, 0, 0       
        y_new = next_y(y, '-', height)
        point_next = how_much_point(x, y_new, new_row, x, y, count, count_min, flag)
        x_new = next_x(x, '-', width)
        point_next_1 = how_much_point(x_new, y, new_row, x, y, count, count_min, flag)
        x_new_2 = next_x(x, '+', width)
        point_next_2 = how_much_point(x_new_2, y, new_row, x, y, count, count_min, flag)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            algoritm_3(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next, flag)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                algoritm_1(x_new, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1, flag)
            if point_next_2 >= 0:
                algoritm_2(x_new_2, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2, flag)
        if point_next < 0 and point_next_1 < 0 and point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag)
            return(1)
        return(0)

def algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag): 
    if count > 0:      
        point_next, point_next_1, point_next_2 = 0, 0, 0
        y_new = next_y(y, '+', height)
        point_next = how_much_point(x, y_new, new_row, x, y, count, count_min, flag)
        x_new = next_x(x, '-', width)
        point_next_1 = how_much_point(x_new, y, new_row, x, y, count, count_min, flag)
        x_new_2 = next_x(x, '+', width)
        point_next_2 = how_much_point(x_new_2, y, new_row, x, y, count, count_min, flag)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            algoritm_4(x, y_new, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next, flag)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                algoritm_1(x_new, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_1, flag)
            if point_next_2 >= 0:
                algoritm_2(x_new_2, y, my_pac, i, new_row, count - 1, count_min, height, width, point + point_next_2, flag)
        if point_next < 0 and point_next_1 < 0 and point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag)
            return(1)
        return(0)

def algoritm(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag):
    if height // 3 >= x and width // 2 >= y:
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
    elif height // 3 <= x <= height // 3 * 2 and width // 2 >= y:
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
    elif height // 3 * 2 >= x and width // 2 >= y:
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
    elif height // 3 >= x and width // 2 <= y:
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
    elif height // 3 * 2 >= x and width // 2 <= y:
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)   
    else:
        algoritm_4(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_1(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_2(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)
        algoritm_3(x, y, my_pac, i, new_row, count, count_min, height, width, point, flag)

def hope_map(hope_row, my_pac, my_pac_old_place, width, height):
    for i in range(count_pac):
        if my_pac_old_place[i]['old_x'] != my_pac[i]['y'] or my_pac_old_place[i]['old_y'] != my_pac[i]['y']:
            
            a = next_x(my_pac[i]['x'], '-', width)
            if my_pac_old_place[i]['old_x'] == a and my_pac_old_place[i]['old_y'] == my_pac[i]['y']:
                hope_row[my_pac[i]['y']][a] = '$'
            
            a = next_x(my_pac[i]['x'], '-', width)
            b = next_x(a, '-', width)
            if my_pac_old_place[i]['old_x'] == b and my_pac_old_place[i]['old_y'] == my_pac[i]['y']:
                hope_row[my_pac[i]['y']][a] = '$'
                hope_row[my_pac[i]['y']][b] = '$'
            
            a = next_x(my_pac[i]['x'], '+', width)
            if my_pac_old_place[i]['old_x'] == a and my_pac_old_place[i]['old_y'] == my_pac[i]['y']:
                hope_row[my_pac[i]['y']][a] = '$'
            
            a = next_x(my_pac[i]['x'], '+', width)
            b = next_x(a, '+', width)
            if my_pac_old_place[i]['old_x'] == b and my_pac_old_place[i]['old_y'] == my_pac[i]['y']:
                hope_row[my_pac[i]['y']][a] = '$'
                hope_row[my_pac[i]['y']][b] = '$'


            a = next_y(my_pac[i]['y'], '-', width)
            if my_pac_old_place[i]['old_y'] == a and my_pac_old_place[i]['old_x'] == my_pac[i]['x']:
                hope_row[a][my_pac[i]['x']] = '$'
            
            a = next_y(my_pac[i]['y'], '-', width)
            b = next_y(a, '-', width)
            if my_pac_old_place[i]['old_y'] == b and my_pac_old_place[i]['old_x'] == my_pac[i]['x']:
                hope_row[a][my_pac[i]['x']] = '$'
                hope_row[b][my_pac[i]['x']] = '$'
            
            a = next_y(my_pac[i]['y'], '+', width)
            if my_pac_old_place[i]['old_y'] == a and my_pac_old_place[i]['old_x'] == my_pac[i]['x']:
                hope_row[a][my_pac[i]['x']] = '$'
            
            a = next_y(my_pac[i]['y'], '+', width)
            b = next_y(a, '+', width)
            if my_pac_old_place[i]['old_y'] == b and my_pac_old_place[i]['old_x'] == my_pac[i]['x']:
                hope_row[a][my_pac[i]['x']] = '$'
                hope_row[b][my_pac[i]['x']] = '$'


            a = next_x(my_pac[i]['x'], '-', width)
            b = next_y(my_pac[i]['y'], '-', width)
            if my_pac_old_place[i]['old_y'] == b and my_pac_old_place[i]['old_x'] == a:
                hope_row[b][a] = '$'
                if b + 1 < height:
                    if hope_row[b + 1][a] != '#':
                        hope_row[b + 1][a] = '$'
                    else:
                        hope_row[b][a + 1] = '$'
                else:
                    if hope_row[0][a] != '#':
                        hope_row[0][a] = '$'
                    else:
                        hope_row[0][a + 1] = '$'
            
            a = next_x(my_pac[i]['x'], '+', width)
            b = next_y(my_pac[i]['y'], '+', width)
            if my_pac_old_place[i]['old_y'] == b and my_pac_old_place[i]['old_x'] == a:
                hope_row[b][a] = '$'
                if b - 1 >= 0:
                    if hope_row[b - 1][a] != '#':
                        hope_row[b - 1][a] = '$'
                    else:
                        hope_row[b][a - 1] = '$'
                else:
                    if hope_row[height - 1][a] != '#':
                        hope_row[height - 1][a] = '$'
                    else:
                        hope_row[height - 1][a + 1] = '$'

            a = next_x(my_pac[i]['x'], '+', width)
            b = next_y(my_pac[i]['y'], '-', width)
            if my_pac_old_place[i]['old_y'] == b and my_pac_old_place[i]['old_x'] == a:
                hope_row[b][a] = '$'
                if b - 1 >= 0:
                    if hope_row[b - 1][a] != '#':
                        hope_row[b - 1][a] = '$'
                    else:
                        hope_row[b][a + 1] = '$'
                else:
                    if hope_row[height - 1][a] != '#':
                        hope_row[height - 1][a] = '$'
                    else:
                        hope_row[height - 1][a + 1] = '$'

            a = next_x(my_pac[i]['x'], '-', width)
            b = next_y(my_pac[i]['y'], '+', width)
            if my_pac_old_place[i]['old_y'] == b and my_pac_old_place[i]['old_x'] == a:
                hope_row[b][a] = '$'
                if b + 1 < height:
                    if hope_row[b + 1][a] != '#':
                        hope_row[b + 1][a] = '$'
                    else:
                        hope_row[b][a - 1] = '$'
                else:
                    if hope_row[0][a] != '#':
                        hope_row[0][a] = '$'
                    else:
                        hope_row[0][a - 1] = '$'

def new_info_for_hope_row(hope_row, new_row, my_pac, count_pac, width, height):
    for i in range(count_pac):
        x = my_pac[i]['x']
        y = my_pac[i]['y']

        check_x = next_x(x, '-', width)
        while new_row[y][check_x] != '#':
            if new_row[y][check_x] == ' ' and hope_row[y][check_x] == '.':
                hope_row[y][check_x] == '$'
            check_x = next_x(check_x, '-', width)
        check_x = next_x(x, '+', width)
        while new_row[y][check_x] != '#':
            if new_row[y][check_x] == ' ' and hope_row[y][check_x] == '.':
                hope_row[y][check_x] == '$'
            check_x = next_x(check_x, '+', width)

        check_y = next_y(y, '-', height)
        while new_row[check_y][x] != '#':
            if new_row[check_y][x] == ' ' and hope_row[check_y][check_x] == '.':
                hope_row[check_y][x] == '$'
            check_y = next_y(check_y, '-', width)
        check_y = next_y(y, '+', height)
        while new_row[check_y][x] != '#':
            if new_row[check_y][x] == ' ' and hope_row[check_y][x] == '.':
                hope_row[check_y][x] == '$'
            check_y = next_y(check_y, '+', width)

width, height = [int(i) for i in input().split()]

row = []
my_pac_old_place = []
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
    count_opponent_pac = 0
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
            hope_row[y][x] = str(count_pac)
            my_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown, 'x_output': 0, 'y_output': 0, 'save_point': -1, 'flag_speed': 0, 'flag': 'NEXT', 'neighbor': -1, 'len': width})            
            count_pac += 1
        else:
            hope_row[y][x] = '$'
            if type_id == 'PAPER':
                new_row[y][x] = 'P'
            if type_id == 'ROCK':
                new_row[y][x] = 'R'
            if type_id == 'SCISSORS':
                new_row[y][x] = 'S'
            opponent_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown})
            count_opponent_pac += 1

    visible_pellet_count = int(input())
    len_big_pellet = height + width
    flag_for_save = 0
    for j in range(visible_pellet_count):        
        x, y, value = [int(j) for j in input().split()]
        if value == 1:
            new_row[y][x] = '.'
            hope_row[y][x] = '.'
        elif value == 10:
            new_row[y][x] = '*'
            hope_row[y][x] = '.'

    if count_step != 1:
        hope_map(hope_row, my_pac, my_pac_old_place, width, height)
        for i in range(count_pac):
            my_pac_old_place[i]['old_x'] = my_pac[i]['x']
            my_pac_old_place[i]['old_y'] = my_pac[i]['y']
    else:
        for i in range(count_pac):
            my_pac_old_place.append({'old_x': my_pac[i]['x'], 'old_y': my_pac[i]['y']})

    for i in range(count_pac):
        for j in range(count_pac):
            if j != i:
                if abs(my_pac[i]['x'] - my_pac[j]['x']) + abs(my_pac[i]['y'] - my_pac[j]['y']) < 6:
                    if my_pac[i]['neighbor'] == -1:
                        my_pac[i]['neighbor'] = j
                    if my_pac[j]['neighbor'] == -1:
                        my_pac[j]['neighbor'] = i

    for i in range(count_pac):
        x_start = my_pac[i]['x']
        y_start = my_pac[i]['y']
        count, count_min, point, flag = 3, 3, 0, 'NEXT'
        if my_pac[i]['flag_speed'] == 0:
            algoritm(x_start, y_start, my_pac, i, new_row, count, count_min, height, width, point, flag)
            if my_pac[i]['save_point'] == 0 and my_pac[i]['flag'] == 'NEXT':
                count, count_min, point = 7, 7, 0
                algoritm(x_start, y_start, my_pac, i, new_row, count, count_min, height, width, point, flag)
                if my_pac[i]['save_point'] == 0 and my_pac[i]['flag'] == 'NEXT':
                    if my_pac[i]['neighbor'] != -1:
                        if if_neighbor(i, my_pac, hope_row) == 0:
                            hope_step(i, my_pac, hope_row)
                    else:
                        hope_step(i, my_pac, hope_row)
        if my_pac[i]['flag'] != 'NEXT':
            my_pac[i]['flag_speed'] = 2
        elif my_pac[i]['ability_cooldown'] == 0:
            my_pac[i]['flag_speed'] = 1
    f_print()