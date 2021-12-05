import pytest
import utils


def soln(input: [str]) -> int:
    bitlen = len(input[0])
    gamma = ["0"] * bitlen
    epsilon = ["1"] * bitlen
    n = len(input)
    for i in range(bitlen):
        ones, zeros = _count_bits(input, i)
        # most common bit is ones. what if count of ones == zeros?
        if ones > zeros:
            gamma[i] = "1"
            epsilon[i] = "0"

    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)

    return epsilon * gamma


# return count of (ones, zeros)
def _count_bits(input: [str], idx: int) -> (int, int):
    ones = 0
    n = len(input)
    for s in input:
        if s[idx] == "1":
            ones += 1
    zeros = n - ones
    return (ones, zeros)


def _keep_only(ls: [str], bit: str, idx: int):
    new = []
    for s in ls:
        if s[idx] == bit:
            new.append(s)
    return new


def soln2(input: [str]) -> int:
    bitlen = len(input[0])

    o2input = input[::]
    for i in range(bitlen):
        ones, zeros = _count_bits(o2input, i)
        keep_bit = "1" if ones >= zeros else "0"
        o2input = _keep_only(o2input, keep_bit, i)
        if len(o2input) == 1:
            break

    co2input = input[::]
    for i in range(bitlen):
        ones, zeros = _count_bits(co2input, i)
        keep_bit = "0" if zeros <= ones else "1"
        co2input = _keep_only(co2input, keep_bit, i)
        if len(co2input) == 1:
            break

    o2 = int("".join(o2input[0]), 2)
    co2 = int("".join(co2input[0]), 2)
    return o2 * co2


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
    assert soln2(sample_input) == 230


def test_real():
    my_input = utils.read_str_input("2021_3.txt")
    assert soln(my_input) == 1540244
    assert soln2(my_input) == 4203981
