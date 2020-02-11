import sys
import timeit
import pprint

sys.stdin = open('팰린드롬_경로_찾기', 'r')

start_time = timeit.default_timer()


def solution(index, limit, last):
    pass


for testCase in range(int(input())):
    N_inputs = int(input())
    S_inputs = [list(map(int, input().split())) for _ in range(N_inputs)]
    C_inputs = [[0 for _ in range(N_inputs)] for __ in range(N_inputs)]
    stack = []
    for y in range(N_inputs):
        for x in range(N_inputs):
            if y + x == N_inputs - 1:
                C_inputs[y][x] = 1
                stack.append([[x, y], [x, y]])
    answer = 0
    N_big = 1000000007
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 12
