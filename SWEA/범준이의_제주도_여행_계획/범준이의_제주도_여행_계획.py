import sys
import timeit
import pprint

sys.stdin = open('범준이의_제주도_여행_계획', 'r')

start_time = timeit.default_timer()


def solution(depth, limit, last_site, spent_time, history, temp_ans):
    global table_info, table_sites, ans, qnt_sites, qnt_days, ans_history
    if depth <= limit - 1:
        for site in range(qnt_sites):
            if site != last_site:
                if table_sites[site][0] == 'P':
                    if site not in history:
                        temp_time = spent_time + table_info[last_site][site] + int(table_sites[site][1])
                        if temp_time <= 9 * 60:
                            history.append(site)
                            solution(depth, limit, site, temp_time, history, temp_ans + int(table_sites[site][2]))
                            history.remove(site)
                elif table_sites[site][0] == 'H':
                    if spent_time + table_info[last_site][site] <= 9 * 60:
                        history.append(site)
                        solution(depth + 1, limit, site, 0, history, temp_ans)
                        history.remove(site)
                else:
                    if depth == limit - 1:
                        if spent_time + table_info[last_site][site] <= 9 * 60:
                            if temp_ans > ans:
                                history.append(site)
                                ans = temp_ans
                                ans_history = history[:]
                                history.remove(site)


for t in range(int(input())):
    qnt_sites, qnt_days = map(int, input().split())
    table_info = [[0 for __ in range(qnt_sites)] for _ in range(qnt_sites)]
    for start in range(qnt_sites - 1):
        info = list(map(int, input().split()))
        for end in range(len(info)):
            table_info[start][1 + start + end] = info[end]
            table_info[1 + start + end][start] = info[end]
    table_sites = [[] for _ in range(qnt_sites)]
    for _ in range(qnt_sites):
        table_sites[_] = input().split()
    ans = 0
    ans_history = []
    solution(0, qnt_days, 0, 0, [], 0)
    xx = list(map(lambda x: str(x + 1), ans_history))
    print("#{} {} {}".format(t + 1, ans, ' '.join(xx)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 25 2 3 9 5 6 10 4 1
#2 11 2 5 1
#3 0
#4 24 2 5 9 6 4 1
#5 14 3 6 4 5 1
#6 47 5 3 11 4 16 7 13 16 6 1
#7 33 2 6 15 4 12 5 16 10 8 7 1
#8 45 8 18 6 11 17 13 9 19 10 14 1
#9 46 10 12 18 15 16 18 3 7 17 9 13 1
#10 44 5 22 30 18 15 33 4 12 1