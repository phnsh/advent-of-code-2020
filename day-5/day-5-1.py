# TODO
def fold(line):
    # print(line)
    total_seats = 128
    lower = 0
    higher = 128
    row = 0
    column = 0
    for i in line[:7]:
        if i == 'F':
            higher = (lower + higher) // 2
            row = higher - 1
        elif i == 'B':
            lower = (lower + higher) // 2
            row = lower

    total_seats = 8
    lower = 0
    higher = 8
    for i in line[-3:]:
        if i == 'L':
            higher = (lower + higher) // 2
            column = higher - 1
        elif i == 'R':
            lower = (lower + higher) // 2
            column = lower
    return (row * 8) + column

with open('../inputs/day-5.txt') as f:
    highest_id = 0
    for line in f:
        id = fold(line.strip())
        if id > highest_id:
            highest_id = id
    print('highest id:', highest_id)