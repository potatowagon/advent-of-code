import math

import pytest
import utils


def soln1(input: [int]) -> int:
    inc_count = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            inc_count += 1
    return inc_count


def soln2(input: [int]) -> int:
    inc_count = 0
    window_sum = 0
    prev_sum = math.inf
    for i, v in enumerate(input):
        window_sum += v
        # trim window end
        if i >= 3:
            window_sum -= input[i - 3]
        # complete window
        if i >= 2:
            if window_sum > prev_sum:
                inc_count += 1
            prev_sum = window_sum
    return inc_count


def test_sample():
    sample_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert soln1(sample_input) == 7
    assert soln2(sample_input) == 5


def test_real():
    my_input = utils.read_int_input("2021_1.txt")
    assert soln1(my_input) == 1228
    assert soln2(my_input) == 1257
