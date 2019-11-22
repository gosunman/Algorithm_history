import sys
import timeit
import pprint

sys.stdin = open('롤러코스터', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_rails = int(input())
    info_rails = []
    for _ in range(qnt_rails):
        info_rails.append(list(map(int, input().split())))
    
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 14
#2 1242
#3 27