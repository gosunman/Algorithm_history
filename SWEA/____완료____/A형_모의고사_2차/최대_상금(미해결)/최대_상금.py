import sys
import pprint

sys.stdin = open('최대_상금')


def solution(index, limit, target, count):
    global answer
    if count != 0:
        if index != limit - 1:
            biggest = target[index]
            candidate = [index]
            for i in range(index + 1, limit):
                if target[i] > biggest:
                    biggest = target[i]
                    candidate = [i]
                elif target[i] == biggest:
                    candidate.append(i)
            if biggest == target[index]:
                solution(index+1, limit, target, count)
            else:
                for i in candidate:
                    target[i], target[index] = target[index], target[i]
                    solution(index + 1, limit, target, count - 1)
                    target[i], target[index] = target[index], target[i]
        else:
            if count % 2:
                target[-1], target[-2] = target[-2], target[-1]
                solution(index, limit, target, 0)
                target[-1], target[-2] = target[-2], target[-1]
            else:
                solution(index, limit, target, 0)
    else:
        if int("".join(target)) > answer:
            answer = int("".join(target))


for tc in range(int(input())):
    number, chance = input().split()
    answer = int(number)
    number = list(number)
    chance = int(chance)
    solution(0, len(number), number, chance)
    print("#{} {}".format(tc + 1, answer))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645