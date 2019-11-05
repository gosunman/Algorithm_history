import sys
import timeit
import pprint

sys.stdin = open('벽돌_깨기', 'r')

start_time = timeit.default_timer()

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bomb(line, data):
    stack = []
    bomb = 0
    for Y in range(limit_y):
        if data[Y][line]:
            stack = [line, Y]
            break
    else:
        return bomb
    while stack:
        old_x, old_y = stack.pop()
        distance = data[old_y][old_x]
        data[old_y][old_x] = -1
        temp_stack = []
        while stack:
            for move in moves:
                dx, dy = move
                new_x, new_y = old_x + dx, old_y + dy
                temp_stack.append([new_x, new_y])


def solution(depth, count, temp):
    global limit, limit_x, limit_y, maximum_bang
    if depth != limit:
        for i in range(limit_x):
            _table = []
            for j in range(limit_y):
                _table.append(temp[j][:])
                cnt = bomb(i, _table)
                solution(depth + 1, count + cnt, _table)
    else:
        if count > maximum_bang:
            maximum_bang = count


for testCase in range(int(input())):
    limit, limit_x, limit_y = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(limit_y)]
    maximum_bang = 0
    total = 0
    for y in range(limit_y):
        for x in range(limit_x):
            if table[y][x]:
                total += 1
    solution(0, 0, table)
    print("#{} {}".format(testCase + 1, total - maximum_bang))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 12
# 2 27
# 3 4
# 4 8
# 5 0
