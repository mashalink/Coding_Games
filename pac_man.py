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

def if_neighbor(i, my_pac, hope_row, tunnel):
    n = my_pac[i]['neighbor']
    tun = 0
    tun2 = height
    if count_tunnel == 1:
        if tunnel[0]['row'] < height / 2:
            tun = tunnel[0]['row']
        if tunnel[0]['row'] > height / 2:
            tun2 = tun
    elif count_tunnel > 1:
        if tunnel[0]['row'] < height / 2:
            tun = tunnel[0]['row']
        if tunnel[0]['row'] > height / 2:
            tun2 = tunnel[count_tunnel - 1]['row']
    if my_pac[i]['x'] <= my_pac[n]['x'] and my_pac[i]['y'] > my_pac[n]['y']:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k] and k > my_pac[n]['y']:
                a = 0
                while a < width - 1:
                    if hope_row[k][a] == '.':
                        if (a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a + 2 < my_pac[n]['x'] and tun2 > my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k -= 1
        k = height - 1
        while k >= 0:
            if ' ' in hope_row[k] and k > my_pac[n]['y']:
                a = 0
                while a <= width - 1:
                    if hope_row[k][a] == ' ':
                        if (a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a + 2 < my_pac[n]['x'] and tun2 > my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a += 1
            k -= 1
        return(0)
    elif my_pac[i]['x'] < my_pac[n]['x'] and my_pac[i]['y'] <= my_pac[n]['y']:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]  and k >= my_pac[n]['y']:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == '.':
                        if (a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a + 2 < my_pac[n]['x'] and tun2 >= my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
        k = height - 1
        while k >= 0:
            if ' ' in hope_row[k]  and k >= my_pac[n]['y']:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        if (a + 2 < my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a + 2 < my_pac[n]['x'] and tun2 >= my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
        return(0)
    elif my_pac[i]['x'] > my_pac[n]['x'] and my_pac[i]['y'] <= my_pac[n]['y']:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k] and k >= my_pac[n]['y']:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == '.':
                        if (a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a - 2 > my_pac[n]['x'] and tun2 >= my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
        k = height - 1
        while k >= 0:
            if ' ' in hope_row[k] and k >= my_pac[n]['y']:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        if (a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a - 2 > my_pac[n]['x'] and tun2 >= my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k -= 1
        return(0)
    elif my_pac[i]['x'] >= my_pac[n]['x'] and my_pac[i]['y'] > my_pac[n]['y']:
        k = 0
        while k <= height - 1:
            if '.' in hope_row[k]  and k < my_pac[n]['y']:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == '.':
                        if (a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a - 2 < my_pac[n]['x'] and tun <= my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k += 1
        k = 0
        while k <= height - 1:
            if ' ' in hope_row[k]  and k < my_pac[n]['y']:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        if (a - 2 > my_pac[n]['x'] and abs(a - my_pac[i]['x']) < width / 2) or (a - 2 < my_pac[n]['x'] and tun < my_pac[n]['y']):
                            my_pac[i]['x_output'] = a
                            my_pac[i]['y_output'] = k
                            return(1)
                    a -= 1
            k += 1
    else:
        return(0)
           
def hope_step(i, my_pac, hope_row, height, width):
    c = width / 3
    d = height / 2
    e = width - c

    if my_pac[i]['x'] <= c and my_pac[i]['y'] <= d and my_pac[i]['neighbor'] == -1:
        k = 0
        while k <= height - 1:
            if '.' in hope_row[k]:
                a = 0
                while a < int(c):
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a += 1
            k += 1
    elif c < my_pac[i]['x'] < e and my_pac[i]['y'] <= d and my_pac[i]['neighbor'] == -1:
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
    elif my_pac[i]['x'] > e and my_pac[i]['y'] <= d and my_pac[i]['neighbor'] == -1:
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
    elif my_pac[i]['x'] < c and my_pac[i]['y'] > d and my_pac[i]['neighbor'] == -1:
        k = height - 1
        while k >= 0:
            if '.' in hope_row[k]:
                a = 0
                while a < int(c):
                    if hope_row[k][a] == '.':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a += 1
            k -= 1
    elif c < my_pac[i]['x'] < e and my_pac[i]['y'] > d and my_pac[i]['neighbor'] == -1:
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
    elif my_pac[i]['x'] > e and my_pac[i]['y'] > d and my_pac[i]['neighbor'] == -1: 
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
    if my_pac[i]['y'] <= d:
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
            if ' ' in hope_row[k]:
                a = width - 1
                while a >= 0:
                    if hope_row[k][a] == ' ':
                        my_pac[i]['x_output'] = a
                        my_pac[i]['y_output'] = k
                        return(1)
                    a -= 1
            k -= 1
    return(0)
      
def how_much_point(x, y, new_row, old_x, old_y, count, count_min, flag, count_opponent_pac):
    if new_row[y][x] == '*':
        return(10)
    elif new_row[y][x] == '.':
        return(1)
    elif new_row[y][x] == ' ':
        return(0)
    elif '0' <= new_row[y][x] <= '4':
        if count > count_min - 2:
            new_row[old_y][old_x] = '#'
        return(-5)
    elif new_row[y][x] == 'P' or new_row[y][x] == 'R' or new_row[y][x] == 'S':
        for j in range(count_opponent_pac):
            if x - 1 <= opponent_pac[j]['x'] <= x + 1 and y - 1 <= opponent_pac[j]['y'] <= y + 1:
                k = j
        if new_row[y][x] == 'P' and my_pac[i]['type_id'] == "SCISSORS" and (my_pac[i]['speed_turns_left'] > opponent_pac[k]['speed_turns_left'] or (my_pac[i]['speed_turns_left'] >= opponent_pac[k]['speed_turns_left'] and count >= count_min - 1)):
            return(15)
        if new_row[y][x] == 'R' and my_pac[i]['type_id'] == "PAPER"  and (my_pac[i]['speed_turns_left'] > opponent_pac[k]['speed_turns_left'] or (my_pac[i]['speed_turns_left'] == opponent_pac[k]['speed_turns_left'] and count >= count_min - 1)):
            return(15)
        if new_row[y][x] == 'S' and my_pac[i]['type_id'] == "ROCK"  and (my_pac[i]['speed_turns_left'] > opponent_pac[k]['speed_turns_left'] or (my_pac[i]['speed_turns_left'] == opponent_pac[k]['speed_turns_left'] and count >= count_min - 1)):
            return(15)
        if my_pac[i]['ability_cooldown'] == 0 and new_row[y][x] == 'P' and my_pac[i]['type_id'] != 'SCISSORS' and count >= count_min - 4:
            flag = 'SCISSORS'
            next_step(point, x, y, i, my_pac, count, flag, start)
            return(-5)  
        if my_pac[i]['ability_cooldown'] == 0 and new_row[y][x] == 'R' and my_pac[i]['type_id'] != 'PAPER' and count >= count_min - 4:
            flag = 'PAPER'
            next_step(point, x, y, i, my_pac, count, flag, start)
            return(-5)  
        if my_pac[i]['ability_cooldown'] == 0 and new_row[y][x] == 'S' and my_pac[i]['type_id'] != 'ROCK' and count >= count_min - 4:
            flag = 'ROCK'
            next_step(point, x, y, i, my_pac, count, flag, start)
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

def next_step(point, x, y, i, my_pac, count, flag, start): 
    if flag != 'NEXT':
        my_pac[i]['flag'] = flag
    elif my_pac[i]['save_point'] < point:
        my_pac[i]['len'] = abs(my_pac[i]['x'] - x) + abs(my_pac[i]['y'] - y)
        my_pac[i]['save_point'] = point
        my_pac[i]['x_output'] = x
        my_pac[i]['y_output'] = y
        my_pac[i]['start'] = start
             
def algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start):
    if count > 0:
        point_next, point_next_1, point_next_2 = 0, 0, 0
        x_new = next_x(x, '-', width)
        point_next = how_much_point(x_new, y, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        y_new = next_y(y, '-', height)
        point_next_1 = how_much_point(x, y_new, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        y_new_2 = next_y(y, '+', height)
        point_next_2 = how_much_point(x, y_new_2, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            if start == 0 and point_next > 0:
                algoritm_1(x_new, y, my_pac, i,  hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, count)
            else:
                algoritm_1(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, start)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_3(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, count)
                else:
                    algoritm_3(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, start)
            if point_next_2 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_4(x, y_new_2, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, count)
                else:
                    algoritm_4(x, y_new_2, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, start)
        if point_next < 0 and point_next_1 < 0 or point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag, start)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag, start)
            return(1)
        return(0)

def algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start):
    if count > 0:       
        point_next, point_next_1, point_next_2 = 0, 0, 0       
        x_new = next_x(x, '+', width)
        point_next = how_much_point(x_new, y, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        y_new = next_y(y, '-', height)
        point_next_1 = how_much_point(x, y_new, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        y_new_2 = next_y(y, '+', height)
        point_next_2 = how_much_point(x, y_new_2, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            if start == 0 and point_next > 0:
                algoritm_2(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, count)
            else:
                algoritm_2(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, start)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_3(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, count)
                else:
                    algoritm_3(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, start)
            if point_next_2 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_4(x, y_new_2, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, count)
                else:
                    algoritm_4(x, y_new_2, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, start)
        if point_next < 0 and point_next_1 < 0 or point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag, start)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag, start)
            return(1)
        return(0)

def algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start):
    if count > 0:        
        point_next, point_next_1, point_next_2 = 0, 0, 0       
        y_new = next_y(y, '-', height)
        point_next = how_much_point(x, y_new, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        x_new = next_x(x, '-', width)
        point_next_1 = how_much_point(x_new, y, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        x_new_2 = next_x(x, '+', width)
        point_next_2 = how_much_point(x_new_2, y, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            if start == 0 and point_next > 0:
                algoritm_3(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, count)
            else:
                algoritm_3(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, start)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_1(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, count)
                else:
                    algoritm_1(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, start)
            if point_next_2 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_2(x_new_2, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, count)
                else:
                    algoritm_2(x_new_2, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, start)
        if point_next < 0 and point_next_1 < 0 and point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag, start)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag, start)
            return(1)
        return(0)

def algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start): 
    if count > 0:      
        point_next, point_next_1, point_next_2 = 0, 0, 0
        y_new = next_y(y, '+', height)
        point_next = how_much_point(x, y_new, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        x_new = next_x(x, '-', width)
        point_next_1 = how_much_point(x_new, y, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        x_new_2 = next_x(x, '+', width)
        point_next_2 = how_much_point(x_new_2, y, hope_row, x, y, count, count_min, flag, count_opponent_pac)
        if point_next == -5 or point_next_1 == -5 or point_next_2 == -5:
            return(0)
        if point_next >= 0:
            if start == 0 and point_next > 0:
                algoritm_4(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, count)
            else:
                algoritm_4(x, y_new, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next, flag, count_opponent_pac, start)
        if count != 5 and point_next > -2:
            if point_next_1 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_1(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, count)
                else:
                    algoritm_1(x_new, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_1, flag, count_opponent_pac, start)
            if point_next_2 >= 0:
                if start == 0 and point_next > 0:
                    algoritm_2(x_new_2, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, count)
                else:
                    algoritm_2(x_new_2, y, my_pac, i, hope_row, count - 1, count_min, height, width, point + point_next_2, flag, count_opponent_pac, start)
        if point_next < 0 and point_next_1 < 0 and point_next_2 < 0:
            if point >= 0:
                next_step(point, x, y, i, my_pac, count, flag, start)
                return(1)
            return(0)
    else:
        if point >= 0:
            next_step(point, x, y, i, my_pac, count, flag, start)
            return(1)
        return(0)

def algoritm(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start):
    if height // 3 >= x and width // 2 >= y:
        algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
    elif height // 3 <= x <= height // 3 * 2 and width // 2 >= y:
        algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
    elif height // 3 * 2 >= x and width // 2 >= y:
        algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
    elif height // 3 >= x and width // 2 <= y:
        algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
    elif height // 3 * 2 >= x and width // 2 <= y:
        algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)   
    else:
        algoritm_4(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_1(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_2(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
        algoritm_3(x, y, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)

def new_info_for_hope_row(hope_row, new_row, my_pac, count_pac, width, height):
    for i in range(count_pac):
        x = my_pac[i]['x']
        y = my_pac[i]['y']

        check_x = next_x(x, '-', width)
        while new_row[y][check_x] != '#':
            if new_row[y][check_x] == ' ' and (hope_row[y][check_x] == '.' or hope_row[y][check_x] == '*'):
                hope_row[y][check_x] = ' '
            check_x = next_x(check_x, '-', width)
        check_x = next_x(x, '+', width)
        while new_row[y][check_x] != '#':
            if new_row[y][check_x] == ' ' and (hope_row[y][check_x] == '.' or hope_row[y][check_x] == '*'):
                hope_row[y][check_x] = ' '
            check_x = next_x(check_x, '+', width)

        check_y = next_y(y, '-', height)
        while new_row[check_y][x] != '#':
            if new_row[check_y][x] == ' ' and (hope_row[check_y][check_x] == '.' or hope_row[y][check_x] == '*'):
                hope_row[check_y][x] = ' '
            check_y = next_y(check_y, '-', width)
        check_y = next_y(y, '+', height)
        while new_row[check_y][x] != '#':
            if new_row[check_y][x] == ' ' and (hope_row[check_y][x] == '.' or hope_row[y][check_x] == '*'):
                hope_row[check_y][x] = ' '
            check_y = next_y(check_y, '+', width)


width, height = [int(i) for i in input().split()]

row = []
for i in range(height):
    row.append(list(input()))

count_step = 0

hope_row = copy.deepcopy(row)
for i in range(height):
    for j in range(width):
        if hope_row[i][j] == ' ':
           hope_row[i][j] = '.'

tunnel = []
count_tunnel = 0
for i in range(height):
    if row[i][0] == ' ':
        tunnel.append({'row': i})
        count_tunnel += 1

# game loop
while True:
    new_row = copy.deepcopy(row)
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())
    my_pac, opponent_pac, count_pac, count_opponent_pac = [], [], 0, 0
    count_step += 1

    for i in range(height):
        for j in range(width):
            if hope_row[i][j] == 'P' or hope_row[i][j] == 'R' or hope_row[i][j] == 'S' or '0' <= hope_row[i][j] <= '5':
                hope_row[i][j] = ' '
    
    for i in range(visible_pac_count):
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)
        mine = int(mine)
        if mine != 0:
            if type_id != "DEAD":
                new_row[y][x] = str(count_pac)           
                hope_row[y][x] = str(count_pac)
                my_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown, 'x_output': 0, 'y_output': 0, 'save_point': -1, 'flag_speed': 0, 'flag': 'NEXT', 'neighbor': -1, 'start': 0, 'len': width})            
                count_pac += 1
        else:
            if type_id != "DEAD":
                if type_id == 'PAPER':
                    hope_row[y][x] = 'P'
                if type_id == 'ROCK':
                    hope_row[y][x] = 'R'
                if type_id == 'SCISSORS':
                    hope_row[y][x] = 'S'
            opponent_pac.append({'pac_id': pac_id, 'x': x, 'y': y, 'type_id': type_id, 'speed_turns_left': speed_turns_left, 'ability_cooldown': ability_cooldown})
            count_opponent_pac += 1

    visible_pellet_count = int(input())

    for j in range(visible_pellet_count):        
        x, y, value = [int(j) for j in input().split()]
        if value == 1:
            new_row[y][x] = '.'
            hope_row[y][x] = '.'
        elif value == 10:
            new_row[y][x] = '*'
            hope_row[y][x] = '*'

    new_info_for_hope_row(hope_row, new_row, my_pac, count_pac, width, height)

    if count_step == 1:
        for i in range(count_pac):
            if my_pac[i]['type_id'] == 'PAPER':
                if hope_row[my_pac[i]['y']][width - my_pac[i]['x'] - 1] != 'P':
                    for j in range(count_pac):
                        if i != j:
                            if abs(my_pac[i]['y'] - my_pac[j]['y']) + abs((width - my_pac[i]['x'] - 1) - my_pac[j]['x']) < 5 and my_pac[j]['type_id'] != 'SCISSORS':
                                flag = 'SCISSORS'
                                next_step(0, 0, 0, j, my_pac, 0, flag, 0)
            if my_pac[i]['type_id'] == 'ROCK':
                if hope_row[my_pac[i]['y']][width - my_pac[i]['x'] - 1] != 'R':
                    for j in range(count_pac):
                        if i != j:
                            if abs(my_pac[i]['y'] - my_pac[j]['y']) + abs((width - my_pac[i]['x'] - 1) - my_pac[j]['x']) < 5 and my_pac[j]['type_id'] != 'SCISSORS':
                                flag = 'PAPER'
                                next_step(0, 0, 0, j, my_pac, 0, flag, 0)
            if my_pac[i]['type_id'] == 'SCISSORS':
                if hope_row[my_pac[i]['y']][width - my_pac[i]['x'] - 1] != 'S':
                    for j in range(count_pac):
                        if i != j:
                            if abs(my_pac[i]['y'] - my_pac[j]['y']) + abs((width - my_pac[i]['x'] - 1) - my_pac[j]['x']) < 5 and my_pac[j]['type_id'] != 'SCISSORS':
                                flag = 'ROCK'
                                next_step(0, 0, 0, j, my_pac, 0, flag, 0)

    for i in range(count_pac):
        for j in range(count_pac):
            if j != i:
                if abs(my_pac[i]['x'] - my_pac[j]['x']) + abs(my_pac[i]['y'] - my_pac[j]['y']) < 10:
                    if my_pac[i]['neighbor'] == -1:
                        my_pac[i]['neighbor'] = j
                    if my_pac[j]['neighbor'] == -1:
                        my_pac[j]['neighbor'] = i

    for i in range(count_pac):
        x_start = my_pac[i]['x']
        y_start = my_pac[i]['y']
        count, count_min, point, flag, start = 3, 3, 0, 'NEXT', 0 
        if my_pac[i]['flag_speed'] == 0:
            algoritm(x_start, y_start, my_pac, i, hope_row, count, count_min, height, width, point, flag, count_opponent_pac, start)
            if my_pac[i]['save_point'] == 0 and my_pac[i]['flag'] == 'NEXT':
                count, count_min, point = 7, 7, 0
                if my_pac[i]['save_point'] == 0 and my_pac[i]['flag'] == 'NEXT':
                    if my_pac[i]['neighbor'] != -1:
                        if if_neighbor(i, my_pac, hope_row, tunnel) == 0:
                            hope_step(i, my_pac, hope_row, height, width)
                    else:
                        hope_step(i, my_pac, hope_row, height, width)
        if my_pac[i]['flag'] != 'NEXT':
            my_pac[i]['flag_speed'] = 2
        elif my_pac[i]['ability_cooldown'] == 0:
            my_pac[i]['flag_speed'] = 1
    f_print()