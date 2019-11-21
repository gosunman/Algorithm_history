import sys
import timeit
import pprint

sys.stdin = open('화학물질2', 'r')

start_time = timeit.default_timer()

for tc in range(int(input())):
    ans = float('inf')
    size_table = int(input())
    table = [list(map(int, input().split())) for _ in range(size_table)]
    elements = []
    info_front = {}
    info_end = {}
    cnt = 0

    for y in range(size_table):
        for x in range(size_table):
            if table[y][x]:
                i, j = x, y
                while j < size_table and table[j][i]:
                    j += 1
                j -= 1
                while i < size_table and table[j][i]:
                    i += 1
                i -= 1
                elements.append([j - y + 1, i - x + 1])
                info_front[j - y + 1] = cnt
                info_end[i - x + 1] = cnt
                cnt += 1
                for column in range(y, j + 1):
                    for row in range(x, i + 1):
                        table[column][row] = 0

    data = [elements[0]]
    cnt = 1
    while cnt != len(elements):
        a = info_end.get(data[0][0])
        if a is not None:
            data.insert(0, elements[a])
        else:
            b = info_front.get(data[-1][1])
            if b is not None:
                data.append(elements[b])
        cnt += 1

    sources = [data[0][0]]
    for index in range(cnt):
        sources.append(data[index][1])

    table = [[0 for _ in range(cnt)] for __ in range(cnt)]

    for layer in range(1, cnt):
        for count in range(cnt - layer):
            y = count
            x = count + layer
            answer = float('inf')
            for k in range(y, x):
                a, b, c = sources[y-1], sources[k], sources[x]
                temp = table[y][k] + table[k+1][x] + a*b*c
                if temp < answer:
                    answer = temp
            table[y][x] = answer
    print("#{} {}".format(tc + 1, table[0][cnt-1]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 64
# 2 6
