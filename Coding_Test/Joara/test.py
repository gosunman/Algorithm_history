import sys
import timeit
import pprint

sys.stdin = open('../../problem_list.txt', 'r')

start_time = timeit.default_timer()


def solution(N, K):
    genuine_count = 0
    temp_index = 0
    Nsoldiers = N - 2
    status_soldiers = [0] + [1 for i in range(N - 2)]
    while Nsoldiers != 2:
        while genuine_count != K:
            temp_index += 1
            temp_index %= N - 1
            if status_soldiers[temp_index]:
                genuine_count += 1
        status_soldiers[temp_index] = 0
        Nsoldiers -= 1
        genuine_count = 0
    print("the answer is")
    for i in range(N - 1):
        if status_soldiers[i]:
            print(i)
    print("done")


solution(41, 3)

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))
