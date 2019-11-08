import sys
import timeit
import pprint

sys.stdin = open('프로세서_연결하기', 'r')

start_time = timeit.default_timer()

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 딕셔너리에 추가하기
def _add(x, y, database):
    if database.get(x):
        if y not in database[x]:
            database[x].append(y)
    else:
        database[x] = [y]


# 딕셔너리 삭제하기
def _remove(x, y, database):
    if len(database[x]) == 1:
        del database[x]
    else:
        database[x].remove(y)


# 해당 위치에 전선이나 코어가 이미 존재하는 지 확인하기
def check(x, y, exception):
    global size_table
    if exception.get(x):
        if y in exception[x]:
            return False
        else:
            return True
    else:
        return True


# 재귀함수, depth는 현재 고려중인 코어의 인덱스, limit은 고려해야할 코어의 총 개수,
# cnt는 전원에 연결된 코어의 개수, exception은 전선이나 코어가 위치한 좌표의 모음
def solution(depth, limit, cnt, exception):
    global cores, count, wire_length, size_table
    if depth != limit:
        # 백트래킹: 이후의 모든 코어를 연결해도 이미 구한 최대값보다 작다면 탐색 중지
        if cnt + limit - depth >= count:
            x, y = cores[depth]
            # 해당 코어를 연결한다고 가정할 시, 네 방향으로 탐색하여 가능한 경우인지 파악
            for direction in range(4):
                dx, dy = move[direction]
                step = 1
                isGood = True
				# 연결하려는 방향으로 전선을 기록해두는 작업
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
				# 만약 연결이 되었다면, 다음번 탐색을 진행한다.
                if isGood:
                    solution(depth + 1, limit, cnt + 1, exception)
                # 다른 방향으로 탐색을 수행하기 전에, 이번 방향으로 연결했던 전선을 삭제하는 작업
				# 기존 기록 지우기
                temp_step = 1
                while temp_step < step:
                    new_x, new_y = x + dx * temp_step, y + dy * temp_step
                    _remove(new_x, new_y, exception)
                    temp_step += 1
            # 해당 코어를 전원에 연결하지 않는 경우
            solution(depth + 1, limit, cnt, exception)

    else:
		# 연결된 코어수가 많다면 기록
        if count < cnt:
            count = cnt
            wire_length = sum([len(_) for _ in exception.values()])
		# 연결된 코어수가 같다면, 전선이 절약된 경우에만 기록
        elif count == cnt:
            temp = sum([len(_) for _ in exception.values()])
            if wire_length > temp:
                wire_length = temp


for testCase in range(int(input())):
    size_table = int(input())
    table = [list(map(int, input().split())) for _ in range(size_table)]
	# 벽에 붙어 있는 코어는 굳이 고려할 필요가 없기 때문에, 해당 코어를 제외한 코어의 좌표 목록
    cores = []
	# 코어와 전선이 위치한 경우들을 표시하여 기록한 딕셔너리
    block = {}
	# 코어의 개수
    existing_core = 0
    count = wire_length = 0
    for y in range(size_table):
        for x in range(size_table):
            if table[y][x]:
                _add(x, y, block)
                existing_core += 1
                if x not in [0, size_table - 1] and y not in [0, size_table - 1]:
                    cores.append([x, y])
    solution(0, len(cores), 0, block)
	# 정답은 block의 요소 개수(전선+코어)에서 코어의 개수(existing_core)를 빼 구한다.
    print("#{} {}".format(testCase + 1, wire_length - existing_core))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 12
# 2 10
# 3 24
