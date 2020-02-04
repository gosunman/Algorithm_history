import sys
import timeit
import pprint
import heapq

sys.stdin = open('Shortest_Path_Faster', 'r')

start_time = timeit.default_timer()

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
    available = [1 for _ in range(N_node + 1)]
    bfs = [[start, 0]]
    while start != end:
        start, point = heapq.heappop(bfs)
        print(start, point)
        for key in edges[start].keys():
            if key == end:
                print("#{} {}".format(testCase + 1, point + edges[start][key]))
                start = end
                break
            if available[key]:
                available[key] = 0
                heapq.heappush(bfs, (point + edges[start][key], [key, point + edges[start][key]]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 3
