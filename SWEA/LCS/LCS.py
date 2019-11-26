import sys
import timeit
import pprint

sys.stdin = open('LCS', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    DNA_1 = input().strip()
    DNA_2 = input().strip()
    i = j = 0
    imax = len(DNA_1)
    jmax = len(DNA_2)
    table = [[0 for _ in range(imax)] for __ in range(jmax)]
    if DNA_1[i] == DNA_2[j]:
        pass
    elif DNA_1[i] == DNA_2[j - 1]:
        pass
    elif DNA_1[i - 1] == DNA_2[j]:
        pass
    else:
        pass

    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 3
