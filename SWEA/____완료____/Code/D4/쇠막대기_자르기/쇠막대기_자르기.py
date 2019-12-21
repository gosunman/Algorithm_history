import sys
import timeit
import pprint

sys.stdin = open('쇠막대기_자르기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    S = input().strip()
    answer = 0
    count = 0
    for i in range(len(S)):
        if S[i] == '(':
            count += 1
        else:
            count -= 1
            if S[i-1] == ')':
                answer += 1
            else:
                answer += count
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 17
#2 24