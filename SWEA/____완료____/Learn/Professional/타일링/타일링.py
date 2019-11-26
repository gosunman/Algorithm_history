import sys
import timeit
import pprint

sys.stdin = open('타일링', 'r')

start_time = timeit.default_timer()

memoization = [0, 1, 3]


def memo(index):
    memoization.append(memoization[index - 1] + 2 * memoization[index - 2])


for i in range(3, 251):
    memo(i)

for testCase in range(int(input())):
    width = int(input())
    print("#{} {}".format(testCase + 1, memoization[width]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 683
# 3 845100400152152934331135470251
# 4 1071292029505993517027974728227441735014801995855195223534251
# 5 2142584059011987034055949456454883470029603991710390447068501
