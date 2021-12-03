import pytest
import utils


def soln(input: [int]) -> int:
    return 1


def test_sample():
    sample_input = [1]
    assert soln(sample_input) == 1


def test_real():
    my_input = utils.read_int_input("REPLACEME.txt")
    assert soln(my_input) == 1
