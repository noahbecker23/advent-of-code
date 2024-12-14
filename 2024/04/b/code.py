import numpy as np
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/04/b'
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
            if (input[i,j] == 'A') & (i >= 1) & (j >= 1) & (input.shape[0] - 1 >= i + 1) & (input.shape[1] - 1 >= j + 1):
                if (((input[i-1,j-1] == 'M') & (input[i+1,j+1] == 'S')) | ((input[i-1,j-1] == 'S') & (input[i+1,j+1] == 'M'))) & (((input[i-1,j+1] == 'M') & (input[i+1,j-1] == 'S')) | ((input[i-1,j+1] == 'S') & (input[i+1,j-1] == 'M'))):
                    solutions.add(str([i,j]))
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
                if (input[i,j] == 'A') & (i >= 1) & (j >= 1) & (input.shape[0] - 1 >= i + 1) & (input.shape[1] - 1 >= j + 1):
                    if (((input[i-1,j-1] == 'M') & (input[i+1,j+1] == 'S')) | ((input[i-1,j-1] == 'S') & (input[i+1,j+1] == 'M'))) & (((input[i-1,j+1] == 'M') & (input[i+1,j-1] == 'S')) | ((input[i-1,j+1] == 'S') & (input[i+1,j-1] == 'M'))):
                        solutions.add(str([i,j]))
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
