#!/usr/bin/env python3

from enum import Enum
from typing import List, Optional, Tuple, Union


# ==== Solutions ==== #


def parse_input(data: str):
    pass


def solve1(data: str) -> Optional[str]:
    input = parse_input(data)
    return None


def solve2(data: str) -> Optional[str]:
    input = parse_input(data)
    return None


# ==== Solutions with test data ==== #


test_data1 = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
test_answer1 = 'CMZ'

test_data2 = test_data1
test_answer2 = 'CMZ'

solves = [
    {'func': solve1, 'test_data': test_data1, 'test_answer': test_answer1},
    {'func': solve2, 'test_data': test_data2, 'test_answer': test_answer2},
]

# ==== Template for running solutions ==== #


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input = f.read()

        number = 1
        for solve in solves:
            func = solve['func']

            slv = func(solve['test_data'])
            answer = solve['test_answer']
            if slv == answer:
                print(f'Solution {number} - Test has passed')
            else:
                print(
                    f'Solution {number} - Test has failed. Should be {answer}, got {slv}')
                number += 1
                continue

            slv = func(input)
            if slv is not None:
                print(f'Solution {number} - The answer: {slv}')
            number += 1
