import sys
import timeit
import pprint

sys.stdin = open('콩_많이_심기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N, M = map(int, input().split())
    answer = 0
    x = -1
    for i in range(N):
        x += 1
        x %= 4
        y = -1
        for j in range(M):
            y += 1
            y %= 4
            if x == 0 or x == 1:
                if y == 0 or y == 1:
                    answer += 1
            else:
                if y == 2 or y == 3:
                    answer += 1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 4
