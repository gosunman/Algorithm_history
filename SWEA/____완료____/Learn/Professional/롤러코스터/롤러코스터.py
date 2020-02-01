import sys
import timeit
import pprint

sys.stdin = open('롤러코스터', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_rails = int(input())
    info_rails = [list(map(int, input().split())) for _ in range(qnt_rails)]
    info_rails.sort(key=lambda x: (x[0]-1)/x[1], reverse=True)
    answer = 1
    for i in range(qnt_rails):
        answer *= info_rails[i][0]
        answer += info_rails[i][1]
        answer %= 1000000007
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 14
#2 1242
#3 27