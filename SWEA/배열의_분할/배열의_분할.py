import sys
import timeit
import pprint

sys.stdin = open('배열의_분할', 'r')

start_time = timeit.default_timer()


def solution(index, cut, state):
    global answer, N_size, S_number
    if index + 1 < N_size:
        temp_diff = S_number[index + 1] - S_number[index]
        if state:
            if temp_diff < 0:
                solution(index + 1, cut + 1, not state)
                solution(index + 1, cut + 1, state)
            else:
                solution(index + 1, cut, state)
        else:
            if temp_diff > 0:
                solution(index + 1, cut + 1, not state)
                solution(index + 1, cut + 1, state)
            else:
                solution(index + 1, cut, state)
    else:
        if cut < answer:
            answer = cut


for testCase in range(int(input())):
    answer = float('inf')
    N_size = int(input())
    S_number = list(map(int, input().split()))
    initial_state = -1
    initial_index = 0
    while initial_index + 1 < N_size:
        diff = S_number[initial_index + 1] - S_number[initial_index]
        if diff == 0:
            initial_index += 1
        elif diff > 0:
            initial_state = True
            break
        else:
            initial_state = False
            break

    if initial_state != -1:
        solution(initial_index + 1, 1, initial_state)
    else:
        answer = 1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 2
# 3 5
