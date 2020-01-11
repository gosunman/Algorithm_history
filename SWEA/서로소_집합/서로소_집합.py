import sys
import timeit
import pprint

sys.stdin = open('서로소_집합', 'r')

start_time = timeit.default_timer()

def group(node):
    global fathers
    while fathers[node] != node:
        node = fathers[node]
    return node

for testCase in range(int(input())):
    N_groups, M_operators = map(int, input().split())
    fathers = [i for i in range(N_groups)]
    answer = ""
    for _ in range(M_operators):
        operator, n1, n2 = map(int, input().split())
        n1 -= 1
        n2 -= 1
        if operator:
            if group(n1) == group(n2):
                answer += '1'
            else:
                answer += '0'
        else:
            fathers[group(n2)] = group(n1)
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 001