import sys
import timeit
import pprint
from queue import PriorityQueue

sys.stdin = open('Shortest_Path_Faster', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_node, N_edge, start, end = map(int, input().split())
    S_edge = [list(map(int, input().split())) for _ in range(N_edge)]
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 3
