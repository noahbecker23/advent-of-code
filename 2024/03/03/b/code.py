import pandas as pd
import os
import re


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/03/b'
os.chdir(dir)


### Develop solution

data_ex = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

def get_output(input):
    last = 'do'
    post = input.replace('\n', '')
    keepers = []
    while len(post) > 0:
        if last == 'do':
            if len(re.findall(r".*don't\(\)", post)) > 0:
                pre  = post.split("don't()", 1)[ 0]
                post = post.split("don't()", 1)[-1]
            else:
                pre = post
                post = ''
            keepers.append(pre)
            last = "don't"
        if last == "don't":
            if len(re.findall(r".*do\(\)", post)) > 0:
                pre  = post.split("do()", 1)[ 0]
                post = post.split("do()", 1)[-1]
            else:
                post = ''
            last = 'do'
    data = pd.DataFrame(keepers)
    data.columns = ['match']
    data = data['match'].str.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)')
    data = pd.DataFrame(data.explode())
    data['match']    = data['match'].str.replace('mul\(', '', regex=True)
    data['match']    = data['match'].str.replace('\)'   , '', regex=True)
    data[['a', 'b']] = data['match'].str.split(',', expand=True).astype(int)
    data['c']        = data['a'] * data['b']
    return sum(data['c'])

get_output(data_ex)


### Create function

def main(data):
    last = 'do'
    post = data.replace('\n', '')
    keepers = []
    while len(post) > 0:
        if last == 'do':
            if len(re.findall(r".*don't\(\)", post)) > 0:
                pre  = post.split("don't()", 1)[ 0]
                post = post.split("don't()", 1)[-1]
            else:
                pre = post
                post = ''
            keepers.append(pre)
            last = "don't"
        if last == "don't":
            if len(re.findall(r".*do\(\)", post)) > 0:
                pre  = post.split("do()", 1)[ 0]
                post = post.split("do()", 1)[-1]
            else:
                post = ''
            last = 'do'
    data = pd.DataFrame(keepers)
    data.columns = ['match']
    data = data['match'].str.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)')
    data = pd.DataFrame(data.explode())
    data['match']    = data['match'].str.replace('mul\(', '', regex=True)
    data['match']    = data['match'].str.replace('\)'   , '', regex=True)
    data[['a', 'b']] = data['match'].str.split(',', expand=True).astype(int)
    data['c']        = data['a'] * data['b']
    return sum(data['c'])


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
