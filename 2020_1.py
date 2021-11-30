import pytest
import os


def soln(input: [int]) -> int:
    seen = set()
    for v in input:
        pair = 2020 - v
        if pair in seen:
            return pair * v
        else:
            seen.add(v)


def test_sample():
    sample_input = [1721, 979, 366, 299, 675, 1456]
    assert soln(sample_input) == 514579


def test_real():
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, '2020_1_input.txt')
    with open(input_file) as f:
        my_input = f.readlines()
    my_input = list(map(lambda x: int(x), my_input))
    assert soln(my_input) == 969024
