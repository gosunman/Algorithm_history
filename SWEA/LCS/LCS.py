import sys
import timeit
import pprint

sys.stdin = open('LCS', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    DNA_1 = input().strip()
    DNA_2 = input().strip()
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3