import sys
import timeit
import pprint

sys.stdin = open('키_순서', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
	qnt_people = int(input())
	qnt_relations = int(input())
	table = [[0 for _ in range(qnt_people)] for __ in range(qnt_people)]
	for relation in range(qnt_relations):
		start, end = map(int, input().split())
		table[start-1][end-1] = 1
	for k in range(qnt_people):
		for j in range(qnt_people):
			if k != j:
				for i in range(qnt_people):
					if i != k and i != j and not table[i][j]:
						if table[i][k] and table[k][j]:
							table[i][j] = 1
	answer = 0
	for person in range(qnt_people):
		temp = 0
		for _ in range(qnt_people):
			temp += table[person][_] + table[_][person]
		if temp == qnt_people-1:
			answer += 1
	print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
