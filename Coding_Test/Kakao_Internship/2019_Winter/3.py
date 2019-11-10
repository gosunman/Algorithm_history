def combination(depth, limit, store, candidates, answer):
    if depth != limit:
        for index in range(len(candidates[depth])):
            if candidates[depth][index] not in store:
                store.add(candidates[depth][index])
                combination(depth+1, limit, store, candidates, answer)
                store.remove(candidates[depth][index])
    else:
        if store not in answer:
            answer.append(set(list(store)))

def solution(user_id, banned_id):
    answer = []
    user_id_by_length = [[] for _ in range(9)]
    candidates = [[] for _ in range(len(banned_id))]
    for user in user_id:
        user_id_by_length[len(user)].append(user)
    for bann_index in range(len(banned_id)):
        bann = banned_id[bann_index]
        for user in user_id_by_length[len(bann)]:
            for index in range(len(bann)):
                if user[index] != bann[index] and bann[index] != '*':
                    break
            else:
                candidates[bann_index].append(user)
    combination(0, len(candidates), set(), candidates, answer)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))