def solution(message, K):
    if len(message) <= K:
        return message
    else:
        if message[K] == ' ':
            return message[:K]
        else:
            while message[K] != ' ' and K != 0:
                K -= 1
            if K == 0:
                return message[:0]
            else:
                return message[:K]