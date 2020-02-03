import sys
import timeit
import pprint

sys.stdin = open('진수의_홀수_약수', 'r')

start_time = timeit.default_timer()

MAX = 10 ** 6 + 1
DP = [0] * MAX
for i in range(1, MAX, 2):
    for j in range(i, MAX, i):
        DP[j] += i

for i in range(1, MAX):
    DP[i] += DP[i - 1]

answer = []

for testCase in range(int(input())):
    S, E = map(int, input().split())
    ans = DP[E] - DP[S - 1]
    answer.append("#{} {}".format(testCase + 1, ans))

print('\n'.join(answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 32
#2 411233508408