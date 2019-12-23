import sys
import timeit
import pprint

sys.stdin = open('덕환이의_카드_뽑기', 'r')

start_time = timeit.default_timer()

for testCase in range(int(input())):
    N_cards, N_steps = map(int, input().split())
    deck = [card + 1 for card in range(N_cards)]
    index = 0
    while len(deck) != 1:
        index = (index + N_steps) % len(deck)
        del deck[index]
    print("#{} {}".format(testCase + 1, deck[0]))

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

# 1 6
# 2 5
# 3 72252
