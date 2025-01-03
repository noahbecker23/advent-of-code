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
            antennae = pd.DataFrame(np.where(input == frequencies[i])).transpose()
            antennae.columns = ['x', 'y']
            for j in range(len(antennae)):
                antenna = antennae.iloc[j]
                others  = antennae.drop(j)
                others['prev_x'] = antenna['x']
                others['prev_y'] = antenna['y']
                others['diff_x'] = others['x'] - others['prev_x']
                others['diff_y'] = others['y'] - others['prev_y']
                others['antinode_x'] = others['x'] + others['diff_x']
                others['antinode_y'] = others['y'] + others['diff_y']
                for k in range(len(others)):
                    if (others.iloc[k]['antinode_x'] >= 0) & (others.iloc[k]['antinode_x'] < input.shape[0]) & (others.iloc[k]['antinode_y'] >= 0) & (others.iloc[k]['antinode_y'] < input.shape[1]):
                        antinodes.add(tuple([others.iloc[k]['antinode_x'], others.iloc[k]['antinode_y']]))
                    else:
                        pass
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
                    others['prev_x'] = antenna['x']
                    others['prev_y'] = antenna['y']
                    others['diff_x'] = others['x'] - others['prev_x']
                    others['diff_y'] = others['y'] - others['prev_y']
                    others['antinode_x'] = others['x'] + others['diff_x']
                    others['antinode_y'] = others['y'] + others['diff_y']
                    for k in range(len(others)):
                        if (others.iloc[k]['antinode_x'] >= 0) & (others.iloc[k]['antinode_x'] < input.shape[0]) & (others.iloc[k]['antinode_y'] >= 0) & (others.iloc[k]['antinode_y'] < input.shape[1]):
                            antinodes.add(tuple([others.iloc[k]['antinode_x'], others.iloc[k]['antinode_y']]))
                        else:
                            pass
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
