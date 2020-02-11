import sys
import timeit
import pprint

sys.stdin = open('당근밭_경보기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_table = int(input())
    S_table = [list(map(int, input().split())) for _ in range(N_table)]

    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 2
#2 7
#3 2