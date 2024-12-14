import numpy as np
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/04/a'
os.chdir(dir)


### Develop solution

data_ex = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

data_ex = data_ex.splitlines()
data_ex = [list(x) for x in data_ex]
data_ex = np.array(data_ex)

def get_output(input):
    solutions = set()
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if input[i,j] == 'X':
                # Up
                if i >= 3:
                    if (input[i-1,j] == 'M') & (input[i-2,j] == 'A') & (input[i-3,j] == 'S'):
                        solutions.add(str([i-3,j])+str([i-2,j])+str([i-1,j])+str([i,j]))
                    # Up-Left
                    if j >= 3:
                        if (input[i-1,j-1] == 'M') & (input[i-2,j-2] == 'A') & (input[i-3,j-3] == 'S'):
                            solutions.add(str([i-3,j-3])+str([i-2,j-2])+str([i-1,j-1])+str([i,j]))
                    # Up-Right
                    if input.shape[1] - 1 >= j + 3:
                        if (input[i-1,j+1] == 'M') & (input[i-2,j+2] == 'A') & (input[i-3,j+3] == 'S'):
                            solutions.add(str([i-3,j+3])+str([i-2,j+2])+str([i-1,j+1])+str([i,j]))
                # Down
                if input.shape[0] - 1 >= i + 3:
                    if (input[i+1,j] == 'M') & (input[i+2,j] == 'A') & (input[i+3,j] == 'S'):
                        solutions.add(str([i,j])+str([i+1,j])+str([i+2,j])+str([i+3,j]))
                    # Down-Left
                    if j >= 3:
                        if (input[i+1,j-1] == 'M') & (input[i+2,j-2] == 'A') & (input[i+3,j-3] == 'S'):
                            solutions.add(str([i,j])+str([i+1,j-1])+str([i+2,j-2])+str([i+3,j-3]))
                    # Down-Right
                    if input.shape[1] - 1 >= j + 3:
                        if (input[i+1,j+1] == 'M') & (input[i+2,j+2] == 'A') & (input[i+3,j+3] == 'S'):
                            solutions.add(str([i,j])+str([i+1,j+1])+str([i+2,j+2])+str([i+3,j+3]))
                # Left
                if j >= 3:
                    if (input[i,j-1] == 'M') & (input[i,j-2] == 'A') & (input[i,j-3] == 'S'):
                        solutions.add(str([i,j-3])+str([i,j-2])+str([i,j-1])+str([i,j]))
                # Right
                if input.shape[1] - 1 >= j + 3:
                    if (input[i,j+1] == 'M') & (input[i,j+2] == 'A') & (input[i,j+3] == 'S'):
                        solutions.add(str([i,j])+str([i,j+1])+str([i,j+2])+str([i,j+3]))
    return len(solutions)

get_output(data_ex)


### Create function

def main(data):
    data = data.splitlines()
    data = [list(x) for x in data]
    data = np.array(data)

    def get_output(input):
        solutions = set()
        for i in range(input.shape[0]):
            for j in range(input.shape[1]):
                if input[i,j] == 'X':
                    # Up
                    if i >= 3:
                        if (input[i-1,j] == 'M') & (input[i-2,j] == 'A') & (input[i-3,j] == 'S'):
                            solutions.add(str([i-3,j])+str([i-2,j])+str([i-1,j])+str([i,j]))
                        # Up-Left
                        if j >= 3:
                            if (input[i-1,j-1] == 'M') & (input[i-2,j-2] == 'A') & (input[i-3,j-3] == 'S'):
                                solutions.add(str([i-3,j-3])+str([i-2,j-2])+str([i-1,j-1])+str([i,j]))
                        # Up-Right
                        if input.shape[1] - 1 >= j + 3:
                            if (input[i-1,j+1] == 'M') & (input[i-2,j+2] == 'A') & (input[i-3,j+3] == 'S'):
                                solutions.add(str([i-3,j+3])+str([i-2,j+2])+str([i-1,j+1])+str([i,j]))
                    # Down
                    if input.shape[0] - 1 >= i + 3:
                        if (input[i+1,j] == 'M') & (input[i+2,j] == 'A') & (input[i+3,j] == 'S'):
                            solutions.add(str([i,j])+str([i+1,j])+str([i+2,j])+str([i+3,j]))
                        # Down-Left
                        if j >= 3:
                            if (input[i+1,j-1] == 'M') & (input[i+2,j-2] == 'A') & (input[i+3,j-3] == 'S'):
                                solutions.add(str([i,j])+str([i+1,j-1])+str([i+2,j-2])+str([i+3,j-3]))
                        # Down-Right
                        if input.shape[1] - 1 >= j + 3:
                            if (input[i+1,j+1] == 'M') & (input[i+2,j+2] == 'A') & (input[i+3,j+3] == 'S'):
                                solutions.add(str([i,j])+str([i+1,j+1])+str([i+2,j+2])+str([i+3,j+3]))
                    # Left
                    if j >= 3:
                        if (input[i,j-1] == 'M') & (input[i,j-2] == 'A') & (input[i,j-3] == 'S'):
                            solutions.add(str([i,j-3])+str([i,j-2])+str([i,j-1])+str([i,j]))
                    # Right
                    if input.shape[1] - 1 >= j + 3:
                        if (input[i,j+1] == 'M') & (input[i,j+2] == 'A') & (input[i,j+3] == 'S'):
                            solutions.add(str([i,j])+str([i,j+1])+str([i,j+2])+str([i,j+3]))
        return len(solutions)

    return get_output(data)


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
