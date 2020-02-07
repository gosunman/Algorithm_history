import sys
import timeit
import pprint

sys.stdin = open('최솟값으로_이동하기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    W, H, N = map(int, input().split())
    S_points = [list(map(int, input().split())) for _ in range(N)]
    start_x, start_y = S_points[0]
    i = 1
    answer = 0
    while i < N:
        end_x, end_y = S_points[i]
        diff_x, diff_y = end_x - start_x, end_y - start_y
        if diff_x * diff_y > 0:
            answer += max(abs(diff_x), abs(diff_y))
        elif diff_x * diff_y < 0:
            answer += (abs(diff_x) + abs(diff_y))
        else:
            answer += max(abs(diff_x), abs(diff_y))
        start_x, start_y = end_x, end_y
        i += 1
    print('#{} {}'.format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 5
