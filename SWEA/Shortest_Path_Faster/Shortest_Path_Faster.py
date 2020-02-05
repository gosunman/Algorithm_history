import sys
import timeit

sys.stdin = open('Shortest_Path_Faster', 'r')

start_time = timeit.default_timer()


def en(ele):
    global count, que
    count += 1
    index = count
    que[count] = ele
    while index > 1:
        if que[index][0] < que[index // 2][0]:
            que[index], que[index // 2] = que[index // 2], que[index]
            index //= 2
        else:
            index = 1


def de():
    global count, que
    pop_ele = que[1]
    que[1], que[count] = que[count], que[1]
    index = 1
    while index < count:
        if index * 2 < count:
            if index * 2 + 1 < count:
                target = (index * 2) if que[index * 2] <= que[index * 2 + 1] else (index * 2 + 1)
                if que[index] > que[target]:
                    que[index], que[target] = que[target], que[index]
                    index = target
                else:
                    count -= 1
                    return pop_ele
            else:
                if que[index] > que[index * 2]:
                    que[index], que[index * 2] = que[index * 2], que[index]
                    index *= 2
                else:
                    count -= 1
                    return pop_ele
        else:
            index *= 2
    count -= 1
    return pop_ele


for testCase in range(int(input())):
    N_node, N_edge, start, end = map(int, input().split())
    S_edge = [list(map(int, input().split())) for _ in range(N_edge)]
    edges = {}
    for i in range(N_edge):
        a, b, c = S_edge[i]
        if edges.get(a):
            edges[a][b] = c
        else:
            edges[a] = {b: c}
        if edges.get(b):
            edges[b][a] = c
        else:
            edges[b] = {a: c}
    count = 0
    que = [0] * 300001
    en([0, start])
    while start != end:
        point, start = de()
        if start == end:
            print("#{} {}".format(testCase + 1, point))
        else:
            for key, value in edges[start].items():
                en([point + value, key])

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))



# 1 1
# 2 3
