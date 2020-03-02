import sys
import timeit
import pprint

sys.stdin = open('보물상자_비밀번호', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_inputs, Kth = map(int, input().split())
    limit = N_inputs // 4
    S_inputs = input().strip()
    S_inputs += S_inputs[:limit]
    candidates = set()
    for i in range(limit):
        for j in range(4):
            index = i + limit*j
            candidates.add(S_inputs[index:index+limit])
    candidates = sorted(list(candidates), reverse=True)
    print("#{} {}".format(testCase + 1, str(int(candidates[Kth-1], 16))))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 503
#2 55541
#3 334454
#4 5667473
#5 182189737