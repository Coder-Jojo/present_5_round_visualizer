from time import sleep 
import random 
from pprint import pprint
from collections import defaultdict 
from math import log2 

player = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55, 8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59, 12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

player_inverse = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63]
glob = []

sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
sbox_inverse = [5, 14, 15, 8, 12, 1, 2, 13, 11, 4, 6, 3, 0, 7, 9, 10]

def get_ddt():
    ddt = [[0 for i in range(16)] for j in range(16)]
    for i in range(16):
        for j in range(16):
            ddt[i^j][sbox[i] ^ sbox[j]] += 1 
    return ddt

ddt = get_ddt()

def get_2_input_1_output_lookup():
    lookup = defaultdict(lambda : list())
    lookdown = defaultdict(lambda : list())
    for i in [1, 2, 4, 8]:
        for j in [1, 2, 4, 8]:
            if i != j:
                for k in [1, 2, 4, 8]:
                    if ddt[i+j][k]:
                        lookup[i+j].append(k)
                        lookdown[k].append(i+j)
                    if ddt[k][i+j]:
                        lookup[k].append(i+j)
                        lookdown[i+j].append(k)
    for key, value in lookup.items():
        lookup[key] = list(set(value))
    for key, value in lookdown.items():
        lookdown[key] = list(set(value))
    return lookup, lookdown

lookup, lookdown = get_2_input_1_output_lookup()

def create_path(round, sn, input_bits):
    path_down, path_up = [], []
    org_sn = sn
    sbox_state = [[0, 0] for i in range(16)]
    
    if input_bits == 2:
        start_in = [3, 5, 6, 9, 10, 12][random.randint(0, 5)]
    else:
        start_in = [1, 2, 4, 8][random.randint(0, 3)]
    start_out = lookup[start_in][random.randint(0, len(lookup[start_in]) - 1)]
    sbox_state[org_sn] = [start_in, start_out]

    # print(sbox_state)

    for r in range(round, 4):
        new_sbox_state = [[0, 0] for i in range(16)]
        for sn, (i, o) in enumerate(sbox_state):
            if i == 0:
                continue
            
            o_out = list()
            for p, one, in enumerate(str(bin(o)[2:].zfill(4))):
                if one == '1':
                    o_out.append(p)

            if len(o_out) >= 1:
                out_line = sn*4 + o_out[0]
                new_in_line = player[out_line]
                path_down.append((new_in_line, r+1, out_line, r))
                new_sbox_state[new_in_line//4][0] += 2**(new_in_line%4)
            if len(o_out) >= 2:
                out_line = sn*4 + o_out[1]
                new_in_line = player[out_line]
                path_down.append((new_in_line, r+1, out_line, r))
                new_sbox_state[new_in_line//4][0] += 2**(new_in_line%4)

        for sn, (i, o) in enumerate(new_sbox_state):
            if i == 0:
                sbox_state[sn] = [0, 0]
            else:
                sbox_state[sn] = [i, lookup[i][random.randint(0, len(lookup[i]) - 1)]]
    
    sbox_state = [[0, 0] for i in range(16)]
    sbox_state[org_sn] = [start_in, start_out]
    print(sbox_state)

    for r in range(round, 0, -1):
        new_sbox_state = [[0, 0] for i in range(16)]
        for sn, (i, o) in enumerate(sbox_state):
            if o == 0:
                continue
            
            i_out = list()
            for p, one, in enumerate(str(bin(i)[2:].zfill(4))):
                if one == '1':
                    i_out.append(p)
            # print(i_out)
            if len(i_out) >= 1:
                out_line = sn*4 + i_out[0]
                new_in_line = player_inverse[out_line]
                path_up.append((out_line, r, new_in_line, r-1))
                new_sbox_state[new_in_line//4][1] += 2**(new_in_line%4)
            if len(i_out) >= 2:
                out_line = sn*4 + i_out[1]
                new_in_line = player_inverse[out_line]
                path_up.append((out_line, r, new_in_line, r-1))
                new_sbox_state[new_in_line//4][1] += 2**(new_in_line%4)
        # print(new_sbox_state)
        for sn, (i, o) in enumerate(new_sbox_state):
            if o == 0:
                sbox_state[sn] = [0, 0]
            else:
                sbox_state[sn] = [lookdown[o][random.randint(0, len(lookdown[o]) - 1)], o]
        
        # print(f'round: {r}', sbox_state)
    return path_up + path_down

def wait_for_next():
    glob[0]['next'] = False
    
    while glob[0]['next'] == False:
        sleep(0.25)

def visualize(path, lines, player_layers):
    for x, y, x1, y1 in path:
        lines.add_line(x, y, x1, y1)
        player_layers[y].activate(x // 4)
        player_layers[y1].activate(x1 // 4)
        wait_for_next()

    for x, y, x1, y1 in path:
        lines.remove_line(x, y, x1, y1)
        player_layers[y].deactivate(x // 4)
        player_layers[y1].deactivate(x1 // 4)


def logic_sbox(player_lines, lines, options):
    sleep(2)
    glob.append(options)

    round = options['round']
    sbox = options['sbox']
    
    wait_for_next()
    path = create_path(round, sbox, 2)
    visualize(path, lines, player_lines)
    wait_for_next()
    path = create_path(round, sbox, 4)
    visualize(path, lines, player_lines)
    options['stop'] = True

if __name__ == '__main__':
    logic_sbox(player, glob, [])
    # pprint(lookup)
    # pprint(lookdown)

