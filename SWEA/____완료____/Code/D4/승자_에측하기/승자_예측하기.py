import sys
import timeit
import pprint

sys.stdin = open('승자_예측하기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    limit = int(input())
    index = 1
    turn = True
    while limit > 0:
        limit -= index
        if turn:
            index *= 4
        turn = not turn
    if turn:
        win = "Alice"
    else:
        win = "Bob"
    print("#{} {}".format(testCase+1, win))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))


#1 Bob
#2 Alice
#3 Bob
#4 Alice
#5 Bob