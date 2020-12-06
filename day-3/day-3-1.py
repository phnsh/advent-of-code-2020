f = open('../inputs/day-3.txt', 'r')
# lines = f.readlines()
# print(len(lines))
# print(lines[1])
# print(7 % 6)
# exit(0)
curr_pos = 0
counter = 0
line_len = len(lines[0].replace('\n', ''))
tree_counter = 0
# print(line_len)
for line in lines:
	# print(len(line.replace('\n', '')))
	# print(curr_pos)
	if line[curr_pos] == '#':
		tree_counter += 1
	counter += 3
	curr_pos = counter % line_len

print(tree_counter)