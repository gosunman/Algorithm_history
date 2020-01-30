import sys
import timeit
import pprint

sys.stdin = open('../../problem_list.txt', 'r')

start_time = timeit.default_timer()


def combination(depth, limit, store, count):
    global checklist, m
    if depth < limit != count:
        store.append(depth)
        combination(depth + 1, limit, store, count + 1)
        store.pop()
        combination(depth + 1, limit, store, count)
    else:
        if limit == count:
            checklist.append(store)


def solution(n, m):
    # 관계도
    status_input = [list(map(int, input().split())) for _ in range(n)]

    # 최소 음식 경우의 수가 i 인경우
    for i in range(1, m + 1):
        # 확인해봐야 할 조합의 모음
        checklist = []
        combination(0, i, [], 0)
        for onelist in checklist:
            count = 0
            status_friends = [1 for _ in range(n)]
            for food in range(i):
                for friend in range(n):
                    if status_input[friend][onelist[i]] and status_friends[friend]:
                        status_friends[friend] = 0
                        count += 1
            if count == n:
                return True

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))
