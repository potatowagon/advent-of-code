import math
import os

import pytest


def soln(input: [str]) -> int:
    hor = 0
    depth = 0
    for v in input:
        _dir,val = v.split(' ')
        val = int(val)
        if _dir == "forward":
            hor += val
        elif _dir == "down":
            depth += val
        elif _dir == "up":
            depth -= val
    return hor * depth

def soln2(input: [str]) -> int:
    hor = 0
    depth = 0
    aim = 0
    for v in input:
        _dir,val = v.split(' ')
        val = int(val)
        if _dir == "forward":
            hor += val
            depth += (aim * val)
        elif _dir == "down":
            aim += val
        elif _dir == "up":
            aim -= val
    return hor * depth


def test_sample():
    sample_input = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]
    assert soln(sample_input) == 150
    assert soln2(sample_input) == 900



def test_real():
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "2021_2.txt")
    with open(input_file) as f:
        my_input = f.readlines()
    assert soln(my_input) == 2120749
    assert soln2(my_input) == 2138382217
