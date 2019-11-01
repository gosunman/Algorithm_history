import sys
import timeit
import pprint

sys.stdin = open('분수_스도쿠', 'r')

start_time = timeit.default_timer()


#분자에는 9가 들어갈 수 없고
#분모에는 1이 들어갈 수 없다

def solution(x, y):
	global ans_table
	candidates = list(map(str, range(1, 10)))
	target_count = ans_table[y][x].count('-')
	current_count = 9
	row = list(range(6))
	column = list(range(6))
	group = list(range(6))
	for _ in range(6):
		for element in ans_table[y][_]:
			if element in candidates:
				candidates.remove(element)
				current_count -= 1
				if current_count == target_count:
					break
		if current_count == target_count:
			break
		for element in ans_table[_][x]:
			if element in candidates:
				candidates.remove(element)
				current_count -= 1
				if current_count == target_count:
					break
		if current_count == target_count:
			break
	if current_count != target_count:
		pivot_x, pivot_y = x // 3, y // 2
		pivot_x *= 3
		pivot_y *= 2
		for new_x in range(3):
			for new_y in range(2):
				for element in ans_table[pivot_y + new_y][pivot_x + new_x]:
					if element in candidates:
						candidates.remove(element)
						current_count -= 1
						if current_count == target_count:
							break
				if current_count == target_count:
					break
			if current_count == target_count:
				break
	if current_count == target_count:
		if target_count == 2:
			candidates.sort()
			ans_table[y][x] = ans_table[y][x].replace('-', candidates[0], 1)
			ans_table[y][x] = ans_table[y][x].replace('-', candidates[1], 1)
			return True
		else:
			ans_table[y][x] = ans_table[y][x].replace('-', candidates[0], 1)
			return True
	else:
		if target_count == 1 and '/' in ans_table[y][x]:
			if ans_table[y][x].index('-') == 0:
				if candidates[0] < ans_table[y][x][2] < candidates[1]:
					ans_table[y][x] = ans_table[y][x].replace('-', candidates[0], 1)
					return True
			else:
				if candidates[-1] > ans_table[y][x][0] > candidates[-2]:
					ans_table[y][x] = ans_table[y][x].replace('-', candidates[-1], 1)
					return True


for testCase in range(int(input())):
	ans_table = [input().split() for _ in range(6)]
	incomplete = True
	while incomplete:
		incomplete = False
		for y in range(6):
			for x in range(6):
				if '-' in ans_table[y][x]:
					incomplete = True
					solution(x, y)

	print("#{}".format(testCase + 1))
	for _ in range(6):
		print(" ".join(ans_table[_]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# #1
# 7/9 1/5 4 3 2 6/8
# 3 6 2/8 1/9 7 4/5
# 1 7/9 3 4/5 6/8 2
# 8 2/4 5/6 7 1/3 9
# 5/6 3 1/9 2/8 4 7
# 2/4 8 7 6 5/9 1/3
# #2
# 2 6/9 4/8 1/5 3 7
# 1/7 3 5 2 4/8 6/9
# 6/9 8 7 3 2/5 1/4
# 3 4/5 1/2 6/9 7 8
# 5 2/7 6/9 4/8 1 3
# 4/8 1 3 7 6/9 2/5
