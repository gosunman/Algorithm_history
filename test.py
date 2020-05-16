arr = [1, 2, 3, 1, 2]
x = 1
answer = min(arr[:x])
result = [answer]
for i in range(x, len(arr)):
    if arr[i-x] == answer:
        if answer != arr[i]:
            temp = min(arr[i-x+1:i+1])
            answer = temp
            result.append(temp)
print(max(result))
