def enter_operator(sample, count_list, value, depth):
    global result_min, result_max, number_number
    if depth != number_number:
        for i in range(4):
            if not count_list[i]:
                continue
            else:
                count_list[i] -= 1
                if i == 0:
                    enter_operator(sample, count_list, value + sample[depth], depth + 1)
                elif i == 1:
                    enter_operator(sample, count_list, value - sample[depth], depth + 1)
                elif i == 2:
                    enter_operator(sample, count_list, value * sample[depth], depth + 1)
                else:
                    enter_operator(sample, count_list, int(value / sample[depth]), depth + 1)
                count_list[i] += 1
    else:
        if result_min > value:
            result_min = value
        if result_max < value:
            result_max = value


for t in range(int(input())):
    number_number = int(input()) - 1
    list_operator = list(map(int, input().split()))
    list_number = list(map(int, input().split()))
    result_min = +100000000
    result_max = -100000000
    first_number = list_number.pop(0)
    enter_operator(list_number, list_operator, first_number, 0)
    print("#{} {}".format(t + 1, result_max - result_min))