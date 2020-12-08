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
    seat_set = {1,2,4,6}
    diff = 0
    for line in f:
        seat_set.add(fold(line.strip()))
    for i in seat_set:
        temp = i - diff
        if temp > 1:
            print(i, ": ", temp)
        diff = i