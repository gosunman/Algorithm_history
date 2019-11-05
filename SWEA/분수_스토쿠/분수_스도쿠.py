import sys
import timeit
import pprint

sys.stdin = open('분수_스도쿠', 'r')

start_time = timeit.default_timer()

def solution(x, y):
    global ans_table
    candidates = list(map(str, range(1, 10)))
    target_count = ans_table[y][x].count('-')
    current_count = 9
    row = [[], [], []]
    column = [[], [], []]
    group = [[], [], []]
    for _ in range(6):
        for element in ans_table[y][_]:
            if '-' in element:
                if '/' in element:
                    if '-' in element[0]:
                        row[1].append(_)
                    if '-' in element[2]:
                        row[2].append(_)
                else:
                    row[0].append(_)
            if element in candidates:
                candidates.remove(element)
                current_count -= 1
                if current_count == target_count:
                    break
        if current_count == target_count:
            break

        for element in ans_table[_][x]:
            if '-' in element:
                if '/' in element:
                    if '-' in element[0]:
                        column[1].append(_)
                    if '-' in element[2]:
                        column[2].append(_)
                else:
                    column[0].append(_)
            if element in candidates:
                candidates.remove(element)
                current_count -= 1
                if current_count == target_count:
                    break
        if current_count == target_count:
            break

    pivot_x, pivot_y = x // 3, y // 2
    pivot_x *= 3
    pivot_y *= 2
    for new_x in range(3):
        for new_y in range(2):
            for element in ans_table[pivot_y + new_y][pivot_x + new_x]:
                if '-' in element:
                    if '/' in element:
                        if '-' in element[0]:
                            group[1].append([pivot_x + new_x,pivot_y + new_y])
                        if '-' in element[2]:
                            group[2].append([pivot_x + new_x,pivot_y + new_y])
                    else:
                        group[0].append([pivot_x + new_x,pivot_y + new_y])
                if element in candidates:
                    candidates.remove(element)
                    current_count -= 1
                    if current_count == target_count:
                        break
            if current_count == target_count:
                break
        if current_count == target_count:
            break


    if current_count == target_count:
        if target_count == 2:
            candidates.sort()
            ans_table[y][x] = ans_table[y][x].replace('-', candidates[0], 1)
            ans_table[y][x] = ans_table[y][x].replace('-', candidates[1], 1)
            return True
        else:
            ans_table[y][x] = ans_table[y][x].replace('-', candidates[0], 1)
            return True
    else:
        if target_count == 1 and '/' in ans_table[y][x]:
            if ans_table[y][x].index('-') == 0:
                if candidates[0] < ans_table[y][x][2] < candidates[1]:
                    ans_table[y][x] = ans_table[y][x].replace('-', candidates[0], 1)
                    return True
            else:
                if candidates[-1] > ans_table[y][x][0] > candidates[-2]:
                    ans_table[y][x] = ans_table[y][x].replace('-', candidates[-1], 1)
                    return True

    row_state = False
    if not row[0]:
        if len(row[1]) == 1 and row[1] == [x] and '1' in candidates:
            candidates.remove('1')
            ans_table[y][x][0] = '1'
            row_state = True
        if len(row[2]) == 1 and row[2] == [x] and '9' in candidates:
            candidates.remove('9')
            ans_table[y][x][2] = '9'
            row_state = True
    if row_state:
        return True

    column_state = False
    if not column[0]:
        if len(column[1]) == 1 and column[1] == [y] and '1' in candidates:
            candidates.remove('1')
            ans_table[y][x][0] = '1'
            column_state = True
        if len(column[2]) == 1 and column[2] == [y] and '9' in candidates:
            candidates.remove('9')
            ans_table[y][x][2] = '9'
            column_state = True
    if column_state:
        return True

    group_state = False
    if not group[0]:
        if len(group[1]) == 1 and group[1] == [[x, y]] and '1' in candidates:
            candidates.remove('1')
            ans_table[y][x][0] = '1'
            group_state = True
        if len(group[2]) == 1 and group[2] == [[x, y]] and '9' in candidates:
            candidates.remove('9')
            ans_table[y][x][2] = '9'
            group_state = True
    if group_state:
        return True


for testCase in range(int(input())):
    ans_table = [input().split() for _ in range(6)]
    incomplete = True
    while incomplete:
        incomplete = False
        for y in range(6):
            for x in range(6):
                if '-' in ans_table[y][x]:
                    incomplete = True
                    solution(x, y)

    print("#{}".format(testCase + 1))
    for _ in range(6):
        print(" ".join(ans_table[_]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# #1
# 7/9 1/5 4 3 2 6/8
# 3 6 2/8 1/9 7 4/5
# 1 7/9 3 4/5 6/8 2
# 8 2/4 5/6 7 1/3 9
# 5/6 3 1/9 2/8 4 7
# 2/4 8 7 6 5/9 1/3
# #2
# 2 6/9 4/8 1/5 3 7
# 1/7 3 5 2 4/8 6/9
# 6/9 8 7 3 2/5 1/4
# 3 4/5 1/2 6/9 7 8
# 5 2/7 6/9 4/8 1 3
# 4/8 1 3 7 6/9 2/5