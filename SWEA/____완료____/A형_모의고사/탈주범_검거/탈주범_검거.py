import sys
import timeit
import pprint

sys.stdin = open('탈주범_검거', 'r')

start_time = timeit.default_timer()

ds = [[0, -1], [0, 1], [-1, 0], [1, 0]]

pipes = {0: [],
         1: [0, 1, 2, 3],
         2: [0, 1],
         3: [2, 3],
         4: [0, 3],
         5: [1, 3],
         6: [1, 2],
         7: [0, 2]}

counter = [1, 0, 3, 2]

for testCase in range(int(input())):
    y_limit, x_limit, y_start, x_start, t_limit = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(y_limit)]
    t = 0
    stack = [[x_start, y_start]]
    answer = 0
    while t < t_limit and stack:
        t += 1
        temp_stack = []
        while stack:
            base_x, base_y = stack.pop()
            if table[base_y][base_x]:
                for ele in pipes[table[base_y][base_x]]:
                    dx, dy = ds[ele]
                    new_x, new_y = base_x + dx, base_y + dy
                    if 0 <= new_x < x_limit and 0 <= new_y < y_limit:
                        if counter[ele] in pipes[table[new_y][new_x]]:
                            temp_stack.append([new_x, new_y])
                table[base_y][base_x] = 0
                answer += 1
        stack += temp_stack
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 5
# 2 15
# 3 29
# 4 67
# 5 71


# pipe_info = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
# check = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# for t in range(int(input())):
#     y_max, x_max, y_start, x_start, time = map(int, input().split())
#     status = [list(map(int, input().split())) for _ in range(y_max)]
#     visited = [[True for __ in range(x_max)] for _ in range(y_max)]
#     stack = [[x_start, y_start]]
#     visited[y_start][x_start] = False
#     cnt = 1
#     past = 1
#     while stack and past < time:
#         temp_stack = []
#         while stack:
#             x_start, y_start = stack.pop()
#             pipe = status[y_start][x_start]
#             for propagation in pipe_info[pipe]:
#                 new_y = y_start + dy[propagation]
#                 new_x = x_start + dx[propagation]
#                 if 0 <= new_y < y_max and 0 <= new_x < x_max and visited[new_y][new_x]:
#                     if status[new_y][new_x] in check[propagation]:
#                         temp_stack.append([new_x, new_y])
#                         visited[new_y][new_x] = False
#                         cnt += 1
#         stack.extend(temp_stack)
#         past += 1
#     print(f"#{t + 1} {cnt}")
