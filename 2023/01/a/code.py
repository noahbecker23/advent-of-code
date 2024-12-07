import pandas as pd
import re
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2023/01/a'
os.chdir(dir)


### Develop solution

data_ex = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

data_ex = data_ex.splitlines()
data_ex = pd.DataFrame(data_ex)
data_ex.columns = ['input']

def get_output(input):
    output = re.sub(r'[^0-9]', '', input)
    output = str(output[0]) + str(output[len(output) - 1])
    output = int(output)
    return output

data_ex['output'] = data_ex['input'].apply(get_output)

sum(data_ex['output'])


### Create function

def main(data):
    data = data.splitlines()
    data = pd.DataFrame(data)
    data.columns = ['input']

    def get_output(input):
        output = re.sub(r'[^0-9]', '', input)
        output = str(output[0]) + str(output[len(output) - 1])
        output = int(output)
        return output

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
