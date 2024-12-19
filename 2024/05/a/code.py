import pandas as pd
import math
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/05/a'
os.chdir(dir)


### Develop solution

data_ex = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

data_ex = data_ex.splitlines()

rules   = data_ex[0                     : data_ex.index('')]
data_ex = data_ex[data_ex.index('') + 1 :                  ]

rules = pd.DataFrame(rules)
rules.columns = ['input']
rules[['number', 'before']] = rules['input'].str.split('|', expand=True).astype(int)

data_ex = pd.DataFrame(data_ex)
data_ex.columns = ['input']

def get_output(input):
    numbers = input.split(',')
    numbers = [int(x) for x in numbers]
    for i in range(len(numbers)):
        if sum(rules['number'] == numbers[i]) == 0:
            pass
        else:
            check = list(rules[rules['number'] == numbers[i]]['before'])
            for j in range(len(check)):
                if check[j] in numbers:
                    index = numbers.index(check[j])
                    if i > index:
                        return False
                    else:
                        pass
                else:
                    pass
    return True

data_ex['output'] = data_ex['input'].apply(get_output)
data_ex = data_ex[data_ex['output'] == True]

def find_middle(input):
    numbers = input.split(',')
    numbers = [int(x) for x in numbers]
    return numbers[math.floor(len(numbers) / 2)]

data_ex['middle'] = data_ex['input'].apply(find_middle)

sum(data_ex['middle'])


### Create function

def main(data):
    data = data.splitlines()

    rules = data[0                  : data.index('')]
    data  = data[data.index('') + 1 :               ]

    rules = pd.DataFrame(rules)
    rules.columns = ['input']
    rules[['number', 'before']] = rules['input'].str.split('|', expand=True).astype(int)

    data = pd.DataFrame(data)
    data.columns = ['input']

    def get_output(input):
        numbers = input.split(',')
        numbers = [int(x) for x in numbers]
        for i in range(len(numbers)):
            if sum(rules['number'] == numbers[i]) == 0:
                pass
            else:
                check = list(rules[rules['number'] == numbers[i]]['before'])
                for j in range(len(check)):
                    if check[j] in numbers:
                        index = numbers.index(check[j])
                        if i > index:
                            return False
                        else:
                            pass
                    else:
                        pass
        return True

    data['output'] = data['input'].apply(get_output)
    data = data[data['output'] == True]

    def find_middle(input):
        numbers = input.split(',')
        numbers = [int(x) for x in numbers]
        return numbers[math.floor(len(numbers) / 2)]

    data['middle'] = data['input'].apply(find_middle)

    return sum(data['middle'])


### Read in input

with open('input.txt', 'r') as file:
    data = file.read()


### Generate output

output = main(data)


### Write output to file

with open('output.txt', 'w') as file:
    file.write(str(output))
