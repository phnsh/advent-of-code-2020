from functools import reduce

def yes_answers(line):
    temp = line.rstrip().split(' ')
    return len(reduce(set.intersection, map(set, temp)))


with open('../inputs/day-6.txt') as f:
    data = ''
    yes_count = 0
    for line in f:
        if line.strip().split('\n')[0] == '':
            yes_count += yes_answers(data)
            data = ''
            continue
        data += line.replace('\n', ' ')

    print(yes_count)