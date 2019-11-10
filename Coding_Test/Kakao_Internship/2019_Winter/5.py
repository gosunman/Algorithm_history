def solution(stones, k):
    possible = 200000000
    index = 0
    while index < len(stones)-k+1:
        temp_possible = -1
        temp_index = -1
        for temp in range(k):
            if stones[index + temp] > temp_possible:
                temp_possible = stones[index + temp]
                temp_index = index + temp
        if temp_possible <= possible:
            possible = temp_possible
        index = temp_index + 1
    answer = possible
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
