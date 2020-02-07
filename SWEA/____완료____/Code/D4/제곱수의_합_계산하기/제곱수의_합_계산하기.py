import sys
import timeit
import pprint

sys.stdin = open('제곱수의_합_계산하기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N = int(input())
    S = input().split()
    answer = 0
    for i in range(N):
        answer += int(S[i][:-1]) ** int(S[i][-1])
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1953566
#2 102
#3 10385