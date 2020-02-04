import sys
import timeit
import pprint

sys.stdin = open('가장_빠른_문자열_타이핑', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    target, tool = input().split()
    count = 0
    i = 0
    while i < len(target):
        if target[i] != tool[0]:
            count += 1
            i += 1
        else:
            if i + len(tool) <= len(target):
                if target[i:i+len(tool)] == tool:
                    count += 1
                    i += len(tool)
                else:
                    count += 1
                    i += 1
            else:
                count += len(target) - i
                i += len(tool)
    print("#{} {}".format(testCase + 1, count))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 5