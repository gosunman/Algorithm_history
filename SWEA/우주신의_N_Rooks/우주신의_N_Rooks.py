import sys
import timeit
import pprint

sys.stdin = open('우주신의_N_Rooks', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_table, M = map(int, input().split())

    print("#{} {} {}".format(testCase + 1, 0, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

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

# #include <cstdio>
# int DP[1000001];
# int main() {
#     int T, M;
#     long long N;
#     scanf("%d", &T);
#     for (int tc = 1; tc <= T; tc++) {
#         scanf("%lld %d", &N, &M);
#         N %= M;
#         if (N == 0) N = M;
#         DP[1] = 0;
#         for (int i = 2; i <= N; i++)
#             DP[i] = ((long long)DP[i - 1] * i + (i & 1 ? -1 : 1)) % M;
#         printf("#%d %d\n", tc, ((long long)DP[N] * DP[N]) % M);
#     }
# }