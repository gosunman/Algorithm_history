import sys

sys.stdin = open("러시아_국기_같은_깃발", "r")


def calc(color, y):
    global memory, temp
    if memory[color].get(y):
        temp += memory[color][y]
    else:
        count = 0
        for x in range(M):
            if status[y][x] != color:
                count += 1
        memory[color][y] = count
        temp += count


for tc in range(int(input())):
    N, M = map(int, input().split())
    status = [list(input()) for i in range(N)]
    answer = 50 * 50
    memory = {'R': {}, 'W': {}, 'B': {}}
    for second in range(1, N - 1):
        for third in range(second + 1, N):
            temp = 0
            for color, start, end in [['W', 0, second], ['B', second, third], ['R', third, N]]:
                for y in range(start, end):
                    calc(color, y)
            if temp < answer:
                answer = temp
    print("#{} {}".format(tc + 1, answer))

# 1 11
# 2 44
