import sys
import timeit
import pprint

sys.stdin = open('줄기세포_배양.txt', 'r')

start_time = timeit.default_timer()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def write_info(x, y, life, current_life, database):
    if database.get(x):
        if database[x].get(y):
            if database[x][y][0] < life:
                database[x][y] = [life, current_life]
        else:
            database[x][y] = [life, current_life]
    else:
        database[x] = {y: [life, current_life]}


def erase_info(x, y, database):
    if len(database[x].keys()) == 1:
        del database[x]
    else:
        del database[x][y]


def run_simulation(test_group, exception_group):
    add_candidates_info = {}
    del_candidates_info = {}
    for x, temp in test_group.items():
        for y, info in temp.items():
            test_group[x][y][1] -= 1
            life, current_life = test_group[x][y]
            if current_life == -1:
                for direction in range(4):
                    new_x = x + dx[direction]
                    new_y = y + dy[direction]
                    write_info(new_x, new_y, life, life, add_candidates_info)
            if current_life == -life:
                write_info(x, y, life, life, exception_group)
                write_info(x, y, life, life, del_candidates_info)
    for x, temp in add_candidates_info.items():
        for y, info in temp.items():
            if exception_group.get(x):
                if exception_group[x].get(y):
                    pass
                else:
                    write_info(x, y, info[0], info[0], test_group)
            else:
                write_info(x, y, info[0], info[0], test_group)
    for x, temp in del_candidates_info.items():
        for y, info in temp.items():
            if info_cells.get(x) and info_cells[x].get(y):
                erase_info(x, y, test_group)


for testCase in range(int(input())):
    size_row, size_column, last_round = map(int, input().split())
    temp_table = [list(map(int, input().split())) for _ in range(size_row)]
    info_cells = {}
    exception_group = {}
    for y in range(size_row):
        for x in range(size_column):
            life = temp_table[y][x]
            if life:
                write_info(x, y, life, life, info_cells)
                write_info(x, y, life, life, exception_group)
    for _ in range(last_round+1):
        print(f"{_} round:")
        print(info_cells)
        print(exception_group)
        run_simulation(info_cells, exception_group)
    print("#{} {}".format(testCase + 1, len(info_cells)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 22
# 2 36
# 3 90
# 4 164
# 5 712
