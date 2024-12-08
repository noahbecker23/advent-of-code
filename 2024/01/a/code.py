import pandas as pd
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/01/a'
os.chdir(dir)


### Develop solution

data_ex = '''3   4
4   3
2   5
1   3
3   9
3   3'''

data_ex = data_ex.splitlines()
data_ex = pd.DataFrame(data_ex)
data_ex.columns = ['input']

def get_output(input):
    input[['a', 'b']] = input['input'].str.split(expand=True).astype(int)
    input['a_sorted'] = input['a'].sort_values().reset_index(drop=True)
    input['b_sorted'] = input['b'].sort_values().reset_index(drop=True)
    input['diff'] = abs(input['a_sorted'] - input['b_sorted'])
    return sum(input['diff'])

get_output(data_ex)


### Create function

def main(data):
    data = data.splitlines()
    data = pd.DataFrame(data)
    data.columns = ['input']

    def get_output(input):
        input[['a', 'b']] = input['input'].str.split(expand=True).astype(int)
        input['a_sorted'] = input['a'].sort_values().reset_index(drop=True)
        input['b_sorted'] = input['b'].sort_values().reset_index(drop=True)
        input['diff'] = abs(input['a_sorted'] - input['b_sorted'])
        return sum(input['diff'])

    return get_output(data)


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
