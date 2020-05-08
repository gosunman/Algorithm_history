def find(n):
    if table[n] == n:
        return n
    else:
        find(table[n])


N, M = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(N)]
edge = [list(map(int, input().split())) for _ in range(M)]

table = [n for n in range(N+1)]
for e in edge:
    f, b = e
    if table[b] == b:
        table[b] = f
    else:
        table[b] = find(table[b])

dict = {}
for i in range(1, len(table)):
    if dict.get(table[i]) == None:
        dict[table[i]] = [point[i-1]]
    else:
        dict[table[i]].append(point[i-1])
maxV = 0
for val in dict.values():
    X, Y = [], []
    for v in val:
        X.append(v[0])
        Y.append(v[1])
    lx = max(X) - min(X)
    ly = max(Y) - min(Y)
    temp = (lx + ly)*2
    maxV = max(maxV, temp)
print(maxV)
