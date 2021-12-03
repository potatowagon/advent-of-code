import pytest
import utils


def soln(input: [str]) -> int:
    bitlen = len(input[0])
    gamma = ["0"] * bitlen
    epsilon = ["1"] * bitlen
    n = len(input)
    for i in range(bitlen):
        ones = 0
        for s in input:
            if s[i] == "1":
                ones += 1
        zeros = n - ones
        # most common bit is ones. what if count of ones == zeros?
        if ones > zeros:
            gamma[i] = "1"
            epsilon[i] = "0"

    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)

    return epsilon * gamma


def test_sample():
    sample_input = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    assert soln(sample_input) == 198


def test_real():
    my_input = utils.read_str_input("2021_3.txt")
    assert soln(my_input) == 1540244
