pipe_info = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
check = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for t in range(int(input())):
    y_max, x_max, y_start, x_start, time = map(int, input().split())
    status = [list(map(int, input().split())) for _ in range(y_max)]
    visited = [[True for __ in range(x_max)] for _ in range(y_max)]
    stack = [[x_start, y_start]]
    visited[y_start][x_start] = False
    cnt = 1
    past = 1
    while stack and past < time:
        temp_stack = []
        while stack:
            x_start, y_start = stack.pop()
            pipe = status[y_start][x_start]
            for propagation in pipe_info[pipe]:
                new_y = y_start + dy[propagation]
                new_x = x_start + dx[propagation]
                if 0 <= new_y < y_max and 0 <= new_x < x_max and visited[new_y][new_x]:
                    if status[new_y][new_x] in check[propagation]:
                        temp_stack.append([new_x, new_y])
                        visited[new_y][new_x] = False
                        cnt += 1
        stack.extend(temp_stack)
        past += 1
    print(f"#{t + 1} {cnt}")