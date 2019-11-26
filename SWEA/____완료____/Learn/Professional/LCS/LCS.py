import sys
import timeit
import pprint

sys.stdin = open('LCS', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    DNA_1 = '0' + input().strip()
    DNA_2 = '0' + input().strip()
    i = j = 0
    imax = len(DNA_1)
    jmax = len(DNA_2)
    table = [[0 for _ in range(imax)] for __ in range(jmax)]
    for j in range(jmax):
        for i in range(imax):
            if i == 0 or j == 0:
                table[j][i] = 0
            else:
                if DNA_1[i] == DNA_2[j]:
                    table[j][i] = table[j - 1][i - 1] + 1
                else:
                    table[j][i] = max(table[j - 1][i], table[j][i - 1])
    print("#{} {}".format(testCase + 1, table[jmax-1][imax-1]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 3
