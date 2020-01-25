import sys
import timeit
import pprint

sys.stdin = open('서준이의_퍼즐_풀기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_size = int(input())
    index = [] # 몇 개 짜리
    S_column = {} # 몇 개 짜리 : 몇 개
    answer = "Yes"
    for i in map(int, input().split()):
        if S_column.get(i):
            S_column[i] += 1
        else:
            S_column[i] = 1
            index.append(i)
    index.sort()
    S_row = sorted(list(map(int, input().split())), reverse=True)
    for i in S_row:
        count = 0
        target_index = 0
        while count < i:
            count += S_column[index[target_index]]
            target_index += 1
        temp_index = 0
        temp_count = 0
        while temp_index != target_index + 1:
            temp_count += S_column[index[temp_index]]
            if temp_count < count:
                temp_index += 1
                if index[temp_index] == 1:
                    pass
                else:
                    pass
            else:
                pass
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#추가 인풋 아웃풋 있음

#1 Yes
#2 No
#3 No
#4 No

#1 No
#2 No
#3 Yes
#4 No
#5 No
#6 No
#7 No
#8 No
#9 No
#10 No
#11 No
#12 No
#13 No
#14 No
#15 No
#16 Yes
#17 Yes
#18 Yes
#19 Yes
#20 Yes
#21 Yes
#22 Yes
#23 No
#24 Yes
#25 Yes
#26 Yes
#27 No
#28 Yes
#29 Yes
#30 Yes
#31 No
#32 Yes
#33 No
#34 No
#35 Yes
#36 Yes
#37 No
#38 No
#39 No
#40 No
#41 No