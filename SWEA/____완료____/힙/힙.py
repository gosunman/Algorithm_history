import sys
import timeit
import pprint

sys.stdin = open('힙', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    outputs = []
    qnt_commands = int(input())
    heap = [0] * qnt_commands + [0]
    cnt = 0
    for _ in range(qnt_commands):
        command = list(map(int, input().split()))
        if command[0] == 1:
            cnt += 1
            index = cnt
            heap[index] = command[1]
            while index != 1 and heap[index] > heap[index//2]:
                heap[index], heap[index//2] = heap[index//2], heap[index]
                index //= 2
        else:
            if heap[1]:
                outputs.append(str(heap[1]))
                heap[1] = heap[cnt]
                heap[cnt] = 0
                cnt -= 1
                index = 1
                while index * 2 + 1 <= cnt:
                    next = (index * 2) if heap[index * 2] >= heap[index * 2 + 1] else (index * 2 + 1)
                    if heap[index] < heap[next]:
                        heap[index], heap[next] = heap[next], heap[index]
                        index = next
                    else:
                        break
            else:
                outputs.append(str(-1))
    print("#{} {}".format(testCase + 1, " ".join(outputs)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1 -1
#2 5 3