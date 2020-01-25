import sys
import timeit
import pprint

sys.stdin = open('디오판토스_방정식', 'r')

start_time = timeit.default_timer()


def get_gcd(n, m):
    num = max(a, b)
    divisor = min(a, b)
    while (num % divisor) != 0:
        remainder = num % divisor
        num = divisor
        divisor = remainder
    return divisor


for testCase in range(int(input())):
    x = y = 0
    a, b, c = map(int, input().split())
    gcd = get_gcd(a, b)
    gcm = a * b // gcd
    print("#{} {} {}".format(testCase + 1, x, y))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1 -1
