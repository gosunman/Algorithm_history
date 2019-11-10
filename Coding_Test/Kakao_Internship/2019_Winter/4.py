def solution(k, room_number):
    room_status = [0 for _ in range(k + 1)]
    answer = []
    full = {}
    for room in room_number:
        if room_status[room]:
            pass
        else:
            room_status[room] = 1
            for key in full.keys():

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
