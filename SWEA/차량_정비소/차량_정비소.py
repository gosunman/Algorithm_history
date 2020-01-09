import sys
import timeit
import pprint

sys.stdin = open('차량_정비소', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_receptions, N_mechanics, N_customer, first_N, second_N = map(int, input().split())
    first_N -= 1
    second_N -= 1
    S_receptions = list(map(int, input().split()))
    S_mechanics = list(map(int, input().split()))
    S_customers = list(map(int, input().split()))
    N_complete = 0
    time = 0
    while N_complete == N_customer:
        time += 1

        pass
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 7
#3 2
#4 22
#5 18
#6 15
#7 -1
#8 259
#9 100
#10 164