import sys
import timeit
import pprint

sys.stdin = open('줄기세포_배양', 'r')

start_time = timeit.default_timer()


# 처음은 비활성 상태, 초기 숫자가 X이면, X시간 후 활성 상태가 된다
# 활성 상태가 되면 X 시간 동안 살아 있다가 죽게 된다.
# 세포가 죽더라도 소멸하는 것은 아니며 셀은 차지하고 있는다

# 세포는 활성화 된 직후, 상 하 좌 우로 번식한다.
# 번식된 세포는 비활성화 상태
# 이미 세포가 있는 곳으로는 번식하지 않는다
# 두 개가 동시에 번식하려고 할 때는 생명력 수치가 높은 세포가 차지한다.

# 비활성 + 활성 상태의 세포 수를 구하는 프로그램

def insert(value, store):
    if type(value) == list:
        if store.get(value[0]):
            if store[value[0]].get(value[1]):
                pass
            else:
                store[value[0]][value[1]] = 1
        else:
            store[value[0]] = {value[1]: 1}
    else:
        if store.get(value):
            store[value] += 1

# used = {1:{2:1, 4:1, 6:1},2:{5:1, 7:1}}


def all_around(X, Y):
    return [[X + 1, Y], [X - 1, Y], [X, Y + 1], [X, Y - 1]]


def avail(value, store):
    if type(value) == list:
        if store.get(value[0]):
            if store[value[0]].get(value[1]):
                return False
            else:
                return True
        else:
            return True


for testCase in range(int(input())):
    N, M, K = map(int, input().split())
    time = 0
    count = 0
    used = {}
    temp = [list(map(int, input().split())) for y in range(N)]
    alive = []
    die = {}
    for y in range(N):
        for x in range(M):
            if temp[y][x]:
                count += 1
                insert([x, y], used)
                alive.append([x, y, temp[y][x], time + temp[y][x] + 1])
                insert(time + temp[y][x] * 2, die)
    alive.sort(key=lambda ele: (ele[3], -ele[2]))
    while time < K:
        time += 1
        if die.get(time):
            count -= die[time]
        temp_count = 0
        for i in range(len(alive)):
            if alive[i][3] <= time:
                temp_count += 1
                new_x, new_y = alive[i][:2]
                for coord in all_around(new_x, new_y):
                    if avail(coord, used):
                        x, y = coord
                        count += 1
                        insert([x, y], used)
                        alive.append([x, y, alive[i][2], time + alive[i][2] + 1])
                        insert(time + alive[i][2] * 2, die)
            else:
                break
        alive = alive[temp_count:]
        alive.sort(key=lambda ele: (ele[3], -ele[2]))
    print("#{} {}".format(testCase + 1, count))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 22
# 2 36
# 3 90
# 4 164
# 5 712
