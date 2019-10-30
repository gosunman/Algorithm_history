import sys
import timeit
import pprint

sys.stdin = open('활주로_건설.txt', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
	start, end = map(int, input().split())
	print("#{} {}".format(testCase + 1, cnt))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1
#2 0
#3 31