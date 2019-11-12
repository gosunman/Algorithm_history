def solution(i, j, k):
    global ans, size_table, fee, table, tc
    cost = k**2 + (k-1)**2
    cnt = 0
    for y in range(-(k-1), k):
        t = k - abs(y)
        for x in range(-(t-1), t):
            if 0 <= i + x < size_table and 0 <= j + y < size_table:
                if table[j + y][i + x]:
                    cnt += 1
    temp_ans = cnt * fee - cost
    if temp_ans >= 0:
        if cnt > ans:
            ans = cnt


for tc in range(int(input())):
    ans = 1
    size_table, fee = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(size_table)]
    for z in range(2, size_table+2):
        for y in range(size_table):
            for x in range(size_table):
                solution(x, y, z)
    print("#{} {}".format(tc + 1, ans))