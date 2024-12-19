import numpy as np
import math
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/06/b'
os.chdir(dir)


### Develop solution

data_ex = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

data_ex = data_ex.splitlines()
data_ex = [list(x) for x in data_ex]
data_ex = np.array(data_ex)
data_ex = np.pad(data_ex, pad_width=1, mode='constant', constant_values=0)

def get_path(input):
    data = input.copy()
    position = '.'
    n_rotations = 0
    path = []
    while position != '0':
        if math.modf(n_rotations / 4)[0] == 0.25:
            data = np.rot90(data)
            data = np.rot90(data)
            data = np.rot90(data)
            path.append(np.where(data == '^'))
            data = np.rot90(data)
        elif math.modf(n_rotations / 4)[0] == 0.50:
            data = np.rot90(data)
            data = np.rot90(data)
            path.append(np.where(data == '^'))
            data = np.rot90(data)
            data = np.rot90(data)
        elif math.modf(n_rotations / 4)[0] == 0.75:
            data = np.rot90(data)
            path.append(np.where(data == '^'))
            data = np.rot90(data)
            data = np.rot90(data)
            data = np.rot90(data)
        else:
            path.append(np.where(data == '^'))
        coords = np.where(data == '^')
        if data[coords[0][0] - 1][coords[1][0]] == '#':
            n_rotations += 1
            data = np.rot90(data)
        else:
            position = data[coords[0][0] - 1][coords[1][0]]
            data[coords[0][0]][coords[1][0]] = 'X'
            data[coords[0][0] - 1][coords[1][0]] = '^'
    return np.unique(path, axis=0)

candidates = get_path(data_ex)

def get_output(input):
    successes = []
    for i in range(len(candidates)):
        data = input.copy()
        if (candidates[i][0][0] == np.where(input == '^')[0][0]) & (candidates[i][1][0] == np.where(input == '^')[1][0]):
            continue
        data[candidates[i][0][0]][candidates[i][1][0]] = '#'
        position = '.'
        n_rotations = 0
        hits = {}
        while position != '0':
            coords = np.where(data == '^')
            if data[coords[0][0] - 1][coords[1][0]] == '#':
                data[coords[0][0] - 1][coords[1][0]] = '!'
                if math.modf(n_rotations / 4)[0] == 0.25:
                    data = np.rot90(data)
                    data = np.rot90(data)
                    data = np.rot90(data)
                    hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                    if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                        successes.append(candidates[i])
                        break
                    data = np.rot90(data)
                elif math.modf(n_rotations / 4)[0] == 0.50:
                    data = np.rot90(data)
                    data = np.rot90(data)
                    hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                    if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                        successes.append(candidates[i])
                        break
                    data = np.rot90(data)
                    data = np.rot90(data)
                elif math.modf(n_rotations / 4)[0] == 0.75:
                    data = np.rot90(data)
                    hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                    if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                        successes.append(candidates[i])
                        break
                    data = np.rot90(data)
                    data = np.rot90(data)
                    data = np.rot90(data)
                else:
                    hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                    if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                        successes.append(candidates[i])
                        break
                data[coords[0][0] - 1][coords[1][0]] = '#'
                n_rotations += 1
                data = np.rot90(data)
            else:
                position = data[coords[0][0] - 1][coords[1][0]]
                data[coords[0][0]][coords[1][0]] = 'X'
                data[coords[0][0] - 1][coords[1][0]] = '^'
    return len(successes)

get_output(data_ex)


### Create function

def main(data):
    data = data.splitlines()
    data = [list(x) for x in data]
    data = np.array(data)
    data = np.pad(data, pad_width=1, mode='constant', constant_values=0)

    def get_path(input):
        data = input.copy()
        position = '.'
        n_rotations = 0
        path = []
        while position != '0':
            if math.modf(n_rotations / 4)[0] == 0.25:
                data = np.rot90(data)
                data = np.rot90(data)
                data = np.rot90(data)
                path.append(np.where(data == '^'))
                data = np.rot90(data)
            elif math.modf(n_rotations / 4)[0] == 0.50:
                data = np.rot90(data)
                data = np.rot90(data)
                path.append(np.where(data == '^'))
                data = np.rot90(data)
                data = np.rot90(data)
            elif math.modf(n_rotations / 4)[0] == 0.75:
                data = np.rot90(data)
                path.append(np.where(data == '^'))
                data = np.rot90(data)
                data = np.rot90(data)
                data = np.rot90(data)
            else:
                path.append(np.where(data == '^'))
            coords = np.where(data == '^')
            if data[coords[0][0] - 1][coords[1][0]] == '#':
                n_rotations += 1
                data = np.rot90(data)
            else:
                position = data[coords[0][0] - 1][coords[1][0]]
                data[coords[0][0]][coords[1][0]] = 'X'
                data[coords[0][0] - 1][coords[1][0]] = '^'
        return np.unique(path, axis=0)

    candidates = get_path(data)

    def get_output(input):
        successes = []
        for i in range(len(candidates)):
            print('i = ' + str(i + 1) + ' out of ' + str(len(candidates)))
            data = input.copy()
            if (candidates[i][0][0] == np.where(input == '^')[0][0]) & (candidates[i][1][0] == np.where(input == '^')[1][0]):
                continue
            data[candidates[i][0][0]][candidates[i][1][0]] = '#'
            position = '.'
            n_rotations = 0
            hits = {}
            while position != '0':
                coords = np.where(data == '^')
                if data[coords[0][0] - 1][coords[1][0]] == '#':
                    data[coords[0][0] - 1][coords[1][0]] = '!'
                    if math.modf(n_rotations / 4)[0] == 0.25:
                        data = np.rot90(data)
                        data = np.rot90(data)
                        data = np.rot90(data)
                        hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                        if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                            successes.append(candidates[i])
                            break
                        data = np.rot90(data)
                    elif math.modf(n_rotations / 4)[0] == 0.50:
                        data = np.rot90(data)
                        data = np.rot90(data)
                        hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                        if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                            successes.append(candidates[i])
                            break
                        data = np.rot90(data)
                        data = np.rot90(data)
                    elif math.modf(n_rotations / 4)[0] == 0.75:
                        data = np.rot90(data)
                        hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                        if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                            successes.append(candidates[i])
                            break
                        data = np.rot90(data)
                        data = np.rot90(data)
                        data = np.rot90(data)
                    else:
                        hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] = hits.get('[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']', 0) + 1
                        if hits['[' + str(np.where(data == '!')[0][0]) + ',' + str(np.where(data == '!')[1][0]) + ']'] > 4:
                            successes.append(candidates[i])
                            break
                    data[coords[0][0] - 1][coords[1][0]] = '#'
                    n_rotations += 1
                    data = np.rot90(data)
                else:
                    position = data[coords[0][0] - 1][coords[1][0]]
                    data[coords[0][0]][coords[1][0]] = 'X'
                    data[coords[0][0] - 1][coords[1][0]] = '^'
        return len(successes)

    return get_output(data)


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
