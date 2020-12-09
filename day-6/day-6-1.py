def yes_answers(line):
    return len(set(list(line)))


with open('../inputs/day-6.txt') as f:
    data = ''
    yes_count = 0
    for line in f:
        if line.strip().split('\n')[0] == '':
            yes_count += yes_answers(data.replace(' ', ''))
            data = ''
            continue
        data += line.replace('\n', ' ')

    print(yes_count)