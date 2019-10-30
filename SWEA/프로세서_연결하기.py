import sys
import timeit
import pprint

sys.stdin = open('프로세서_연결하기', 'r')

start_time = timeit.default_timer()

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def _add(x, y, database):
	if database.get(x):
		if y in database[x]:
			return False
		else:
			database[x].append(y)
	else:
		database[x] = [y]


def _remove(x, y, database):
	if len(database[x]) == 1:
		del database[x]
	else:
		database[x].remove(y)


def check(x, y, exception):
	global size_table
	if exception.get(x):
		if y in exception[x]:
			return False
		else:
			return True
	else:
		return True


def solution(depth, limit, cnt, exception):
	global cores, count, wire_length, size_table
	if depth != limit:
		# 백트래킹 넣기 이후꺼 다 합산해도 안되는 경우는 종료
		x, y = cores[depth]
		for direction in range(4):
			dx, dy = move[direction]
			step = 1
			isGood = True
			while True:
				new_x, new_y = x + dx * step, y + dy * step
				if 0 <= new_x < size_table and 0 <= new_y < size_table:
					if check(new_x, new_y, exception):
						_add(new_x, new_y, exception)
						step += 1
					else:
						isGood = False
						break
				else:
					break
			if isGood:
				solution(depth + 1, limit, cnt + 1, exception)
			# 기존 기록 지우기
			temp_step = 1
			while temp_step < step:
				new_x, new_y = x + dx * temp_step, y + dy * temp_step
				_remove(new_x, new_y, exception)
				temp_step += 1
		solution(depth + 1, limit, cnt, exception)
	else:
		if count < cnt:
			count = cnt
			wire_length = sum([len(_) for _ in exception.values()])
		elif count == cnt:
			temp = sum([len(_) for _ in exception.values()])
			if wire_length < temp:
				wire_length = temp


for testCase in range(int(input())):
	size_table = int(input())
	table = [list(map(int, input().split())) for _ in range(size_table)]
	cores = []
	block = {}
	count = wire_length = 0
	for y in range(size_table):
		for x in range(size_table):
			if table[y][x]:
				_add(x, y, block)
				wire_length -= 1
				if x not in [0, size_table - 1] and y not in [0, size_table - 1]:
					cores.append([x, y])
	solution(0, len(cores), 0, block)
	print("#{} {}".format(testCase + 1, wire_length))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 12
# 2 10
# 3 24
