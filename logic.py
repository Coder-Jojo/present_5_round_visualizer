from time import sleep
import random
from pprint import pprint

sbox = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55, 8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59, 12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

sbox_inverse = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63]
glob = []


def travel_up(x, y, num):
    queue = [(x, y, num)]
    path = []

    while len(queue):
        x, y, num = queue.pop(0)

        if y == 0:
            break

        if num == 1:
            ix = x*4 + random.randint(0, 3)
            x1 = sbox_inverse[ix]

            queue.append((x1//4, y-1, 2))
            path.append((ix, y, x1, y-1))
        
        elif num == 2:
            ix1 = x*4 + random.randint(0, 3)
            ix2 = x*4 + random.randint(0, 3)

            while ix1 == ix2:
                ix2 = x*4 + random.randint(0, 3)
            
            x1 = sbox_inverse[ix1]
            x2 = sbox_inverse[ix2]

            queue.append((x1//4, y-1, 2))
            queue.append((x2//4, y-1, 2))

            path.append((ix1, y, x1, y-1))
            path.append((ix2, y, x2, y-1))
    
    return path


def travel_down(x, y, num):
    queue = [(x, y, num)]
    path = []

    while len(queue):
        x, y, num = queue.pop(0)

        if y == 4:
            break

        if num == 1:
            ix = x*4 + random.randint(0, 3)
            x1 = sbox[ix]

            queue.append((x1//4, y+1, 2))
            path.append((x1, y+1, ix, y))
        
        elif num == 2:
            ix1 = x*4 + random.randint(0, 3)
            ix2 = x*4 + random.randint(0, 3)

            while ix1 == ix2:
                ix2 = x*4 + random.randint(0, 3)
            
            x1 = sbox[ix1]
            x2 = sbox[ix2]

            queue.append((x1//4, y+1, 2))
            queue.append((x2//4, y+1, 2))

            path.append((x1, y+1, ix1, y))
            path.append((x2, y+1, ix2, y))
    
    return path


def wait_for_next():
    glob[0]['next'] = False
    
    while glob[0]['next'] == False:
        sleep(0.25)


def visualize(path, lines, sbox_layers):
    for x, y, x1, y1 in path:
        lines.add_line(x, y, x1, y1)
        sbox_layers[y].activate(x // 4)
        sbox_layers[y1].activate(x1 // 4)
        wait_for_next()

    for x, y, x1, y1 in path:
        lines.remove_line(x, y, x1, y1)
        sbox_layers[y].deactivate(x // 4)
        sbox_layers[y1].deactivate(x1 // 4)


def in_2_out_1(x, y, lines, sbox_layers):
    path_up = travel_up(x, y, 2)
    path_down = travel_down(x, y, 1)

    visualize(path_up + path_down, lines, sbox_layers)


def in_1_out_2(x, y, lines, sbox_layers):
    path_up = travel_up(x, y, 1)
    path_down = travel_down(x, y, 2)

    visualize(path_down + path_up, lines, sbox_layers)


def logic(sbox_layers, lines, options):

    sleep(2)
    glob.append(options)
    
    # y = int(input('choose the round number (0 - 4): '))
    # x = int(input('choose the sbox number (0 - 15): '))

    round = 0
    sbox = 0

    wait_for_next()
    in_2_out_1(round, sbox, lines, sbox_layers)
    wait_for_next()
    in_1_out_2(round, sbox, lines, sbox_layers)

    options['stop'] = True

    