import sys
import timeit
import pprint

sys.stdin = open('준환이의_양팔저울', 'r')

start_time = timeit.default_timer()


def seq(current, end, result,):
    global sequence
    if current == end - 1:
        sequence[end].append(result[:])
    else:
        seq(current + 1, end, result)
        for i in range(current + 1, end):
            result[current], result[i] = result[i], result[current]
            seq(current + 1, end, result)
            result[current], result[i] = result[i], result[current]


sequence = [[] for i in range(10)]

for i in range(1, 10):
    seq(0, i, list(range(i)))


def solution(current, end, sum_l, sum_r, total):
    global answer, array, S_weights
    if total - sum_l <= sum_l:
        answer += 2**(end-current)
    else:
        if current == end:
            answer += 1
        else:
            solution(current + 1, end, sum_l + S_weights[array[current]], sum_r, total)
            if sum_l >= sum_r + S_weights[array[current]]:
                solution(current + 1, end, sum_l, sum_r + S_weights[array[current]], total)


for tc in range(int(input())):
    N_weights = int(input())
    S_weights = list(map(int, input().split()))
    answer = 0
    for array in sequence[N_weights]:
        solution(1, N_weights, S_weights[array[0]], 0, sum(S_weights))
    print('#{} {}'.format(tc + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 15
# 2 17
# 3 35583723
