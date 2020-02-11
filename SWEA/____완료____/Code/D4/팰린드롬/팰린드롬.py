import sys
import timeit
import pprint

sys.stdin = open('팰린드롬', 'r')

start_time = timeit.default_timer()


def solution(sentence):
    limit = len(sentence)
    if sentence == sentence[::-1]:
        return limit
    for size in range(limit-1, 1, -1):
        for start in range(limit - size + 1):
            if sentence[start: start + size] == sentence[start + size - 1: start - 1: -1]:
                return size
    return 1


for testCase in range(int(input())):
    fullSentence = input().strip()
    print("#{} {}".format(testCase + 1, solution(fullSentence)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))
