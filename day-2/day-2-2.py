# https://adventofcode.com/2020/day/2


input_file = open('inputs/day-2.txt', 'r')
lines = input_file.readlines()


# lines = [
# 	'1-3 a: abcde',
# 	'1-3 b: cdefg',
# 	'2-9 c: ccccccccc'
# ]

valid_passwords = 0

for line in lines:

	password_policy = line
	password = password_policy.split(' ')[2]

	letter_appearance = password_policy.split(' ')[1].split(':')[0]

	occurence_first = int(password_policy.split(' ')[0].split('-')[0])
	occurence_second = int(password_policy.split(' ')[0].split('-')[1])

	if (password[occurence_first - 1]) == letter_appearance and password[occurence_second - 1] == letter_appearance:
		continue
	elif (password[occurence_first - 1]) == letter_appearance or password[occurence_second - 1] == letter_appearance:
		valid_passwords += 1

	# print(occurence_min)
	# print(occurence_max)
	
print(valid_passwords)
	
