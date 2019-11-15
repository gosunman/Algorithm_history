import sys
import timeit
import pprint

sys.stdin = open('이미지_유사도_검사', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
	length = int(input())
	sample_1 = input().strip()
	sample_2 = input().strip()
	table = [[0 for _ in range(length+1)] for __ in range(length+1)]
	for y in range(1, length + 1):
		for x in range(1, length + 1):
			if sample_1[x-1] == sample_2[y-1]:
				table[y][x] = table[y-1][x-1] + 1
			else:
				table[y][x] = max(table[y-1][x], table[y][x-1])
	answer = table[length][length]/length*100
	print(f"#{testCase + 1} {answer:.2f}")

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 60.00
#2 55.00
#3 56.67
#4 67.50
#5 64.00
#6 65.00
#7 64.00
#8 79.33
#9 65.50
#10 84.80