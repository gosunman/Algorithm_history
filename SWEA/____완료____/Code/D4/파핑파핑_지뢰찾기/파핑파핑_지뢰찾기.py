dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for tc in range(int(input())):
    size = int(input())
    # 입력받은 데이터 필드
    ground = [list(input()) for _ in range(size)]

    # 기본값으로 1을 갖는 NXN 행렬을 생성한다
    # 지뢰는 2로 지뢰 주변은 0으로 치환한다
    checked = [[1 for _ in range(size)] for __ in range(size)]
    for y in range(size):
        for x in range(size):
            if ground[y][x] == '*':
                checked[y][x] = 2
                for _ in range(8):
                    i, j = x + dx[_], y + dy[_]
                    if 0 <= i < size and 0 <= j < size and ground[j][i] == '.':
                        checked[j][i] = 0

    cnt = 0
    for y in range(size):
        for x in range(size):
            if checked[y][x] == 1 and ground[y][x]:
                cnt += 1
                ground[y][x] = 0
                stack = [[x, y]]
                while stack:
                    temp = []
                    while stack:
                        point = stack.pop()
                        for _ in range(8):
                            i, j = point[0] + dx[_], point[1] + dy[_]
                            if 0 <= i < size and 0 <= j < size and ground[j][i]:
                                if checked[j][i] == 1:
                                    ground[j][i] = 0
                                    temp.append([i, j])
                                if checked[j][i] == 0:
                                    ground[j][i] = 0
                    stack.extend(temp)

    for y in range(size):
        for x in range(size):
            if checked[y][x] == 0 and ground[y][x]:
                cnt += 1

    print(f"#{tc + 1} {cnt}")