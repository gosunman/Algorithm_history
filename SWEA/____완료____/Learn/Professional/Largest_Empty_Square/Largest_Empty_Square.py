import sys
import timeit
import pprint

sys.stdin = open('Largest_Empty_Square', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    size_table = int(input())
    status_table = [list(map(int, list(input()))) for _ in range(size_table)]
    answer_table = [[0 for _ in range(size_table)] for __ in range(size_table)]
    answer = 0
    for y in range(size_table):
        for x in range(size_table):
            if status_table[y][x]:
                answer_table[y][x] = 0
            else:
                if y == 0:
                    answer_table[y][x] = 1
                    if answer < 1:
                        answer = 1
                if x == 0:
                    answer_table[y][x] = 1
                    if answer < 1:
                        answer = 1
                else:
                    option1 = answer_table[y - 1][x - 1]
                    option2 = answer_table[y - 1][x]
                    option3 = answer_table[y][x - 1]
                    answer_table[y][x] = min(option1, option2, option3) + 1
                    if answer < answer_table[y][x]:
                        answer = answer_table[y][x]
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 2
