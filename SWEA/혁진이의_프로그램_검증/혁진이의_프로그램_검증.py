import sys
import pprint

sys.stdin = open("혁진이의_프로그램_검증")

for tc in range(int(input())):
    R, C = map(int, input().split())
    status = [list(input()) for i in range(R)]
    stack = [(0, 0, 1, 0, 0)]
    answer = "NO"
    used = {}
    while stack:
        x, y, dx, dy, memory = stack.pop()
        while True:
            if used.get(memory):
                if used[memory].get(x):
                    if used[memory][x].get(y):
                        if used[memory][x][y].get(dx):
                            if used[memory][x][y][dx].get(dy):
                                break
                            else:
                                used[memory][x][y][dx][dy] = 1
                        else:
                            used[memory][x][y][dx] = {dy: 1}
                    else:
                        used[memory][x][y] = {dx: {dy: 1}}
                else:
                    used[memory][x] = {y: {dx: {dy: 1}}}
            else:
                used[memory] = {x: {y: {dx: {dy: 1}}}}

            if status[y][x] == "<":
                dx = -1
                dy = 0
            elif status[y][x] == ">":
                dx = 1
                dy = 0
            elif status[y][x] == "^":
                dx = 0
                dy = -1
            elif status[y][x] == "v":
                dx = 0
                dy = 1
            elif status[y][x] == "_":
                if memory:
                    dx = -1
                    dy = 0
                else:
                    dx = 1
                    dy = 0
            elif status[y][x] == "|":
                if memory:
                    dx = 0
                    dy = -1
                else:
                    dx = 0
                    dy = 1
            elif status[y][x] == "?":
                stack.append([x, y, 0, 1, memory])
                stack.append([x, y, 0, -1, memory])
                stack.append([x, y, 1, 0, memory])
                stack.append([x, y, -1, 0, memory])
                break
            elif status[y][x] == ".":
                pass
            elif status[y][x] == "@":
                answer = "YES"
                stack = []
                break
            elif status[y][x] == "+":
                memory = (memory + 1) % 16
            elif status[y][x] == "-":
                memory = (memory - 1) % 16
            else:
                memory = int(status[y][x])
            x = (x + dx) % C
            y = (y + dy) % C
    print(x, y, dx, dy, memory)
    print("#{} {}".format(tc + 1, answer))

#1 YES
#2 NO
#3 YES

# 1 YES
# 2 NO
# 3 YES
# 4 YES
# 5 YES
# 6 YES
# 7 NO
# 8 NO
# 9 YES
# 10 YES
# 11 YES
# 12 YES
# 13 YES
# 14 NO
# 15 YES
# 16 YES
# 17 YES
# 18 YES
# 19 YES
# 20 YES
# 21 YES
# 22 YES
# 23 YES
# 24 YES
# 25 YES
# 26 YES
# 27 YES
# 28 YES
# 29 YES
# 30 YES
# 31 YES
# 32 YES
# 33 YES
# 34 YES
# 35 NO
# 36 YES
# 37 YES
# 38 YES
# 39 NO
# 40 NO
# 41 YES
# 42 YES
# 43 NO
# 44 YES
# 45 YES
# 46 YES
# 47 YES
# 48 NO
# 49 NO
# 50 YES
# 51 NO
# 52 YES
# 53 YES
# 54 YES
# 55 YES
# 56 YES
# 57 NO
# 58 YES
# 59 YES
# 60 NO
# 61 YES
# 62 YES
# 63 NO
# 64 YES
# 65 YES
# 66 YES
# 67 YES
# 68 YES
# 69 YES
