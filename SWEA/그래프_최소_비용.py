import sys
import timeit
import pprint

sys.stdin = open('그래프_최소_비용', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    size_table = int(input())
    table = [list(map(int, input().split())) for _ in range(size_table)]

    for j in range(size_table):
        for i in range(size_table):
            if table[j][i] == 0:
                table[j][i] = float('inf')

    for k in range(size_table):
        for j in range(size_table):
            for i in range(size_table):
                if i != j:
                    table[j][i] = min(table[j][i], table[j][k]+table[k][i])

    ans = 0
    for j in range(size_table):
        for i in range(size_table):
            if i != j:
                if table[j][i] > ans:
                    ans = table[j][i]
    print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 99
#2 132
#3 92