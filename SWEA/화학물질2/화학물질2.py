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

    data = [elements.pop()]
    cnt = 0
    while cnt != len(elements):
        a = info_end.get(data[0][0])
        if a == 0 or a:
            data.insert(0, elements[info_end.get(data[0][0])])
        else:
            b = info_front.get(data[-1][1])
            if b == 0 or b:
                data.append(elements[info_front.get(data[-1][1])])
        cnt += 1

    cnt = len(data)

    new_data = [data[0][0]]
    for index in range(cnt):
        new_data.append(data[index][1])

    table = [[0 for _ in range(cnt + 1)] for __ in range(cnt + 1)]

    for layer in range(1, cnt+1):
        for index in range(cnt - layer + 1):
            if table[index][index + layer - 1] < table[index + 1][index + layer]:
                common = table[index][index + layer - 1]
                new = new_data[index] * new_data[layer] * new_data[layer + 1]
                table[index][index + layer] = common + new
            else:
                common = table[index + 1][index + layer]
                new = new_data[index] * new_data[index+1] * new_data[index + 2]
                table[index][index + layer] = common + new
    print("#{} {}".format(tc + 1, table[cnt][cnt]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 64
# 2 6
