import sys
import timeit
import pprint

sys.stdin = open('구간_합', 'r')

start_time = timeit.default_timer()

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 정수 수, 구간의 수
    integer_list = list(map(int, input().split()))
    temp = sum(integer_list[:M])
    max_sum, min_sum = temp, temp
    for num in range(N - M):
        temp = temp - integer_list[num] + integer_list[num + M]
        if temp > max_sum:
            max_sum = temp
        elif temp < min_sum:
            min_sum = temp
    print("#" + str(test_case) + " " + str(max_sum - min_sum))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 46
# 2 23
# 3 940

# 23
# 00 01 02 03 04 05 06 07 08 09
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23
