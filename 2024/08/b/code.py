import numpy  as np
import pandas as pd
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/08/b'
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
            antennae = pd.DataFrame(np.where(input == frequencies[i])).transpose()
            antennae.columns = ['x', 'y']
            for j in range(len(antennae)):
                antenna = antennae.iloc[j]
                others  = antennae.drop(j)
                for k in range(len(others)):
                    antinodes.add(tuple([others.iloc[k]['x'], others.iloc[k]['y']]))
                    x = others.iloc[k]['x']
                    y = others.iloc[k]['y']
                    diff_x = x - antenna['x']
                    diff_y = y - antenna['y']
                    while (x >= 0) & (x < input.shape[0]) & (y >= 0) & (y < input.shape[1]):
                        x += diff_x
                        y += diff_y
                        if (x >= 0) & (x < input.shape[0]) & (y >= 0) & (y < input.shape[1]):
                            antinodes.add(tuple([x, y]))
    return len(antinodes)

get_output(data_ex)


### Create function

def main(data):
    data = data.splitlines()
    data = [list(x) for x in data]
    data = np.array(data)

    def get_output(input):
        frequencies = np.unique(input).tolist()
        antinodes   = set()
        for i in range(len(frequencies)):
            if frequencies[i] == '.':
                pass
            else:
                antennae = pd.DataFrame(np.where(input == frequencies[i])).transpose()
                antennae.columns = ['x', 'y']
                for j in range(len(antennae)):
                    antenna = antennae.iloc[j]
                    others  = antennae.drop(j)
                    for k in range(len(others)):
                        antinodes.add(tuple([others.iloc[k]['x'], others.iloc[k]['y']]))
                        x = others.iloc[k]['x']
                        y = others.iloc[k]['y']
                        diff_x = x - antenna['x']
                        diff_y = y - antenna['y']
                        while (x >= 0) & (x < input.shape[0]) & (y >= 0) & (y < input.shape[1]):
                            x += diff_x
                            y += diff_y
                            if (x >= 0) & (x < input.shape[0]) & (y >= 0) & (y < input.shape[1]):
                                antinodes.add(tuple([x, y]))
        return len(antinodes)

    return get_output(data)


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
