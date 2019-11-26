import sys
import timeit
import pprint

sys.stdin = open('All_Pair_Shortest_Path', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    n_node, n_edge = map(int, input().split())
    table_edge = [[float('inf') for _ in range(n_node)] for __ in range(n_node)]
    for _ in range(n_edge):
        start, end, weight = map(int, input().split())
        table_edge[start-1][end-1] = weight
    for k in range(n_node):
        for start in range(n_node):
            if k != start:
                for end in range(n_node):
                    if k != end and start != end:
                        option1 = table_edge[start][end]
                        option2 = table_edge[start][k]+table_edge[k][end]
                        table_edge[start][end] = min(option1, option2)
    answer = []
    for j in range(n_node):
        for i in range(n_node):
            if i == j:
                answer.append('0')
            else:
                if table_edge[j][i] == float('inf'):
                    answer.append('-1')
                else:
                    answer.append(str(table_edge[j][i]))
    print("#{} {}".format(testCase + 1, " ".join(answer)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 0 1 3 5 0 2 3 4 0