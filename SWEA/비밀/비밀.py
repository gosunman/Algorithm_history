import sys
import timeit
import pprint

sys.stdin = open('비밀', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    n_kids, n_secrets = map(int, input().split())
    tables = [[0 for _ in range(n_kids)] for __ in range(n_kids)]
    for secret in range(n_secrets):
        temp_input = list(map(int, input().split()))
        for kid in range(temp_input[0] - 1):
            kid_from = temp_input[kid + 1]
            kid_to = temp_input[kid + 2]
            tables[kid_from - 1][kid_to - 1] = 1

    answer1 = [str(sum(tables[kid])) for kid in range(n_kids)]

    answer2 = 0
    for start in range(n_kids):
        for end in range(n_kids):
            if tables[start][end] > answer2:
                answer2 = tables[start][end]
    print("#{} {} {}".format(testCase + 1, " ".join(answer1), answer2))
    pprint.pprint(tables)

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 2 2 4 0 2 1 3 1 1 5 10
