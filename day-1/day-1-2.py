# https://adventofcode.com/2020/day/1

input_file = open('inputs/day-1.txt', 'r')
nums = input_file.readlines()# print(nums[-3:])
# nums = [1721,979,366,299,675,1456]
# print(nums)
pair_counter = 0
first_sums = []

counter = 0

inner_counter = 2
for i in nums:
    for j in nums[counter + 1:]:
        for k in nums[inner_counter:]:
            i = int(i)
            j = int(j)
            k = int(k)
            if (i + j + k) == 2020:
                print(i, '+', j, '+', k, '=', (i + j + k))
                print(i, '*', j, '*', k, '=', (i * j * k))
        inner_counter += 1
    counter += 1
    inner_counter = 2 + counter

