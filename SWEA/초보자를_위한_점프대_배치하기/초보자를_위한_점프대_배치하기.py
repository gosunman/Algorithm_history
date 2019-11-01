import sys
import timeit
import pprint

sys.stdin = open('초보자를_위한_점프대_배치하기', 'r')

start_time = timeit.default_timer()


for testCase in range(int(input())):
	size_bars = int(input())
	bars = sorted(list(map(int, input().split())))
	ans = 0
	print("#{} {}".format(testCase + 1, bars))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1
#2 4
#3 0