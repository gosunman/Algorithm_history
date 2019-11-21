import sys
import timeit
import pprint

sys.stdin = open('사람_네트워크2', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    temp_input = list(map(int, input().split()))
    size_table = temp_input[0]
    table = []
    for index in range(size_table):
        table.append(temp_input[1 + size_table * index:1 + size_table * (index + 1)])
        for i in range(size_table):
            if table[index][i] == 0:
                table[index][i] = float("inf")
    temp_input = []
    for k in range(size_table):
        for j in range(size_table):
            if j != k:
                for i in range(j+1, size_table):
                    if k != i:
                        table[i][j] = table[j][i] = min(table[i][j], table[i][k] + table[k][j])
    answer = size_table ** 2
    for index in range(size_table):
        temp_answer = 0
        for element in table[index]:
            if element != float("inf"):
                temp_answer += element
        if temp_answer < answer:
            answer = temp_answer
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 4
# 2 5
# 1 2
# 2 3
# 3 25
# 4 37
# 5 16
# 6 11
# 7 21
# 8 20
# 9 715
# 10 1449
