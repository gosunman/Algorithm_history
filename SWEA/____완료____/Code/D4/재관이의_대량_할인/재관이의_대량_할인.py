import sys
import timeit
import pprint

sys.stdin = open('재관이의_대량_할인', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_clothes = int(input())
    S_clothes = list(map(int, input().split()))
    count = 0
    price = 0
    S_clothes.sort(reverse=True)
    for cloth in S_clothes:
        count += 1
        if count % 3 != 0:
            price += cloth
    print("#{} {}".format(testCase + 1, price))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 8
#2 21