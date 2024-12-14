import pandas as pd
import os
import re


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/03/a'
os.chdir(dir)


### Develop solution

data_ex = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

data_ex = data_ex.splitlines()
data_ex = pd.DataFrame(data_ex)
data_ex.columns = ['input']

def get_output(input):
    data = pd.DataFrame(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input))
    data.columns = ['match']
    data['match']    = data['match'].str.replace('mul\(', '', regex=True)
    data['match']    = data['match'].str.replace('\)'   , '', regex=True)
    data[['a', 'b']] = data['match'].str.split(',', expand=True).astype(int)
    data['c']        = data['a'] * data['b']
    return sum(data['c'])

data_ex['output'] = data_ex['input'].apply(get_output)

sum(data_ex['output'])


### Create function

def main(data):
    data = data.splitlines()
    data = pd.DataFrame(data)
    data.columns = ['input']

    def get_output(input):
        data = pd.DataFrame(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input))
        data.columns = ['match']
        data['match']    = data['match'].str.replace('mul\(', '', regex=True)
        data['match']    = data['match'].str.replace('\)'   , '', regex=True)
        data[['a', 'b']] = data['match'].str.split(',', expand=True).astype(int)
        data['c']        = data['a'] * data['b']
        return sum(data['c'])

    data['output'] = data['input'].apply(get_output)

    return sum(data['output'])


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
