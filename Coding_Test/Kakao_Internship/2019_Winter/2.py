def solution(s):
    answer = []
    candidates = {}
    size_s = len(s)
    temp = []
    start = 2
    for index in range(2,size_s-1):
        if s[index] == '}':
            temp = s[start:index]
            temp = list(map(int, temp.split(',')))
            for number in temp:
                if candidates.get(number):
                    candidates[number] += 1
                else:
                    candidates[number] = 1
            start = index + 3
    temp = []
    for key, value in candidates.items():
        temp.append([key,value])
    temp.sort(key=lambda x:x[1], reverse=True)
    for number in temp:
        answer.append(number[0])
    return answer