import sys
import timeit
import pprint

sys.stdin = open('디오판토스_방정식', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    a, b, c = map(int, input().split())
    x = 1
    y = c - 
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1 -1