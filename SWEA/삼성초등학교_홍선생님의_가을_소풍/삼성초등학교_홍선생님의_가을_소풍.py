import sys
import timeit
import pprint

sys.stdin = open('삼성초등학교_홍선생님의_가을_소풍', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_students = int(input())
    S_friendship = list(map(int, input().split()))
    available = [1 for _ in range(N_students)]
    relation_give = {i: S_friendship[i] - 1 for i in range(N_students)}
    relation_receive = {relation_give[i]: i for i in relation_give.keys()}
    answer = 0
    for i in range(N_students):
        if available[i]:
            available[i] = 0
            ring = [i]
            while available[relation_give[ring[-1]]]:
                last = relation_give[ring[-1]]
                ring.append(last)
                available[last] = 0
            while available[relation_receive[ring[0]]]:
                prior = relation_receive[ring[0]]
                ring.insert(0, prior)
                available[prior] = 0
            answer += len(ring)
    print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 4
# 2 3
# 3 6
