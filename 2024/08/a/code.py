import numpy  as np
import pandas as pd
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/08/a'
os.chdir(dir)


### Develop solution

data_ex = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

data_ex = data_ex.splitlines()
data_ex = [list(x) for x in data_ex]
data_ex = np.array(data_ex)

def get_output(input):
    frequencies = np.unique(input).tolist()
    antinodes   = set()
    for i in range(len(frequencies)):
        if frequencies[i] == '.':
            pass
        else:
            antennae = np.where(input == frequencies[i])
    return

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
            if input[coords[0][0] - 1][coords[1][0]] == '#':
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
