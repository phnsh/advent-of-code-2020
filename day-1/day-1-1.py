# https://adventofcode.com/2020/day/1

input_file = open('inputs/day-1.txt', 'r')
nums = input_file.readlines()
# nums = [1721,979,366,299,675,1456]
# print(nums)

counter = 0
for i in nums:
    for j in nums[counter + 1:]:
        if (i + j) == 2020:
            print(i * j)
            break
    counter += 1
