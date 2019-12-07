candidates = []


def suffle(depth, limit, samples):
    if depth != limit:
        for index in range(depth, limit):
            samples[depth], samples[index] = samples[index], samples[depth]
            if depth == 0:
                if samples[depth] in [0, 1, 2]:
                    suffle(depth + 1, limit, samples)
            elif depth == 1:
                if samples[depth - 1] in [0, 1]:
                    suffle(depth + 1, limit, samples)
                elif samples[depth - 1] == 2 and samples[depth] in [0, 1, 2, 3]:
                    suffle(depth + 1, limit, samples)
            elif depth == 2:
                if samples[depth] in [0, 1, 2, 3, 4, 5]:
                    suffle(depth + 1, limit, samples)
            else:
                suffle(depth + 1, limit, samples)
            samples[depth], samples[index] = samples[index], samples[depth]
    else:
        if samples not in candidates:
            candidates.append(samples[:])


def solution(A, B, C, D):
    temporary = []
    suffle(0, 4, [A, B, C, D])
    return len(candidates)