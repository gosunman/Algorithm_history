import sys
import timeit
import pprint

sys.stdin = open('줄기세포_배양.txt', 'r')

start_time = timeit.default_timer()

# 네 방향으로 확장시킬 때 쓸 리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 딕셔너리에 데이터를 대입할 때 쓸 함수
def write_info(x, y, life, current_life, database):
	if database.get(x):
		if database[x].get(y):
			if database[x][y][0] < life:
				database[x][y] = [life, current_life]
		else:
			database[x][y] = [life, current_life]
	else:
		database[x] = {y: [life, current_life]}


# 딕셔너리에서 데이터를 삭제할 때 쓸 함수
def erase_info(x, y, database):
	if len(database[x].keys()) == 1:
		del database[x]
	else:
		del database[x][y]


# 실제 시뮬레이션을 돌리는 함수
def run_simulation(test_group, exception_group):
	# test_group = info_cells # 비활성화 + 활성화 셀 정보 (죽은 셀은 제외됨)
	# exception_group = exception_cells # 이미 배양중인 셀의 위치 정보 (번식되어 나갈 수 없는 셀)
	add_candidates_info = {}  # 번식되어 나갈 셀 후보군 (생명력의 수치가 높은 아이를 선택하기 위함)
	del_candidates_info = {}  # test_group에서 죽은 셀을 제외하기 위한 후보군
	for x, temp in test_group.items():
		for y, info in temp.items():
			# 한 라운드가 지나면 생명력 수치(current_life)가 1 줄어들어야 한다.
			test_group[x][y][1] -= 1
			life, current_life = test_group[x][y]
			# current_life가 -1이 되는 순간 주변 셀로 번식되어 나간다
			if current_life == -1:
				for direction in range(4):
					new_x = x + dx[direction]
					new_y = y + dy[direction]
					if not exception_group.get(new_x):
						write_info(new_x, new_y, life, life, add_candidates_info)
						write_info(new_x, new_y, life, life, exception_group)
					else:
						if not exception_group[new_x].get(new_y):
							write_info(new_x, new_y, life, life, add_candidates_info)
							write_info(new_x, new_y, life, life, exception_group)
						else:
							if add_candidates_info.get(new_x):
								if add_candidates_info[new_x].get(new_y):
									write_info(new_x, new_y, life, life, add_candidates_info)
									write_info(new_x, new_y, life, life, exception_group)
			# current_life가 -life가 되는 순간 그 셀은 죽는다
			if current_life == -life:
				write_info(x, y, life, life, del_candidates_info)

	# 생명력의 수치가 높은 아이를 최종 선택하여 추가하는 작업
	for x, temp in add_candidates_info.items():
		for y, info in temp.items():
			write_info(x, y, info[0], info[0], test_group)

	# 죽어버린 셀을 제거하는 작업
	for x, temp in del_candidates_info.items():
		for y, info in temp.items():
			erase_info(x, y, test_group)


for testCase in range(int(input())):
	size_row, size_column, last_round = map(int, input().split())
	temp_table = [list(map(int, input().split())) for _ in range(size_row)]
	info_cells = {}  # 비활성화 + 활성화 셀 정보 (죽은 셀은 제외됨)
	exception_cells = {}  # 이미 배양중인 셀의 위치 정보 (번식되어 나갈 수 없는 셀)
	# 초기값 정리
	for y in range(size_row):
		for x in range(size_column):
			life = temp_table[y][x]
			if life:
				write_info(x, y, life, life, info_cells)
				write_info(x, y, life, life, exception_cells)
				
	# 시뮬레이션 반복 수행
	for _ in range(last_round):
		run_simulation(info_cells, exception_cells)

	# 살아있는 셀의 수를 카운트하는 작업
	ans = 0
	for x, temp in info_cells.items():
		for y, info in temp.items():
			ans += 1

	print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 22
# 2 36
# 3 90
# 4 164
# 5 712
