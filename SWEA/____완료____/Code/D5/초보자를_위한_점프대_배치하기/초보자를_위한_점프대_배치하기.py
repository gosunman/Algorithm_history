import sys
import timeit
import pprint

sys.stdin = open('초보자를_위한_점프대_배치하기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_bars = int(input())
    S_bars = sorted(list(map(int, input().split())))
    S_bars.sort()
    ans = 0
    odd_or_even = True
    for i in range(N_bars - 2):
        temp = S_bars[i + 2] - S_bars[i]
        if temp > ans:
            ans = temp
    temp = S_bars[1] - S_bars[0]
    if temp > ans:
        ans = temp
    temp = S_bars[-1] - S_bars[-2]
    if temp > ans:
        ans = temp
    print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 4
# 3 0
