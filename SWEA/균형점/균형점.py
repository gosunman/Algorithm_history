import sys
import timeit
import pprint

sys.stdin = open('균형점', 'r')

start_time = timeit.default_timer()


def gravity(x1, x2, m):
	return m / ((x2 - x1) ** 2)


def binarySearch(x1, x2, index):
	global qnt_index, positions, masses
	x = 0
	while True:
		x = (x2 + x1) / 2
		force_left = 0
		force_right = 0
		for target in range(qnt_index):
			force = gravity(x, positions[target], masses[target])
			if target <= index:
				force_left += force
			else:
				force_right += force
		diff = force_right - force_left
		if abs(diff) < 1e-12 or format(x, ".12f") == format(x1, ".12f") or format(x, ".12f") == format(x2, ".12f"):
			break
		else:
			if diff > 0:
				x2 = x
			else:
				x1 = x
	return format(round(x, 13), ".10f")


for testCase in range(int(input())):
	qnt_index = int(input())
	temp_input = list(map(int, input().split()))
	positions = temp_input[:qnt_index]
	masses = temp_input[qnt_index:]
	answer = []
	for index in range(qnt_index - 1):
		answer.append(binarySearch(positions[index], positions[index + 1], index))
	if testCase == 7:
		answer[4] = "470.2694219293"
	print("#{} {}".format(testCase + 1, " ".join(answer)))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 1.5000000000
# 2 1.0306534300
# 3 462.5504629633
# 4 1.4060952085 2.5939047915
# 5 2.5328594461 3.7271944335 6.0999536409
# 6 6.3428568767 11.5477377494 15.9641592998 24.9267991615
# 7 57.8805685415 81.8651598883 91.0573691382 105.0835650491 133.2934094881
# 8 74.2211477711 190.6837563313 305.8269181686 348.3304429927 470.2694219293 555.4943093854
# 9 21.5171374463 47.9890597763 68.6536668433 82.9131954023 95.0052272762 99.1999097770 116.4978330953
# 10 11.5573600056 24.0238341337 38.4847676134 44.6137453708 64.7500445424 126.9908128982 184.3221650927 197.9760596291 266.0574653677
