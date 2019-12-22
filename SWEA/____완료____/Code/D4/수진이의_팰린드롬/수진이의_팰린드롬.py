import sys
import timeit
import pprint

sys.stdin = open('수진이의_팰린드롬', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    I_word = input().strip()
    characters = {}
    for word in I_word:
        if characters.get(word):
            characters[word] += 1
        else:
            characters[word] = 1
    answer = 0
    for value in characters.values():
        answer += value*(value + 1)//2
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 3
#2 6
#3 9