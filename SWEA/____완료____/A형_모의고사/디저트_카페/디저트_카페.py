import sys
import timeit
import pprint

sys.stdin = open('디저트_카페', 'r')

start_time = timeit.default_timer()

move = [
    lambda x: [x[0] + 1, x[1] + 1],
    lambda x: [x[0] - 1, x[1] + 1],
    lambda x: [x[0] - 1, x[1] - 1],
    lambda x: [x[0] + 1, x[1] - 1],
]


def comb(i, j):
    global size, tc
    candidates = []
    for first in range(1, min(size - i, size - j - 1)):
        for second in range(1, min(i + 1, size - j - first)):
            candidates.append([first, second, first, second])
    return candidates


def solution(i, j):
    global ans, size, table, notFound
    candidates = comb(i, j)
    for candidate in candidates:
        point = [i, j]
        temp_ans = []
        impossible = False
        for index, step in enumerate(candidate):
            for _ in range(step):
                point = move[index](point)
                value = table[point[1]][point[0]]
                if value in temp_ans:
                    impossible = True
                    break
                else:
                    temp_ans.append(value)
            if impossible:
                break
        if not impossible:
            notFound = False
            if ans < len(temp_ans):
                ans = len(temp_ans)


for tc in range(int(input())):
    ans = 0
    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]
    notFound = True
    for y in range(size - 2):
        for x in range(1, size - 1):
            solution(x, y)
    if notFound:
        ans = -1
    print("#{} {}".format(tc + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
