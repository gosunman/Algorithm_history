import sys
import timeit
import pprint

sys.stdin = open('최종평가', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_table, N, K = map(int, input().split())
    S_table = []
    A = [0 for _ in range(N)]
    for robot in range(N):
        S_table.append(list(map(int, input().split())))
    for basis in range(N):
        y_basis, x_basis = S_table[basis]
        found = {'x+': set(), 'x-': set(), 'y+': 1, 'y-': 1}
        for robot in range(N):
            if basis != robot:
                y_robot, x_robot = S_table[robot]
                if x_basis == x_robot:
                    if y_basis > y_robot and found['y-']:
                        A[basis] += 1
                        found['y-'] = 0
                    elif y_basis < y_robot and found['y+']:
                        A[basis] += 1
                        found['y+'] = 0
                else:
                    slope = (y_robot - y_basis) / (x_robot - x_basis)
                    if x_basis > x_robot:
                        if slope not in found['x-']:
                            A[basis] += 1
                            found['x-'].add(slope)
                    else:
                        if slope not in found['x+']:
                            A[basis] += 1
                            found['x+'].add(slope)
    answer1 = sum(A)

    A += [0 for i in range(N)]
    B = [0 for i in range(N * 2)]
    C = [0 for i in range(N)]

    for i in range(N):
        for j in range(N):
            A[j] = (A[j] * K + j + 1) % N + 1
            A[N + j] = (A[j] * (j + 1) + K) % N + 1
        A.sort()

        B[0] = (1 * A[0] + 1) % N + 1
        for j in range(1, N * 2):
            B[j] = (B[j - 1] * A[j] + j + 1) % N + 1
        C[i] = B[- 1]
    answer2 = sum(C)

    print("#{} {} {}".format(testCase + 1, answer1, answer2))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 8 15
# 2 6 4
# 3 36 14
