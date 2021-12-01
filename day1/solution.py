#!/usr/local/bin/python3


def get_input_array():
    input = []
    with open('input.txt', 'r') as f:
        for line in f:
            try:
                val = int(line)
                input.append(val)
            except ValueError:
                pass
    return input


def count_increases(input):
    increases_count = 0
    for index, value in enumerate(input):
        if index == 0:
            continue
        if value > input[index - 1]:
            increases_count += 1
    return increases_count


def solution1():
    return count_increases(get_input_array())


def solution2():
    input = get_input_array()
    sum_input = []
    for index in range(len(input) - 2):
        sum_input.append(input[index] + input[index + 1] + input[index + 2])
    return count_increases(sum_input)



print(solution1())
print(solution2())
