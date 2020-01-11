import sys
import timeit
import pprint

sys.stdin = open('최소_스패닝_트리', 'r')

start_time = timeit.default_timer()

def group(node):
    global fathers
    while fathers[node] != node:
        node = fathers[node]
    return node

for testCase in range(int(input())):
    N_nodes, N_edges = map(int, input().split())
    S_edges = []
    for i in range(N_edges):
        S_edges.append(list(map(int, input().split())))
    S_edges.sort(key=lambda x: x[2])
    fathers = [i for i in range(N_nodes)]
    available = [1 for i in range(N_nodes)]
    answer = 0
    for i in range(N_edges):
        n1, n2, w = S_edges[i]
        n1 -= 1
        n2 -= 1
        if available[n1]:
            if available[n2]:
                answer += w
                available[n1] = 0
                available[n2] = 0
                fathers[n2] = n1
            else:
                answer += w
                available[n1] = 0
                fathers[n1] = group(n2)
        else:
            if available[n2]:
                answer += w
                available[n2] = 0
                fathers[n2] = group(n1)
            else:
                f1 = group(n1)
                f2 = group(n2)
                if f1 != f2:
                    answer += w
                    fathers[n1] = f2
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 19
#3 2
#4 13
#5 22

