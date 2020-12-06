# https://adventofcode.com/2020/day/2

input_file = open('../inputs/day-2.txt', 'r')
lines = input_file.readlines()

valid_passwords = 0

for line in lines:

    password_policy = line
    password = password_policy.split(' ')[2]

    letter_appearance = password_policy.split(' ')[1].split(':')[0]

    occurence_min = int(password_policy.split(' ')[0].split('-')[0])
    occurence_max = int(password_policy.split(' ')[0].split('-')[1])

    # print(occurence_min)
    # print(occurence_max)

    if occurence_min <= password.count(letter_appearance) <= occurence_max:
        valid_passwords += 1

print(valid_passwords)