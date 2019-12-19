import sys
import timeit
import pprint

sys.stdin = open('그래프_색칠하기.txt', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):

    # initialize
    qnt_node, qnt_line, qnt_color = map(int, input().split())
    table = [[]for _ in range(qnt_node)]
    for _ in range(qnt_line):
        start, end = map(int, input().split())
        table[start-1].append(end-1)
        table[end-1].append(start-1)

    # run
    count = 0
    color = 0
    available = set()
    colored_node = set()

    temp_table = []
    for qnt in range(qnt_node):
        temp_table.append(table[qnt][:])

    while count != qnt_node:
        target_node = -1
        max_size = 0
        for node in range(qnt_node):
            if node not in available and len(temp_table[node]) > max_size:
                max_size = len(temp_table[node])
                target_node = node

        if target_node != -1:
            available.add(target_node)
            for node in temp_table[target_node]:
                temp_table[node].remove(target_node)
                available.add(node)
            temp_table[target_node] = []
            colored_node.add(target_node)
            for node in range(qnt_node):
                if target_node in table[node]:
                    table[node].remove(target_node)
            count += 1
        else:
            available = set()
            color += 1
            temp_table = []
            escape = 0
            for node in range(qnt_node):
                if node not in colored_node:
                    temp_table.append(table[node][:])
                else:
                    temp_table.append([])
                if not temp_table[node]:
                    escape += 1
            if escape == qnt_node:
                color += 1
                break
    print("#{} {}".format(testCase + 1, 1 if color <= qnt_color else 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 0
