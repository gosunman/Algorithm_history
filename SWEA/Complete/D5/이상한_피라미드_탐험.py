import sys
import timeit
import pprint

sys.stdin = open('이상한_피라미드_탐험', 'r')

start_time = timeit.default_timer()

indexes = []

for index in range(1, 142):
	indexes.append(index * (index + 1) // 2)


def find_coord(target):
	y = 0
	x = 0
	for index in range(141):
		if target <= indexes[index]:
			y = index
			x = ((index+1)//2 - 0.5 if index % 2 else index//2) - (indexes[index] - target)
			break
	return x, y


for testCase in range(int(input())):
	start, end = map(int, input().split())
	start_x, start_y = find_coord(start)
	end_x, end_y = find_coord(end)
	go_y = abs(end_y - start_y)
	go_x = int(abs(end_x - start_x))
	# print(start, start_x, start_y)
	# print(end, end_x, end_y)
	ans = 0
	if go_x >= go_y//2:
		ans = go_y + go_x - (go_y//2)
	else:
		ans = go_y
	print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 0
# 3 31
