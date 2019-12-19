import sys
import timeit
import pprint

sys.stdin = open('Need_For_Speed', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_sections, T_time = map(int, input().split())
    S_distance = []
    S_velocity = []
    for i in range(N_sections):
        d, v = map(int, input().split())
        S_distance.append(d)
        S_velocity.append(v)
    max_c = 11**8
    min_c = -max(S_velocity)
    c = diff = 0.1
    while True:
        temp_t = 0
        for i in range(N_sections):
            temp_t += S_distance[i]/(S_velocity[i]+c)
        diff = T_time - temp_t
        if diff >= 0.000001:
            max_c = c
            c = (max_c + min_c) / 2
        elif diff <= -0.000001:
            min_c = c
            c = (max_c + min_c) / 2
        else:
            break
    print("#{} {}".format(testCase + 1, c))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3.000000000
#2 -0.508653377
#3 -455.754000000
#4 -0.000000000
#5 5.499619920
#6 -0.000010000
#7 0.000000010
#8 1838.034569345
#9 1001000.0
#10 -999.999999000
#11 943.004490564
#12 -0.998266073386
#13 0.203739063708
#14 -613.992101903
#15 145753.203721
#16 1000.000001
#17 -8.6
#18 999000.0000004