import sys
import timeit
import pprint

# 솔직히 이 문제는 그냥 배꼈다.. 양심의 가책..ㅠ
sys.stdin = open('우주신의_N_Rooks', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_table, M = map(int, input().split())
    N_table %= M
    memoization = [0, 0, 1] + [0] * N_table
    for i in range(3, N_table+1):
        memoization[i]= ((i-1) * (memoization[i-1]+memoization[i-2])) % M
    print("#{} {}".format(testCase + 1, (memoization[N_table]**2)%M))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# f(n) = f(n-1) * (n-1)
#      + ((n-1) ** 2 - (n-1))

#1 4
#2 691009
#3 198011
#4 558487
#5 0
#6 1
#7 81
#8 114
#9 533
#10 400
#11 235
#12 30
#13 186
#14 226
#15 581964
#16 903369
#17 957643
#18 120625
#19 980651
#20 89555
#21 293935
#22 412009
#23 195380
#24 53009
#25 234722
#26 516036
#27 614522
#28 402525
#29 848115
#30 485
#31 812
#32 226
#33 813560
#34 630448
#35 795304