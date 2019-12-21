import sys
import timeit
import pprint

sys.stdin = open('빠른_휴대전화_키패드', 'r')

start_time = timeit.default_timer()

dictionary = {
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

for testCase in range(int(input())):
    S_input, N_words = map(int, input().split())
    S_input = str(S_input)
    len_word = len(S_input)
    S_words = input().split()
    answer = 0
    for word in S_words:
        available = True
        if len(word) == len_word:
            index = -1
            while index >= -len_word:
                if word[index] not in dictionary[S_input[index]]:
                    available = False
                    break
                else:
                    index -= 1
            if available:
                answer += 1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 2
# 3 2
