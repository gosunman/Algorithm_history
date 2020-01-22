import sys
import timeit
import pprint

sys.stdin = open('차량_정비소', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_receptions, N_mechanics, N_customer, first_N, second_N = map(int, input().split())
    first_N -= 1
    second_N -= 1
    S_receptions = list(map(int, input().split()))
    S_mechanics = list(map(int, input().split()))
    S_customers = list(map(int, input().split()))
    N_complete = 0
    N_occupied_receptions = 0
    N_occupied_mechanics = 0
    reception_available = [[-1, 0] for i in range(N_receptions)] # 종료시간 + 회원번호
    mechanic_available = [-1 for i in range(N_mechanics)]
    waiting = [] # 회원번호 + 접수창고 번호
    time = 0
    answer = 0
    temp_index = 0

    while N_complete != N_customer:

        # 정비창구에서 빼기
        for idx in range(N_mechanics):
            if mechanic_available[idx] == time:
                mechanic_available[idx] = -1
                N_occupied_mechanics -= 1
                N_complete += 1

        # 접수창구에서 빼기
        for idx in range(N_receptions):
            if reception_available[idx][0] == time:
                # 회원 번호 + 접수 창구 번호
                waiting.append([reception_available[idx][1], idx])
                reception_available[idx] = [-1, 0]
                N_occupied_receptions -= 1

        # 정비창구에 넣기
        for idx in range(N_mechanics):
            if mechanic_available[idx] == -1:
                if waiting:
                    index, number = waiting.pop(0)
                    mechanic_available[idx] = time + S_mechanics[idx]
                    if number == first_N and idx == second_N:
                        answer += index
                else:
                    break

        # 접수창구에 넣기
        for idx in range(N_receptions):
            if reception_available[idx] == [-1, 0]:
                if temp_index < N_customer:
                    reception_available[idx] = [time + S_receptions[idx], temp_index + 1]
                else:
                    break
        time += 1

    if answer == 0:
        answer = -1
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 7
#3 2
#4 22
#5 18
#6 15
#7 -1
#8 259
#9 100
#10 164