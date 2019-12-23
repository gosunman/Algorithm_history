import sys
import timeit
import pprint

sys.stdin = open('수제_버거_장인', 'r')

start_time = timeit.default_timer()


def solution(depth, limit, blacklist):
    global relation, answer
    if depth != limit:
        solution(depth + 1, limit, blacklist)
        if depth not in blacklist:
            solution(depth + 1, limit, blacklist | relation[depth])
    else:
        answer += 1


for testCase in range(int(input())):
    N_materials, N_blacklist = map(int, input().split())
    relation = {i: set() for i in range(N_materials)}
    answer = 0
    for _ in range(N_blacklist):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        relation[a].add(b)
        relation[b].add(a)
    solution(0, N_materials, set())
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 5
# 2 8
# 3 4
