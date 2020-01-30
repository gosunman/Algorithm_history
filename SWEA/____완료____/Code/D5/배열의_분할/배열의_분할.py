import sys
import timeit
import pprint

sys.stdin = open('배열의_분할', 'r')

start_time = timeit.default_timer()


def find_state():
    global N_size, S_number, index, state
    state = 0
    while index + 1 < N_size:
        diff = S_number[index + 1] - S_number[index]
        if diff > 0:
            state = 1
            index += 1
            break
        elif diff < 0:
            state = -1
            index += 1
            break
        else:
            index += 1


def find_index():
    global answer, N_size, S_number, index, state
    if state > 0:
        while index + 1 < N_size:
            diff = S_number[index + 1] - S_number[index]
            if diff >= 0:
                index += 1
            else:
                answer += 1
                index += 1
                break
    elif state < 0:
        while index + 1 < N_size:
            diff = S_number[index + 1] - S_number[index]
            if diff <= 0:
                index += 1
            else:
                answer += 1
                index += 1
                break
    else:
        index += 1


for testCase in range(int(input())):
    answer = 1
    N_size = int(input())
    S_number = list(map(int, input().split()))
    index, state = 0, 0
    while index < N_size:
        find_state()
        find_index()
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 2
# 3 5
