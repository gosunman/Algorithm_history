import sys
import timeit
import pprint

sys.stdin = open('성수의_비밀번호_공격', 'r')

start_time = timeit.default_timer()


def solution(store):
	global digit_pw, qnt_key
	case = 1
	for number in range(2, digit_pw+1):
		case *= number
	for number in store:
		if number == 1:
			break
		else:
			for num in range(2, number+1):
				case //= num
	for number in range(2, qnt_key+1):
		case *= number
	return case % 1000000007


def combination(depth, limit, store, rest):
	global answer
	if depth != limit:
		for number in range(rest - limit + depth + 1, 0, -1):
			if store and number > store[-1]:
				break
			else:
				if depth == limit-1 and number != rest - limit + depth + 1:
					break
				store.append(number)
				combination(depth + 1, limit, store, rest - number)
				store.pop()
	else:
		print(store)
		answer += solution(store)


for testCase in range(int(input())):
	qnt_key, digit_pw = map(int, input().split())
	answer = 0
	combination(0, qnt_key, [], digit_pw)
	print("#{} {}".format(testCase + 1, answer))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 1
#2 30
#3 322494480