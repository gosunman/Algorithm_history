N = int(input())
sweet = list(map(int, input().split(" ")))

result = 0
maxV = []
for i in range(len(sweet)):
    if result + sweet[i] > result:
        result = result + sweet[i]
    elif result + sweet[i] < result:
        maxV.append(result)
        result = max(sweet[i], result + sweet[i], 0)
print(max(result, max(maxV)))
