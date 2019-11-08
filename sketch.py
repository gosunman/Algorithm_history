def parent(n):
    while p[n] != n:
        n = p[n]


p = [index for index in range(10)]
