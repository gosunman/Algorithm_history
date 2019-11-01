import sys
import timeit
import pprint

sys.stdin = open('수의_새로운_비교_기준', 'r')

start_time = timeit.default_timer()


for testCase in range(int(input())):
    sample = list(map(int, input()))
    digit_sample = len(sample)
    count = 0

    # 조건 1에 해당하는 수 카운트
    eachSum = sum(sample)

    # 조건 2에 해당하는 수 카운트
    eachMultiply = 1
    for index in range(digit_sample):
        eachMultiply *= (sample[index]+1)

    print("#{} {}".format(testCase + 1, eachMultiply))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 4
# 2 5
# 3 6
# 4 98
# 5 99
# 6 100
# 7 5
# 8 6
# 9 8
# 10 718
# 11 719
# 12 781
# 13 298
# 14 3847857
# 15 6743396
# 16 4785027
# 17 46289229750
# 18 4281026355383
# 19 4282262085262
# 20 100000000000000
