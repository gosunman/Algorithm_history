import sys
import timeit
import pprint

sys.stdin = open('입국심사', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_windows, N_guests = map(int, input().split())
    S_windows = []
    time, complete = 0, 0
    for i in range(N_windows):
        S_windows.append(int(input()))
    status = S_windows[:]
    while complete < N_guests:
        min_temp = min(status)
        for i in range(N_windows):
            status[i] -= min_temp
            if status[i] == 0:
                complete += 1
                status[i] = S_windows[i]
        time += min_temp
    print("#{} {}".format(testCase + 1, time))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 28
#2 8