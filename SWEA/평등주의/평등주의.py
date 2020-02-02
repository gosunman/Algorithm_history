import sys
import timeit
import pprint

sys.stdin = open('평등주의', 'r')

start_time = timeit.default_timer()


def push():
    global status, length_sample, indexes
    length_sample += 1
    idx = length_sample
    while idx//2 > 0:
        p_i, p_p, p_l, p_r = status[idx//2]
        c_i, c_p, c_l, c_r = status[idx]
        if c_p > p_p or (c_p == p_p and c_p != 0 and c_l * c_r > p_l * p_r):
            indexes[p_i] = idx
            indexes[c_i] = idx // 2
            status[idx], status[idx//2] = status[idx//2], status[idx]
            idx //= 2
        else:
            idx = 1
    pass


def pop():
    global status, length_sample, indexes
    status[1], status[length_sample] = status[length_sample], status[1]
    indexes[status[1][1]] = length_sample
    indexes[status[length_sample][1]] = 1
    length_sample -= 1
    idx = 1
    while idx * 2 + 1 <= length_sample or idx * 2 <= length_sample:
        if idx * 2 + 1 > length_sample:
            p_i, p_p, p_l, p_r = status[idx]
            l_i, l_p, l_l, l_r = status[idx * 2]
            if l_p > p_p or (l_p == p_p and l_p != 0 and l_l * l_r > p_l * p_r):
                indexes[p_i] = idx * 2
                indexes[l_i] = idx
                status[idx], status[idx*2] = status[idx*2], status[idx]
                idx *= 2
            else:
                idx = length_sample + 1
        else:
            p_i, p_p, p_l, p_r = status[idx]
            l_i, l_p, l_l, l_r = status[idx * 2]
            r_i, r_p, r_l, r_r = status[index * 2 + 1]
            if l_p > p_p or (l_p == p_p and l_p != 0 and l_l * l_r > p_l * p_r ):
                indexes[p_i] = idx * 2
                indexes[l_i] = idx
                status[idx], status[idx*2] = status[idx*2], status[idx]
                idx *= 2
            elif r_p > p_p or (r_p == p_p and r_p != 0 and r_l * r_r > p_l * p_r):
                indexes[p_i] = idx * 2 + 1
                indexes[r_i] = idx
                status[idx], status[idx * 2 + 1] = status[idx * 2 + 1], status[idx]
                idx = idx * 2 + 1
            else:
                idx = length_sample + 1


for testCase in range(int(input())):
    length_sample, chance = map(int, input().split())
    sample = list(map(int, input().split()))
    status = [[0, float('inf'), 0, 0]]
    indexes = {}
    for index in range(length_sample):
        if index == 0:
            right = sample[index] - sample[index + 1]
            status.append([index, abs(right), right, right])
        elif index == length_sample - 1:
            left = sample[index] - sample[index - 1]
            status.append([index, abs(left), left, left])
        else:
            left = sample[index] - sample[index - 1]
            right = sample[index] - sample[index + 1]
            status.append([index, max(abs(left), abs(right)), left, right])
    status.sort(key=lambda x: (x[1], x[2] * x[3]), reverse=True)
    for index in range(1, length_sample):
        indexes[status[index][0]] = index
    for _ in range(chance):
        pop()
        k_i, k_p, k_l, k_r = status[length_sample + 1]
        if k_i == 0:
            pass
        elif k_i == length_sample + 1:
            pass
        else:
            if k_l * k_r > 0:
                pass
        push()
    print("#{} {}".format(testCase + 1, status[0][1]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1
# 2 4
# 3 0

# 1 1
# 2 2
