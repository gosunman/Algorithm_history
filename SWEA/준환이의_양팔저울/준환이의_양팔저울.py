import sys
import timeit
import pprint

sys.stdin = open('준환이의_양팔저울', 'r')

start_time = timeit.default_timer()


def solution(depth, limit, left, right):
    global answer, S_weights, available
    if depth != limit:
        count = limit-1
        for i in range(limit):
            if available[i]:
                available[i] = 0
                solution(depth+1, limit, left + S_weights[i], right)
                if left >= right + S_weights[i]:
                    solution(depth + 1, limit, left, right + S_weights[i])
                else:
                    count = i
                    available[i] = 1
                    break
                available[i] = 1
        for i in range(count+1, limit):
            if available[i]:
                available[i] = 0
                solution(depth+1, limit, left + S_weights[i], right)
                available[i] = 1
    else:
        answer += 1


for testCase in range(int(input())):
    N_weights = int(input())
    S_weights = list(map(int, input().split()))
    answer = 0
    available = [1 for _ in range(N_weights)]
    solution(0, N_weights, 0, 0)
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 15
# 2 17
# 3 35583723
