import pytest
import utils


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
    my_input = utils.read_int_input("2020_1.txt")
    assert soln(my_input) == 969024
