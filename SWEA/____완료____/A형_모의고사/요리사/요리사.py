comb_set = [0] * 17


def get_combination(depth, n, history):
    global temp
    if depth >= n:
        if len(history) == n // 2:
            temp.append(history[:])
    else:
        if len(history) == n // 2:
            temp.append(history[:])
        else:
            history.append(depth)
            get_combination(depth + 1, n, history)
            history.remove(depth)
            get_combination(depth + 1, n, history)


for t in range(int(input())):
    ans = 0
    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]
    temp = []
    if not comb_set[size]:
        get_combination(0, size, [])
        comb_set[size] = temp
    ans = 0
    comb1 = comb_set[size][:len(comb_set[size])//2]
    comb2 = comb_set[size][len(comb_set[size])//2:][::-1]
    for index in range(len(comb_set[size])//2):
        comb11 = comb1[index]
        comb22 = comb2[index]
        taste1 = 0
        taste2 = 0
        for i in range(size // 2 - 1):
            for j in range(i + 1, size // 2):
                taste1 += table[comb11[i]][comb11[j]] + table[comb11[j]][comb11[i]]
                taste2 += table[comb22[i]][comb22[j]] + table[comb22[j]][comb22[i]]
        if index == 0:
            ans = abs(taste1 - taste2)
        else:
            if abs(taste1 - taste2) < ans:
                ans = abs(taste1 - taste2)
    print('#{} {}'.format(t + 1, ans))