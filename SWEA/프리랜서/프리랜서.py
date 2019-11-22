import sys
import timeit
import pprint

sys.stdin = open('프리랜서', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_tasks, qnt_days = map(int, input().split())
    info_tasks = []
    for _ in range(qnt_tasks):
        info_tasks.append(list(map(int, input().split())))
    answer = 0
    table = [None for _ in range(qnt_days)]
    for index in range(qnt_tasks):
        start, end = info_tasks[index][:2]
        for day in range(start, end+1):
            pass
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 49