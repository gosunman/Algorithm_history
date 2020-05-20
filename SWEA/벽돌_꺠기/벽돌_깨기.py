import sys
import timeit
import pprint

sys.stdin = open('벽돌_깨기', 'r')

start_time = timeit.default_timer()


def find_case(index, N, W, history):
    global cases
    if index != N:
        for i in range(W):
            history.append(i)
            find_case(index + 1, N, W, history)
            history.pop()
    else:
        cases.append(history[:])


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    status = [list(map(int, input().split())) for i in range(H)]
    total = 0
    for y in range(H):
        for x in range(W):
            if status[y][x]:
                total += 1

    cases = []
    find_case(0, N, W, [])

    hit = 0
    for case in cases:
        bang = 0
        copy_table = [status[i][:] for i in range(H)]
        for x in case:
            available = [[1 for j in range(W)] for i in range(H)]
            stack = []
            for y in range(H):
                if copy_table[y][x]:
                    stack.append([x, y])
                    bang += 1
                    available[y][x] = 0
                    break
            while stack:
                i, j = stack.pop()
                for length in range(1, status[j][i]):
                    if 0 <= i - length:
                        if available[j][i - length]:
                            if status[j][i - length]:
                                stack.append([i - length, j])
                                bang += 1
                                available[j][i - length] = 0
                    if i + length < W:
                        if available[j][i + length]:
                            if status[j][i + length]:
                                stack.append([i + length, j])
                                bang += 1
                                available[j][i + length] = 0
                    if 0 <= j - length:
                        if available[j - length][i]:
                            if status[j - length][i]:
                                stack.append([i, j - length])
                                bang += 1
                                available[j - length][i] = 0
                    if j + length < H:
                        if available[j + length][i]:
                            if status[j + length][i]:
                                stack.append([i, j + length])
                                bang += 1
                                available[j + length][i] = 0
            # 빈자리 정리 작업
            for i in range(W):
                found = -1
                for j in range(H):
                    if copy_table[j][i]:
                        fount = j
                        break
                count = 0
                for j in range(H-1, found, -1):
                    if copy_table[j][i] == 0:
                        copy_table[j].pop(i)
                        count += 1
                copy_table[j] = [0 for k in range(count)] + copy_table[j]

        if bang > hit:
            hit = bang
    print("#{} {}".format(tc + 1, total - hit))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 12
# 2 27
# 3 4
# 4 8
# 5 0
