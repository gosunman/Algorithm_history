import sys
import timeit
import pprint

sys.stdin = open('선표의_축구_경기_예측', 'r')

start_time = timeit.default_timer()

combination = []

primenumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def comb(n, p):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    for i in range(1, p + 1):
        answer //= i
    for i in range(1, n - p + 1):
        answer //= i
    return answer


for prime in primenumber:
    combination.append(comb(30, prime))

for testCase in range(int(input())):
    A, B = map(int, input().split())
    A_Prime = 0
    B_Prime = 0
    for index in range(10):
        p = primenumber[index]
        A_Prime += combination[index] * (A ** p) * ((100 - A) ** (30 - p))
        B_Prime += combination[index] * (B ** p) * ((100 - B) ** (30 - p))
    answer = A_Prime / (100 ** 30) + B_Prime / (100 ** 30)
    answer -= A_Prime * B_Prime / (100 ** 60)
    print("#{} {:.5f}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 0.54942
# 2 0.60795
# 3 0.00000
