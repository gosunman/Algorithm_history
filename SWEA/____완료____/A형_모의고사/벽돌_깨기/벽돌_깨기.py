dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def blast(samples, x, y):
    global size_x, size_y
    stack = [[x, y]]
    while stack:
        temp_stack = []
        while stack:
            xx, yy = stack.pop()
            weight = samples[yy][xx]
            samples[yy][xx] = 0
            if weight > 1:
                for distance in range(1, weight):
                    for _ in range(4):
                        new_x, new_y = xx + dx[_] * distance, yy + dy[_] * distance
                        if 0 <= new_x < size_x and 0 <= new_y < size_y:
                            if samples[new_y][new_x] and [new_x, new_y] not in stack:
                                temp_stack.append([new_x, new_y])
        stack += temp_stack
    for yy in range(size_y):
        for xx in reversed(range(size_x)):
            if samples[yy][xx] == 0:
                del samples[yy][xx]
        shortage = size_x - len(samples[yy])
        for _ in range(shortage):
            samples[yy].insert(0, 0)
    return samples


def solution(samples, depth, limit, history):
    global ans, size_x, size_y

    if depth != limit:
        for y in range(size_y):
            next_samples = []
            for _ in range(size_y):
                next_samples.append(samples[_][:])

            if next_samples[y].count(0) != size_x:
                x = 0
                while not next_samples[y][x]:
                    x += 1
                next_samples = blast(next_samples, x, y)

            solution(next_samples, depth + 1, limit, history + [y])

    else:
        score = 0
        for y in range(size_y):
            for x in range(size_x):
                if samples[y][x]:
                    score += 1
        if score < ans:
            # pprint.pprint(samples)
            # print(history, score)
            ans = score


for t in range(int(input())):
    chance, size_y, size_x = map(int, input().split())
    ans = size_x * size_y
    table = [list(map(int, input().split())) for _ in range(size_x)]
    table = list(map(list, zip(*table)))
    solution(table, 0, chance, [])
    print("#{} {}".format(t + 1, ans))

