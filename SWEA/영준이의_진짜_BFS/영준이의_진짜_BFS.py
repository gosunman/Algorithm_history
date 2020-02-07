import sys
import timeit
import pprint

sys.stdin = open('영준이의_진짜_BFS', 'r')

start_time = timeit.default_timer()


def lineage(n):
    global fathers
    family = [n]
    while n != fathers[n]:
        n = fathers[n]
        family.append(n)
    return family


for testCase in range(int(input())):
    N = int(input())
    fathers = [n for n in range(N+1)]
    inputs = list(map(int, input().split()))
    for i in range(N-1):
        fathers[i+2] = inputs[i]
    last_lineage = [1]
    answer = 0
    for i in range(2, N+1):
        new_lineage = lineage(i)
        count = 1
        while last_lineage[-count] == new_lineage[-count]:
            count += 1
            if len(last_lineage) < count or len(new_lineage) < count:
                break
        count -= 1
        answer += len(new_lineage) + len(last_lineage) - count * 2
        last_lineage = new_lineage
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 6
# 2 4
# 3 25
