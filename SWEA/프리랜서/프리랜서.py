import sys
import timeit
import pprint

sys.stdin = open('프리랜서', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_tasks, qnt_days = map(int, input().split())
    info_tasks = []
    for index in range(qnt_tasks):
        d1, d2, w = map(int, input().split())
        info_tasks.append([d1 - 1, d2 - 1, w])
    info_tasks.sort(key=lambda x: (x[1], -x[0]))
    schedule = [info_tasks[0]]
    last_point = info_tasks[0][2]
    for task_index in range(1, qnt_tasks):
        task = info_tasks[task_index]
        current_index = len(schedule) - 1
        last_index = current_index
        current_point = last_point
        while current_index >= 0 and schedule[current_index][1] >= task[0]:
            current_point -= schedule[current_index][2]
            current_index -= 1
        current_point += task[2]
        if current_point > last_point:
            last_point = current_point
            for index in range(current_index + 1, last_index + 1):
                schedule.pop()
            schedule.append(task)
    print("#{} {}".format(testCase + 1, schedule))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 49
