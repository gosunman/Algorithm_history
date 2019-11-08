import sys
import timeit
import pprint

sys.stdin = open('특이한_자석', 'r')

start_time = timeit.default_timer()


def solution(index, clockwise):
    global indexes, spirals, checked
    # 검사하였음을 체크하는 문장
    checked[index] = 0

    # 현재 검사하는 자석이 맨 오른쪽 자석이 아니며 이전에 검사한 적이 없다면
    if index < 3 and checked[index + 1]:
        # 현재 자석의 오른쪽을 향하는 톱날과 그 오른쪽 자석의 왼쪽을 향하는 톱날이 다를 때,
        if spirals[index][(indexes[index] + 2) % 8] != spirals[index + 1][(indexes[index + 1] - 2) % 8]:
            # 오른쪽 자석에서 같은 시뮬레이션 계산을 수행
            solution(index + 1, clockwise * -1)

    # 위와 마찬가지 작업이지만 왼쪽 자석을 향해 진행
    if index > 0 and checked[index - 1]:
        if spirals[index][(indexes[index] - 2) % 8] != spirals[index - 1][(indexes[index - 1] + 2) % 8]:
            solution(index - 1, clockwise * -1)

    # 회전 이후 변경된 맨 위를 향하는 톱날의 인덱스로 갱신
    indexes[index] = (indexes[index] + (-1 if clockwise == 1 else 1)) % 8


for testCase in range(int(input())):
    # 회전 시킬 명령문의 개수
    qnt_commands = int(input())
    # indexes는 맨 위를 가르킬 인덱스의 집합
    # 왜냐하면 자석을 직접 회전시키지 않고, 맨 위를 향하는 톱날을 가르키는 인덱스를 변경시켜 회전하는 효과를 줄 예정이기 때문
    indexes = [0, 0, 0, 0]
    # 자석 정보를 모두 포함하는 리스트
    spirals = []
    for _ in range(4):
        spirals.append(list(map(int, input().split())))

    # 시뮬레이션 시작
    for command in range(qnt_commands):
        # 시뮬레이션에 양 자석으로 탐색을 이어나가는 재귀함수를 이용할 예정이기 때문에, 중복 검사를 막기 위한 리스트
        checked = [1, 1, 1, 1]
        temp, clockwise = map(int, input().split())
        # 문제의 자석 번호는 1~4까지이지만 나는 0~3번을 사용하기 때문에 미리 1을 빼준다
        index = temp - 1
        solution(index, clockwise)

    # 정답을 계산하는 구문
    ans = 0
    for index in range(4):
        ans += spirals[index][indexes[index]] * (2 ** index)

    print("#{} {}".format(testCase + 1, ans))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 10
# 2 14
# 3 3
# 4 13
# 5 15
# 6 10
# 7 2
# 8 6
# 9 5
# 10 4
