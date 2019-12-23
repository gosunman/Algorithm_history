import sys
import timeit
import pprint

sys.stdin = open('동철이의_일_분배', 'r')

start_time = timeit.default_timer()

# def solution(depth, limit, temp, checked):
#     global N_workers, S_workers, answer
#     if depth != limit:
#         for i in range(N_workers):
#             if i not in checked:
#                 checked.add(i)
#                 solution(depth+1, limit, temp * S_workers[depth][i], checked)
#                 checked.remove(i)
#     else:
#         if answer < temp * 100 / 100 ** N_workers:
#             answer = temp * 100 / 100 ** N_workers
#
#
# for testCase in range(int(input())):
#     N_workers = int(input())
#     S_workers = [list(map(int, input().split())) for _ in range(N_workers)]
#     answer = 0
#     solution(0, N_workers, 1, set())
#     print("#{} {}".format(testCase + 1, answer))

# for t in range(int(input())):
#     N = int(input())
#     M = 1 <<
#     D = [0] * M
#     P = [[*map(lambda x: x / 100, map(int, input().split()))] for _ in range(N)]
#     D[0] = 1
#     for mask in range(M):
#         x = sum(1 for i in range(N) if mask & (1 << i))
#         for j in range(N):
#             if mask & (1 << j) == 0:
#                 D[mask | (1 << j)] = max(D[mask | (1 << j)], D[mask] * P[x][j])
#     print(f'#{t + 1} {D[-1] * 100:.6f}')

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 49.654560
# 2 23.362170
# 3 32.000000
# 4 33.804489
# 5 16.695905
# 6 14.878080
# 7 4.559360
# 8 7.764233
# 9 26.789666
# 10 76.560000
# 11 19.489284
# 12 25.181660
# 13 67.000000
# 14 14.040000
# 15 21.488128
# 16 34.278240
# 17 6.189212
# 18 12.970662
# 19 28.549075
# 20 37.813679
# 21 46.307253
# 22 39.797439
# 23 5.075905
# 24 37.557568
# 25 15.988088
# 26 22.015688
# 27 31.856192
# 28 23.778334
# 29 23.581429
# 30 20.113700
# 31 26.600000
# 32 26.078000
# 33 20.622060
# 34 16.872283
# 35 35.033252
# 36 30.348098
# 37 33.965260
# 38 33.542208
# 39 13.736614
# 40 22.231788
# 41 4.178958
# 42 22.400000
# 43 55.936000
# 44 18.668475
# 45 18.131850
# 46 2.400000
# 47 39.195744
# 48 10.475240
# 49 32.743776
# 50 21.234458
# 51 30.237106
# 52 11.228596
# 53 24.089677
# 54 22.932000
# 55 54.676845
# 56 7.023033
# 57 21.560309
# 58 41.031000
# 59 44.490831
# 60 14.886565
# 61 8.983858
# 62 15.788337
# 63 15.846600
# 64 9.230216
# 65 17.922985
# 66 37.840043
# 67 36.860000
# 68 7.013812
# 69 23.478406
# 70 29.779862
# 71 21.312195
# 72 18.462413
# 73 36.643353
# 74 25.444800
# 75 29.290724
# 76 14.004941
# 77 17.825122
# 78 18.588696
# 79 24.624805
# 80 32.472000
# 81 12.918100
# 82 33.080372
# 83 40.936541
# 84 6.915493
# 85 40.423120
# 86 7.200000
# 87 22.260213
# 88 15.804036
# 89 39.452689
# 90 35.491431
# 91 14.089721
# 92 16.558484
# 93 12.369000
# 94 15.203746
# 95 46.773845
# 96 59.030400
# 97 47.819439
# 98 26.329560
# 99 16.493861
# 100 32.439375
