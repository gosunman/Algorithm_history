import sys
import timeit
import pprint

sys.stdin = open('올림픽_종목_투표', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_options, N_judges = map(int, input().split())
    S_options = list(map(int, input().split()))
    S_judges = list(map(int, input().split()))
    memo = {}
    votes = [0 for _ in range(N_options)]
    for judge in range(N_judges):
        if memo.get(S_judges[judge]):
            votes[memo[S_judges[judge]]] += 1
        else:
            for option in range(N_options):
                if S_options[option] <= S_judges[judge]:
                    memo[S_judges[judge]] = option
                    votes[option] += 1
                    break
    print("#{} {}".format(testCase + 1, 1 + votes.index(max(votes))))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 2
#2 1