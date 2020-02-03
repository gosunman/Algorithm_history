import sys
import timeit
import pprint

sys.stdin = open('무선_단속_카메라', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    _, N_receptor, S_camera = input(), int(input()), sorted(list(set(map(int, input().split()))))
    N_camera = len(S_camera)
    answer = 0
    if N_camera > N_receptor:
        answer = sum(sorted([S_camera[i] - S_camera[i - 1] for i in range(1, N_camera)])[:-N_receptor + 1])
        # N_camera - 1
        # N_camera - 1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 5
