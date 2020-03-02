import sys
import timeit
import pprint

sys.stdin = open('수영장', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))