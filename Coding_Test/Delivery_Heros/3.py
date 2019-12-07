def solution(S):
    N = len(S)
    count = 0
    a = 0
    possible = True
    for index in range(N):
        if S[index] == 'a':
            a += 1
            if a == 3:
                return -1
        else:
            count += 2-a
            a = 0
    count += 2-a
    return count
