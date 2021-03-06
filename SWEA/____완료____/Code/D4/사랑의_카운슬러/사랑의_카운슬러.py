import sys
import timeit
import pprint

sys.stdin = open('사랑의_카운슬러', 'r')

start_time = timeit.default_timer()


def solution(index, p, m, count, sum_x, sum_y):
    global S_warms, answer, N_warms, available
    if count != N_warms:
        if p < N_warms // 2:
            solution(index + 1, p + 1, m, count + 1, sum_x + S_warms[index][0], sum_y + S_warms[index][1])
        if m < N_warms // 2:
            solution(index + 1, p, m + 1, count + 1, sum_x - S_warms[index][0], sum_y - S_warms[index][1])
    else:
        temp_answer = sum_x ** 2 + sum_y ** 2
        if temp_answer < answer:
            answer = temp_answer


for testCase in range(int(input())):
    N_warms = int(input())
    S_warms = [list(map(int, input().split())) for _ in range(N_warms)]
    available = [1 for _ in range(N_warms)]
    answer = float('inf')
    solution(0, 0, 0, 0, 0, 0)
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 80000000000
# 2 754
# 3 1109
# 4 4
# 5 145
# 6 1108
# 7 20
# 8 9125
# 9 2
# 10 221
# 11 3250
# 12 0
# 13 97
# 14 14240
# 15 32393
# 16 277
# 17 482
# 18 53
# 19 233
# 20 1
# 21 6786
# 22 5
# 23 5
# 24 13
# 25 772
# 26 25
# 27 680
# 28 801
# 29 0
# 30 1
# 31 924743972
# 32 20279935376
# 33 2702912
# 34 22099762
# 35 171594482
# 36 383665
# 37 15695941
# 38 2325793
# 39 14593657
# 40 4161177
# 41 7554548
# 42 12182641
# 43 140448977
# 44 10714540797
# 45 83250521
# 46 807362914
# 47 4251466
# 48 22235090
# 49 11305510490
# 50 78594385
# 51 827761
# 52 9967392
# 53 267007277
# 54 2814513050
# 55 5912469
# 56 17425386625
# 57 2922169
# 58 3966002
# 59 64089001
# 60 197865
# 61 2800066505
# 62 104525
# 63 21102594893
# 64 6321781
# 65 191412637
# 66 379753837
# 67 26333968
# 68 3453785
# 69 2537719733
# 70 7051471249
# 71 1046487604
# 72 1873909517
# 73 3554266
# 74 85604026
# 75 48104516
# 76 303830113
# 77 6584474
# 78 3360916
# 79 13425782578
# 80 2591052130
# 81 11316517
# 82 1055156680
# 83 3677572
# 84 14704121
# 85 64068725
# 86 468014276
# 87 197281453
# 88 8010536
# 89 44414569377
# 90 12960
# 91 4617637
# 92 602801428
# 93 179101298
# 94 780795469
# 95 35374393
# 96 4236836
# 97 1143676250
# 98 7591323554
# 99 2869310093
# 100 2292250
