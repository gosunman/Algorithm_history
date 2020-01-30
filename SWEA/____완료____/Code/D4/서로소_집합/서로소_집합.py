import sys
import timeit
import pprint

sys.stdin = open('서로소_집합', 'r')

start_time = timeit.default_timer()


def group(node):
    global fathers
    count = 0
    while fathers[node] != node:
        node = fathers[node]
        count += 1
    return node, count


for testCase in range(int(input())):
    N_groups, M_operators = map(int, input().split())
    fathers = [i for i in range(N_groups)]
    answer = ""
    for _ in range(M_operators):
        operator, n1, n2 = map(int, input().split())
        n1 -= 1
        n2 -= 1
        if operator:
            if group(n1)[0] == group(n2)[0]:
                answer += '1'
            else:
                answer += '0'
        else:
            father1, count1 = group(n1)
            father2, count2 = group(n2)
            if count1 > count2:
                fathers[father2] = father1
            else:
                fathers[father1] = father2
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 001
