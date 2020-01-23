import sys
import timeit
import pprint

sys.stdin = open('최소_스패닝_트리', 'r')

start_time = timeit.default_timer()

# for testCase in range(int(input())):
#     N_nodes, N_edges = map(int, input().split())
#     S_edges = [list(map(int, input().split())) for i in range(N_edges)]
#     S_edges.sort(key=lambda x: x[2])
#     available = [1 for i in range(N_nodes + 1)]
#     answer = 0
#     N_line = 0
#     index_edges = 0
#     groups = []
#     while N_line < N_nodes - 1:
#         n1, n2, w = S_edges[index_edges]
#         if available[n1]:
#             if available[n2]:
#                 available[n2] = 0
#                 temp = set()
#                 temp.add(n1)
#                 temp.add(n2)
#                 groups.append(temp)
#             else:
#                 for idx in range(len(groups)):
#                     if n2 in groups[idx]:
#                         groups[idx].add(n1)
#                         break
#             available[n1] = 0
#             answer += w
#             N_line += 1
#         else:
#             if available[n2]:
#                 answer += w
#                 available[n2] = 0
#                 for idx in range(len(groups)):
#                     if n1 in groups[idx]:
#                         groups[idx].add(n2)
#                         break
#                 N_line += 1
#             else:
#                 number1 = number2 = -1
#                 for idx in range(len(groups)):
#                     if n1 in groups[idx]:
#                         number1 = idx
#                     if n2 in groups[idx]:
#                         number2 = idx
#                 if number1 != number2:
#                     if number1 > number2:
#                         number1, number2 = number2, number1
#                     answer += w
#                     temp_set = groups.pop(number2)
#                     groups[number1] = groups[number1] | temp_set
#                     N_line += 1
#         index_edges += 1
#     print("#{} {}".format(testCase + 1, answer))




def group(node):
    global fathers
    temp_count = 0
    while fathers[node] != node:
        node = fathers[node]
        temp_count += 1
    return node, temp_count


for testCase in range(int(input())):
    N_nodes, N_edges = map(int, input().split())
    S_edges = [list(map(int, input().split())) for i in range(N_edges)]
    S_edges.sort(key=lambda x: x[2])
    fathers = [i for i in range(N_nodes + 1)]
    available = [1 for i in range(N_nodes + 1)]
    answer = 0
    N_line = 0
    index_edges = 0
    while N_line < N_nodes - 1:
        n1, n2, w = S_edges[index_edges]
        if available[n1]:
            if available[n2]:
                available[n2] = 0
                fathers[n2] = n1
            else:
                fathers[n1] = group(n2)[0]
            available[n1] = 0
            answer += w
            N_line += 1
        else:
            if available[n2]:
                answer += w
                available[n2] = 0
                fathers[n2] = group(n1)[0]
                N_line += 1
            else:
                f1, c1 = group(n1)
                f2, c2 = group(n2)
                if f1 != f2:
                    if c1 < c2:
                        fathers[f1] = f2
                    else:
                        fathers[f2] = f1
                    answer += w
                    N_line += 1
        index_edges += 1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 3
# 2 19
# 3 2
# 4 13
# 5 22
