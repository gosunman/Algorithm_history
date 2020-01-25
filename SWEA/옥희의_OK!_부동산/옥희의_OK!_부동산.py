import sys
import timeit
import pprint

sys.stdin = open('옥희의_OK!_부동산', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_land, N_money = map(int, input().split())
    S_land = [0] + list(map(int, input().split()))
    index = list(range(N_land))
    temp = index[:]
    size = 0
    # 전체 스캔하면서 카운트
    # 사이즈가 커지면 맨 오른쪽에 있는 놈을 더해서 원래 값 업데이트
    # 만약 숫자가 초과하면 인덱스에서 제거
    # 그래서 매번 전체 후보를 다 조사하는 방식이지만, 인덱스 후보가 줄어들면서 시간 단축
    # 합산하는 과정도 중간 과정을 기억하기 때문에 계산량이 획기적으로 줄어듬
    # 문제는.. c++로 풀어야 한다는 점
    while index:
        for i in index:
            if S_land[i] + S_land[i+size] <
    print("#{} {}".format(testCase + 1, 0))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 4