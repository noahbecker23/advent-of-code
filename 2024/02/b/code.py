import pandas as pd
import os


### Change output directory

dir = 'Z:/Learning/Advent of Code/2024/02/b'
os.chdir(dir)


### Develop solution

data_ex = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

data_ex = data_ex.splitlines()
data_ex = pd.DataFrame(data_ex)
data_ex.columns = ['input']

def get_output(input):
    data = input.split()
    data = [int(x) for x in data]
    data = [data]
    for i in range(len(data[0])):
        new_row = data[0][slice(len(data[0]))]
        new_row.pop(i)
        data.append(new_row)
    pass_count = 0
    for j in range(len(data)):
        if pass_count > 0:
            break
        fail_count = 0
        for i in range(len(data[j])):
            if i == 0:
                prev = data[j][i]
            else:
                curr = data[j][i]
                diff = curr - prev
                if   diff > 0:
                    curr_dir = '+'
                elif diff < 0:
                    curr_dir = '-'
                else:
                    curr_dir = '~'
                if i == 1:
                    prev_dir = curr_dir
                if abs(diff) > 3 or curr_dir == '~' or curr_dir != prev_dir:
                    fail_count += 1
                prev     = curr
                prev_dir = curr_dir
        if fail_count == 0:
            pass_count += 1
    if pass_count > 0:
        output = 1
    else:
        output = 0
    return output

data_ex['output'] = data_ex['input'].apply(get_output)

sum(data_ex['output'])


### Create function

def main(data):
    data = data.splitlines()
    data = pd.DataFrame(data)
    data.columns = ['input']

    def get_output(input):
        data = input.split()
        data = [int(x) for x in data]
        data = [data]
        for i in range(len(data[0])):
            new_row = data[0][slice(len(data[0]))]
            new_row.pop(i)
            data.append(new_row)
        pass_count = 0
        for j in range(len(data)):
            if pass_count > 0:
                break
            fail_count = 0
            for i in range(len(data[j])):
                if i == 0:
                    prev = data[j][i]
                else:
                    curr = data[j][i]
                    diff = curr - prev
                    if   diff > 0:
                        curr_dir = '+'
                    elif diff < 0:
                        curr_dir = '-'
                    else:
                        curr_dir = '~'
                    if i == 1:
                        prev_dir = curr_dir
                    if abs(diff) > 3 or curr_dir == '~' or curr_dir != prev_dir:
                        fail_count += 1
                    prev     = curr
                    prev_dir = curr_dir
            if fail_count == 0:
                pass_count += 1
        if pass_count > 0:
            output = 1
        else:
            output = 0
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