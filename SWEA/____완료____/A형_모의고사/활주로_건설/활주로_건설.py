import sys
import timeit
import pprint

sys.stdin = open('활주로_건설.txt', 'r')

start_time = timeit.default_timer()


def solution(road, chance, road_length):

	# 현재 높이와 바로 전 높이를 비교하므로 인덱스는 1부터 시작한다.
	index = 1

	# 이미 활주로를 건설한 곳인지 아닌지 확인하기 위한 세트
	constructed = set()

	# 마지막 땅까지 확인하고 이상이 없다면 True를 리턴한다.
	while index < road_length:
		# 현재 높이와 바로 전 높이의 차이 값을 구한다.
		status = road[index] - road[index - 1]

		# 인접한 땅의 높이 차이가 1보다 크면 활주로 건설이 불가능하므로 False
		if abs(status) > 1:
			return False

		# 현재 땅이 이전 땅보다 1만큼 높다면,
		elif status == 1:
			# 혹시나 활주로가 0번 인덱스보다 작은 곳까지 설치되야 하는지 여부를 확인한다.
			if index < chance:
				# 활주로를 인덱스 -1 이하에도 설치해야 할 때는 False를 리턴한다.
				return False
			else:
				# 활주로 건설에 이상이 있는 지 확인한다.
				for extra in range(chance):
					# 활주로를 건설해야 하는 땅들의 높이가 같은지 확인한다.
					if road[index-1] != road[index-1-extra]:
						return False
					# 혹시 이전에 활주로를 건설한 땅이 아닌지 확인한다.
					if index - 1 - extra in constructed:
						return False
				else:
					# 이상이 없다면 다음 땅을 확인한다.
					index += 1

		# 현재 땅이 이전 땅보다 1만큼 낮다면,
		elif status == -1:
			# 혹시나 활주로가 road_size보다 크거나 같은 위치에 설치되야 하는지 여부를 확인한다.
			if road_length - index < chance:
				# 활주로를 인덱스 road_size 이상에도 설치해야 할 때는 False를 리턴한다.
				return False
			else:
				# 활주로 건설에 이상이 있는 지 확인한다.
				for extra in range(chance):
					# 활주로를 건설해야 하는 땅들의 높이가 같은지 확인한다.
					if road[index] != road[index+extra]:
						return False
					# 이상이 없다면, 활주로를 건설했다는 표시를 해둔다.
					else:
						constructed.add(index + extra)
				else:
					# 이상이 없다면 활주로 건설이 완료된 그 이후 땅부터 재탐색한다.
					index += chance

		# 현재 땅과 이전 땅의 높이가 갖다면 다음 땅을 탐색한다.
		else:
			index += 1

	return True


for testCase in range(int(input())):
	size_land, length_chance = map(int, input().split())

	# 가로행 세로행을 합쳐 size_land*2 X size_land 2차 리스트를 새로 만든다
	_land = [list(map(int, input().split())) for _ in range(size_land)]
	__land = list(map(list, zip(*_land)))
	land = _land + __land

	# 한 줄 씩 돌려보며 활주로로 사용이 가능하면 그 수를 카운트 한다.
	cnt = 0
	for lane in land:
		if solution(lane, length_chance, size_land):
			cnt += 1
	print("#{} {}".format(testCase + 1, cnt))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 7
# 2 4
# 3 11
# 4 11
# 5 15
# 6 4
# 7 4
# 8 1
# 9 5
# 10 8
