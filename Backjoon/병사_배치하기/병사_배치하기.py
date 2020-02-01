import sys
import timeit
import pprint

sys.stdin = open('병사_배치하기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_input = int(input())
    S_input = list(map(int, input().split()))
    table = [1 for i in range(N_input)]
    for i in range(1, N_input):
        base = S_input[i]
        for j in range(N_input):
            if S_input[j] > base and table[i] < table[j]+1:
                table[i] = table[j] + 1
    print(N_input - table[N_input - 1])

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 2

# LIS