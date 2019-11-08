import sys
import timeit
import pprint

sys.stdin = open('금속막대', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    qnt_parts = int(input())
    temp_input = list(map(int, input().split()))
    parts = [temp_input[2 * qnt:2 * (qnt + 1)] for qnt in range(qnt_parts)]
    temp_answer = [parts.pop()]
    qnt_parts -= 1
    while qnt_parts != 0:
        for qnt in range(qnt_parts):
            if parts[qnt][0] == temp_answer[-1][1]:
                qnt_parts -= 1
                temp_answer.append(parts.pop(qnt))
                break
        else:
            break
    while qnt_parts != 0:
        for qnt in range(qnt_parts):
            if parts[qnt][1] == temp_answer[0][0]:
                qnt_parts -= 1
                temp_answer.insert(0, parts.pop(qnt))
                break
        else:
            break
    answer = []
    for temp in temp_answer:
        answer.append(" ".join(list(map(str, temp))))
    print("#{} {}".format(testCase + 1, " ".join(answer)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 2 3 3 4 4 5
# 2 5 1 1 2 2 4 4 3
# 3 9 5 5 8 8 1 1 2 2 3 3 7
# 4 12 2 2 5 5 6 6 9 9 10 10 11 11 1 1 8 8 4 4 15
# 5 1 6 6 11 11 10 10 2 2 15 15 17 17 7 7 14
# 6 13 15 15 12 12 11 11 7 7 4 4 18 18 6 6 16 16 1 1 10
# 7 7 11 11 15 15 8 8 6 6 3 3 12 12 4 4 14 14 10 10 19 19 1 1 13 13 20
# 8 2 1 1 22 22 10 10 17 17 25 25 3 3 4 4 13 13 15 15 12 12 8 8 9 9 11 11 18 18 23
# 9 26 15 15 3 3 7 7 16 16 9 9 6 6 21 21 14 14 4 4 10 10 17 17 18 18 20 20 23 23 27 27 11 11 8 8 2
# 10 20 10 10 21 21 8 8 29 29 28 28 30 30 12 12 14 14 5 5 6 6 15 15 22 22 9 9 16 16 11 11 25 25 4 4 13 13 2 2 1
