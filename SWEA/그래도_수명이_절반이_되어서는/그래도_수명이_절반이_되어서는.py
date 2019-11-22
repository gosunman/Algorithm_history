import sys
import timeit
import pprint

sys.stdin = open('그래도_수명이_절반이_되어서는', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 5
#3 3