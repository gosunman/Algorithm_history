import sys
import timeit
import pprint

sys.stdin = open('평등주의', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    length_sample, chance = map(int, input().split())
    samples = list(map(int, input().split()))
    candidates = [0 for _ in range(length_sample)]
    maximum_diff = 0
    maximum_index = -1
    for index in range(length_sample - 1):
        candidates[index] = samples[index] - samples[index + 1]
        if candidates[index] > maximum_diff:
            maximum_diff = candidates[index]
            maximum_index = index
    for _ in range(chance):
        pass
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 4
# 3 0

# 1 1
# 2 2
