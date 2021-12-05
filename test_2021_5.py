import pytest
import utils
import copy


def soln(input: [int]) -> int:
    return 1


def _parse(input):
    return [
        [[int(coor) for coor in v.split(",")] for v in s.split(" -> ")] for s in input
    ]


def soln(input: [[[int]]]) -> int:
    max_r = 0
    max_c = 0
    for line in input:
        start, end = line
        max_r = max([max_r, start[0], end[0]])
        max_c = max([max_c, start[1], end[1]])

    grid = [[0] * (max_c+1) for r in range(max_r+1)]
    for start, end in input:
        if start[0] == end[0]:
            r = start[0]
            s,e = (start[1], end[1]) if start[1] <= end[1] else (end[1], start[1])
            for c in range(s, e + 1):
                grid[r][c] += 1

        elif start[1] == end[1]:
            s,e = (start[0], end[0]) if start[0] <= end[0] else (end[0], start[0])
            c = start[1]
            for r in range(s, e + 1):
                grid[r][c] += 1
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] >= 2:
                count += 1
    return count


def soln2(input: [[[int]]]) -> int:
    max_r = 0
    max_c = 0
    for line in input:
        start, end = line
        max_r = max([max_r, start[0], end[0]])
        max_c = max([max_c, start[1], end[1]])

    grid = [[0] * (max_c+1) for r in range(max_r+1)]
    for start, end in input:
        if start[0] == end[0]:
            r = start[0]
            s,e = (start[1], end[1]) if start[1] <= end[1] else (end[1], start[1])
            for c in range(s, e + 1):
                grid[r][c] += 1

        elif start[1] == end[1]:
            s,e = (start[0], end[0]) if start[0] <= end[0] else (end[0], start[0])
            c = start[1]
            for r in range(s, e + 1):
                grid[r][c] += 1
        # diag
        elif abs(start[0]-end[0]) == abs(start[1]-end[1]):
            # bottom left to top right
            if (start[0]+start[1]) == (end[0]+end[1]):
                move = (-1,1)
            else:
                move = (1,1)
            leftmost,end = (start,end) if start[1] <= end[1] else (end,start)
            while leftmost[1] <= end[1]:
                r,c = leftmost
                dr, dc = move
                grid[r][c] += 1
                leftmost = (r + dr, c + dc)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] >= 2:
                count += 1
    return count


def test_sample():
    sample_input = utils.read_str_input("2021_5_s.txt")
    sample_input = _parse(sample_input)
    assert soln(sample_input) == 5
    assert soln2(sample_input) == 12


def test_real():
    my_input = utils.read_str_input("2021_5.txt")
    my_input = _parse(my_input)
    assert soln(my_input) == 4728
    assert soln2(my_input) == 17717
