import sys
import timeit
import pprint

sys.stdin = open('홍준이의_숫자_놀이', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 2 -1
#2 1 -3