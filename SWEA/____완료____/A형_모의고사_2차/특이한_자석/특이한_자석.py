import sys
import pprint

sys.stdin = open("특이한_자석")


def calc(current, diff):
    current += diff
    return current % 8


def solution(current, clockwise):
    global status, avail
    avail[current] = 0
    # 일단 양 옆을 돌려야 할 지 보고 재귀를 던진 후에
    if current < 3 and avail[current + 1]:
        if status[current][calc(center[current], 2)] != status[current + 1][calc(center[current + 1], -2)]:
            solution(current+1, -clockwise)
    if current > 0 and avail[current - 1]:
        if status[current][calc(center[current], -2)] != status[current - 1][calc(center[current - 1], +2)]:
            solution(current-1, -clockwise)
    # 내가 돈다
    center[current] = calc(center[current], -clockwise)


for tc in range(int(input())):
    K = int(input())
    status = [list(map(int, input().split())) for i in range(4)]
    center = [0, 0, 0, 0]
    for _ in range(K):
        index, direction = map(int, input().split())
        avail = [1, 1, 1, 1]
        solution(index - 1, direction)
    answer = 0
    for i in range(4):
        if status[i][center[i]]:
            answer += 2 ** i
    print("#{} {}".format(tc + 1, answer))

# 1 10
# 2 14
# 3 3
# 4 13
# 5 15
# 6 10
# 7 2
# 8 6
# 9 5
# 10 4







# 인접 자석 확인
di = [-1, 1]
dj = [2, 6]
dn = [6, 2]

# 시계 방향 회전
# 반시계 회전
def rotate_magnet(num, direction):
    global magnets
    if direction == 1:
        tmp = magnets[num].pop()
        magnets[num] = [tmp] + magnets[num]
    else:
        tmp = magnets[num].pop(0)
        magnets[num] = magnets[num] + [tmp]


# 인접 자석들의 자성 확인
def check_mg_force(num, direction):
    global used, di, dj, dn
    used[num] = 1
    for d in range(2):
        now_mg_force = dn[d]
        ni = num + di[d]
        nj = dj[d]
        if 0 <= ni < 4 and used[ni] == 0:
            if magnets[ni][nj] != magnets[num][now_mg_force]:
                check_mg_force(ni, direction * -1)
    rotate_magnet(num, direction)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    rotation_info = [list(map(int, input().split())) for _ in range(K)]

    for rot in rotation_info:
        # 인접 자석의 자성 확인
        mg_num = rot[0] - 1
        direction = rot[1]
        used = [0] * 4
        check_mg_force(mg_num, direction)

    ans = 0
    points = [1, 2, 4, 8]
    for i in range(4):
        if magnets[i][0] == 1:
            ans += points[i]
    print('#{} {}'.format(tc, ans))