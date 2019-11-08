import sys
import timeit
import pprint

sys.stdin = open('그래프_색칠하기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_node, qnt_line, qnt_color = map(int, input().split())
    table = [[]for _ in range(qnt_node)]
    for _ in range(qnt_line):
        start, end = map(int, input().split())
        table[start-1].append(end-1)
        table[end-1].append(start-1)
    count = 0
    color = 0
    used = set()
    temp_table = []
    colored_node = set()
    for qnt in range(qnt_node):
        temp_table.append(table[qnt][:])
    while count != qnt_node:
        target_node = -1
        max_size = 0
        for node in range(qnt_node):
            if node not in used and len(temp_table[node]) > max_size:
                max_size = len(temp_table[node])
                target_node = node
        if target_node != -1:
            used.add(target_node)
            for node in temp_table[target_node]:
                if target_node in temp_table[node]:
                    temp_table[node].remove(target_node)
                used.add(node)
            temp_table[target_node] = []
            colored_node.add(target_node)
            count += 1
        else:
            used = set()
            color += 1
            temp_table = []
            for node in range(qnt_node):
                if node not in colored_node:
                    temp_table.append(table[node][:])
                else:
                    temp_table.append([])
    print("#{} {}".format(testCase + 1, 1 if color <= qnt_color else 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 0
