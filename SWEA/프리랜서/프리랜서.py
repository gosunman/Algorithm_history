import sys
import timeit
import pprint

sys.stdin = open('프리랜서', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_tasks, qnt_days = map(int, input().split())
    info_tasks = []
    for _ in range(qnt_tasks):
        d1, d2, w = map(int, input().split())
        info_tasks.append([d1 - 1, d2 - 1, w])
    info_tasks.sort(key=lambda x: (x[1], -x[0]))
    table = [-1 for _ in range(qnt_days)]
    last_point = 0
    for task_index in range(qnt_tasks):
        d1, d2, w = info_tasks[task_index]
        option1 = last_point
        for index in range(d2, d1-1, -1):
            table[index]
        option2 =
    print("#{} {}".format(testCase + 1, info_tasks))
    pprint.pprint(table)

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 49
