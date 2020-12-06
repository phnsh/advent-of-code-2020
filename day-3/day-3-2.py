# terrain = '1'
terrain = '012345678'

f = open('../inputs/day-3.txt', 'r')
lines = f.readlines()

def get_trees(r, d):
	f = open('../inputs/day-3.txt', 'r')
	lines = f.readlines()

	curr_pos = 0
	counter = 0

	right = r
	down = d

	line_len = len(lines[0].replace('\n', ''))
	tree_counter = 0

	for line in lines[::down]:
		if line[curr_pos] == '#':
			tree_counter += 1
		counter += right
		curr_pos = counter % line_len

	print(tree_counter)

	return tree_counter


directions = [(1,1), (3,1), (5,1), (7,1), (1,2)]
product = 1

for i in directions:
	product *= get_trees(i[0], i[1])

print(product)