N = int(input())
skills = {}
for i in range(N):
    key = tuple(map(int, input().split()))
    skills[key] = i
# skills = {(1,4):0,
#           (2,3):1,
#           (5,8):2}
temp = sorted(skills.keys(), key=lambda x: x[0])

for i in range(N):
    cnt = 0
    for k in range(i):
        if temp[k][1] < temp[i][0]:
            cnt += 1
    skills[temp[i]] = i - cnt
for val in skills.values():
    print(val)
