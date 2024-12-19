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

def get_output(input):
    position = '.'
    last_rotate = False
    n_rotations = 0
    obstacles = []
    while position != '0':
        print(input)
        coords = np.where(input == '^')
        if input[coords[0][0] - 1][coords[1][0]] == '#':
            last_rotate = True
            n_rotations += 1
            input = np.rot90(input)
        else:
            position = input[coords[0][0] - 1][coords[1][0]]
            if position == '1' or position == '2' or position == '3':
                pass
            else:
                if last_rotate == True:
                    if len(np.where(input == '3')[0]) != 0:
                        old_coords = np.where(input == '3')
                        input[old_coords[0][0]][old_coords[1][0]] = 'X'
                    if len(np.where(input == '2')[0]) != 0:
                        old_coords = np.where(input == '2')
                        input[old_coords[0][0]][old_coords[1][0]] = '3'
                    if len(np.where(input == '1')[0]) != 0:
                        old_coords = np.where(input == '1')
                        input[old_coords[0][0]][old_coords[1][0]] = '2'
                    input[coords[0][0]][coords[1][0]] = '1'
                    if len(np.where(input == '3')[0]) != 0:
                        if len(np.where(input == '4')[0]) != 0:
                            old_coords =  np.where(input == '4')
                            input[old_coords[0][0]][old_coords[1][0]] = '.'
                        if (input[np.where(input == '3')[0][0]][np.where(input == '1')[1][0]] != '#') & (np.where(input == '1')[1][0] != 1):
                            input[np.where(input == '3')[0][0]][np.where(input == '1')[1][0]] = '4'
                else:
                    input[coords[0][0]][coords[1][0]] = 'X'
            if input[coords[0][0] - 1][coords[1][0]] == '4':
                old_value = input[coords[0][0] - 2][coords[1][0]]
                input[coords[0][0] - 2][coords[1][0]] = 'O'
                if math.modf(n_rotations / 4)[0] == 0.25:
                    input = np.rot90(input)
                    input = np.rot90(input)
                    input = np.rot90(input)
                    obstacles.append(np.where(input == 'O'))
                    input = np.rot90(input)
                elif math.modf(n_rotations / 4)[0] == 0.50:
                    input = np.rot90(input)
                    input = np.rot90(input)
                    obstacles.append(np.where(input == 'O'))
                    input = np.rot90(input)
                    input = np.rot90(input)
                elif math.modf(n_rotations / 4)[0] == 0.75:
                    input = np.rot90(input)
                    obstacles.append(np.where(input == 'O'))
                    input = np.rot90(input)
                    input = np.rot90(input)
                    input = np.rot90(input)
                else:
                    obstacles.append(np.where(input == 'O'))
                print(input)
                print(obstacles)
                input[coords[0][0] - 2][coords[1][0]] = old_value
            input[coords[0][0] - 1][coords[1][0]] = '^'
            last_rotate = False
    return len(obstacles)

get_output(data_ex)


### Create function

def main(data):
    data = data.splitlines()
    data = [list(x) for x in data]
    data = np.array(data)
    data = np.pad(data, pad_width=1, mode='constant', constant_values=0)

    def get_output(input):
        position = '.'
        while position != '0':
            coords = np.where(input == '^')
            if input[coords[0][0] - 1][coords[1][0]] == '#' or input[coords[0][0] - 1][coords[1][0]] == '1' or input[coords[0][0] - 1][coords[1][0]] == '2' or input[coords[0][0] - 1][coords[1][0]] == '3':
                if len(np.where(input == '3')) != 0:
                    old_coords = np.where(input == '3')
                    input[old_coords[0][0]][old_coords[1][0]] = '#'
                if len(np.where(input == '2')) != 0:
                    old_coords = np.where(input == '2')
                    input[old_coords[0][0]][old_coords[1][0]] = '3'
                if len(np.where(input == '1')) != 0:
                    old_coords = np.where(input == '1')
                    input[old_coords[0][0]][old_coords[1][0]] = '2'
                input[coords[0][0] - 1][coords[1][0]] = '1'
                input = np.rot90(input)
            else:
                position = input[coords[0][0] - 1][coords[1][0]]
                input[coords[0][0]][coords[1][0]] = 'X'
                input[coords[0][0] - 1][coords[1][0]] = '^'
        return len(np.where(input == 'X')[0])

    return get_output(data)


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
