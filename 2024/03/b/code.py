import pandas as pd
import os
import re


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/03/b'
os.chdir(dir)


### Develop solution

data_ex = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

last = 'do'
post = data_ex

while len(post) > 0:
pre  = re.findall(r".*don't\(\)", data_ex)
post = re.findall(r"don't\(\).*", data_ex)


def get_output(input):
    re.findall(r".*don't()", input)
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
