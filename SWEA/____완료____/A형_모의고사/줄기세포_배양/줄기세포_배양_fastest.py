import sys
import timeit
import pprint

sys.stdin = open('줄기세포_배양.txt', 'r')

start_time = timeit.default_timer()

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

for testCase in range(int(input())):
	size_row, size_column, last_round = map(int, input().split())
	# 임시 저장 테이블
	_table = [list(map(int, input().split())) for _ in range(size_row)]
	# 생명력 수치 별 살아있는 줄기 세포 리스트
	cells = [[] for _ in range(11)]
	# 배양 용기 정보 (시간 last_round를 고려하여 확장)
	table = [[0 for __ in range(size_column + last_round)] for _ in range(size_row + last_round)]
	for y in range(size_row):
		for x in range(size_column):
			if _table[y][x]:
				# 확장된 부분을 고려하여 좌표 보정 (last_round // 2)
				table[y + last_round // 2][x + last_round // 2] = _table[y][x]
				cells[_table[y][x]].append((x + last_round // 2, y + last_round // 2, 0))
	for current_round in range(1, last_round + 1):
		# 같은 위치에 동시에 번식하려 할 때, 생명력 수치가 큰 세포로 확정해야함
		# 이 부분을 고려하여 생명력 수치가 큰 세포부터 검사
		for life in range(10, 0, -1):
			if cells[life]:
				new_cells = []
				for cell in cells[life]:
					x, y, birth_round = cell
					status = birth_round - current_round
					# status가 -life-1 일 때, 주변으로 번식
					if status == -life - 1:
						for dx, dy in directions:
							new_x = x + dx
							new_y = y + dy
							if not table[new_y][new_x]:
								table[new_y][new_x] = life
								new_cells.append((new_x, new_y, current_round))
						if life == 1:
							# 죽이기
							continue
					# status가 -life*2 일 때, 해당 세포 사멸
					elif status == -life * 2:
						# 죽이기
						continue
					# 특이점 없는 세포는 그대로 생존
					new_cells.append((x, y, birth_round))
				# 탐색 결과 반영
				cells[life] = new_cells
	# 살아 있는 세포 수 카운트
	ans = sum(len(cell_group) for cell_group in cells)
	print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 22
# 2 36
# 3 90
# 4 164
# 5 712
