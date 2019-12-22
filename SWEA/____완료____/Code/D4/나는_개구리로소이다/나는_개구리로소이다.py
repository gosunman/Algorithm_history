import sys
import timeit
import pprint

sys.stdin = open('나는_개구리로소이다', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    I_words = input().strip()
    check = [0 for _ in range(5)]
    answer = 0
    for word in I_words:
        if word == 'c':
            check[0] += 1
            if check[0] > answer:
                answer = check[0]
        elif word == 'r':
            if check[0] > check[1]:
                check[1] += 1
            else:
                answer = -1
                break
        elif word == 'o':
            if check[1] > check[2]:
                check[2] += 1
            else:
                answer = -1
                break
        elif word == 'a':
            if check[2] > check[3]:
                check[3] += 1
            else:
                answer = -1
                break
        else:
            if check[3] > check[4]:
                # check[4] += 1
                for i in range(4):
                    check[i] -= 1
            else:
                answer = -1
                break
    if answer != -1:
        if check[0] == check[1] == check[2] == check[3] == check[4]:
           pass
        else:
            answer = -1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 2
#2 4
#3 -1
#4 -1
#5 -1
#6 1
#7 10
#8 3