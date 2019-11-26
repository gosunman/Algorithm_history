import sys
import timeit
import pprint

sys.stdin = open('쥬스_나누기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    n = int(input())
    answer = [f'1/{n}'] * n
    print("#{} {}".format(testCase + 1, " ".join(answer)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1/1
#2 1/2 1/2