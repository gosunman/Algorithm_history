import sys
import timeit
import pprint

sys.stdin = open('입국심사', 'r')

start_time = timeit.default_timer()

for t in range(int(input())):
    N_desks, N_people = map(int, input().split())
    S_desks = [int(input()) for _ in range(N_desks)]
    time = 0
    limit = 2 << 50
    while time < limit:
        middle = (time + limit) >> 1
        N_accepted = sum(middle // i for i in S_desks)
        if N_accepted < N_people:
            time = middle + 1
        else:
            limit = middle
    print('#{} {}'.format(t + 1, time))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 28
# 2 8
