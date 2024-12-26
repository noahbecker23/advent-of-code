import numpy     as np
import pandas    as pd
import itertools
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/07/b'
os.chdir(dir)


### Develop solution

data_ex = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

data_ex = data_ex.splitlines()
data_ex = pd.DataFrame(data_ex)
data_ex.columns = ['input']
data_ex[['final', 'numbers']] = data_ex['input'].str.split(': ', expand=True)
data_ex['final'] = data_ex['final'].astype(np.int64)

def get_output(input):
    final      = np.int64(input.split(': ')[0])
    numbers    = input.split(': ')[1].split()
    numbers    = [np.int64(x) for x in numbers]
    operations = list(itertools.product(['+', '*', '||'], repeat=len(numbers) - 1))
    for i in range(len(operations)):
        calc = numbers[0]
        for j in range(len(operations[i])):
            if operations[i][j] == '+':
                calc = calc + numbers[j + 1]
            if operations[i][j] == '*':
                calc = calc * numbers[j + 1]
            if operations[i][j] == '||':
                calc = np.int64(str(calc) + str(numbers[j + 1]))
            if calc > final:
                break
        if calc == final:
            return True
    return False

data_ex['output'] = data_ex['input'].apply(get_output)

sum(data_ex[data_ex['output']]['final'])


### Create function

def main(data):
    data = data.splitlines()
    data = pd.DataFrame(data)
    data.columns = ['input']
    data[['final', 'numbers']] = data['input'].str.split(': ', expand=True)
    data['final'] = data['final'].astype(np.int64)

    def get_output(input):
        final      = np.int64(input.split(': ')[0])
        numbers    = input.split(': ')[1].split()
        numbers    = [np.int64(x) for x in numbers]
        operations = list(itertools.product(['+', '*', '||'], repeat=len(numbers) - 1))
        for i in range(len(operations)):
            calc = numbers[0]
            for j in range(len(operations[i])):
                if operations[i][j] == '+':
                    calc = calc + numbers[j + 1]
                if operations[i][j] == '*':
                    calc = calc * numbers[j + 1]
                if operations[i][j] == '||':
                    calc = np.int64(str(calc) + str(numbers[j + 1]))
                if calc > final:
                    break
            if calc == final:
                return True
        return False

    data['output'] = data['input'].apply(get_output)

    return sum(data[data['output']]['final'])


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
