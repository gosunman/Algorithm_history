import sys
import pprint

sys.stdin = open("활주로_건설")

for tc in range(int(input())):
    answer = 0
    N, X = map(int, input().split())
    status = [list(map(int, input().split())) for i in range(N)]
    status += list(map(list, zip(*status)))
    for case in range(2 * N):
        line = status[case]
        avail = [1 for i in range(N)]
        index = 0
        while index < N - 1:
            if line[index] == line[index + 1]:
                index += 1
            elif line[index] == line[index + 1] - 1:
                # 앞의 블록이 높은 경우
                if avail[index - X + 1:index + 1] == [1] * X:
                    # 뒤로 X 만큼 블록에 건설한 적이 없고
                    if line[index - X + 1: index + 1] == [line[index]] * X:
                        # 뒤로 X 만큼의 블록이 평탄하다면
                        index += 1
                    else:
                        break
                else:
                    break
            elif line[index] == line[index + 1] + 1:
                # 앞의 블록이 낮은 경우
                if index + X < N:
                    # 그 앞으로 다리를 건설할 땅이 남아 있고
                    if line[index + 1: index + X + 1] == [line[index + 1]] * X:
                        # 그 앞으로 X 만큼의 블록이 평탄하다면
                        for i in range(index + 1, index + X + 1):
                            avail[i] = 0
                        index += X
                    else:
                        break
                else:
                    break
            else:
                # 높이가 2 이상 차이나는 경우이므로 실패
                break
        if index == N - 1:
            answer += 1
    print("#{} {}".format(tc + 1, answer))

# 1 7
# 2 4
# 3 11
# 4 11
# 5 15
# 6 4
# 7 4
# 8 1
# 9 5
# 10 8
