# TODO
def fold(line, lower, higher):
	# print(line)
	total_seats = 128
	lower = 0
	higher = 128
	for i in line[:7]:
		if i == 'F':
			higher = (lower + higher) // 2
		elif i == 'B':
			lower = (lower + higher) // 2

	print(lower, higher)
	if line[6] == 'F':
		print(lower)
	else:
		print(higher)

	
	exit()


with open('../inputs/day-5.txt') as f:
	for line in f:
		fold(line.strip())