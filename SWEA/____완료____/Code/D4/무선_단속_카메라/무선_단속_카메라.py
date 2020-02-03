import sys
import timeit
import pprint

sys.stdin = open('무선_단속_카메라', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_camera = int(input())
    N_receptor = int(input())
    S_camera = sorted(list(map(int, input().split())))
    ans = 0
    if N_camera > N_receptor:
        S_calc = []
        for i in range(1, N_camera):
            S_calc.append(S_camera[i] - S_camera[i - 1])
        S_calc = sorted(S_calc)
        ans = 0
        for i in range(0, N_camera - N_receptor):
            ans += S_calc[i]
    print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 5
