import collections
import itertools

import pytest
import utils


class HashedBoard:
    def __init__(self, board):
        self.r_marked2count = {}
        self.c_marked2count = {}
        self.last_marked = None
        self.val2rc = collections.defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.val2rc[board[r][c]].append((r, c))

    def mark(self, val):
        coors = self.val2rc[val]
        for r, c in coors:
            self.r_marked2count[r] = self.r_marked2count.get(r, 0) + 1
            self.c_marked2count[c] = self.c_marked2count.get(c, 0) + 1
        del self.val2rc[val]
        self.last_marked = val

    def is_win(self):
        for k, v in self.r_marked2count.items():
            if v == 5:
                return True
        for k, v in self.c_marked2count.items():
            if v == 5:
                return True
        return False

    def get_unmarked_vals_sum(self):
        return sum([k for k in self.val2rc])


def soln(rolled, boards) -> int:
    hashed_boards = [HashedBoard(b) for b in boards]

    for v in rolled:
        for b in hashed_boards:
            b.mark(v)
            if b.is_win():
                return v * b.get_unmarked_vals_sum()
    return -1

def soln2(rolled, boards) -> int:
    hashed_boards = [HashedBoard(b) for b in boards]
    last_win = None

    for v in rolled:
        leftovers = []
        for b in hashed_boards:
            b.mark(v)
            if b.is_win():
                last_win = b
            else:
                leftovers.append(b)
        hashed_boards = leftovers

    return last_win.get_unmarked_vals_sum() * last_win.last_marked if last_win else -1


def _parse(input):
    input = [list(y) for x, y in itertools.groupby(input, lambda z: z == "") if not x]
    rolled = input[0][0].split(",")
    boards = input[1:]

    rolled = [int(v) for v in rolled]
    boards = [[[int(c) for c in r.split(" ") if c != ""] for r in b] for b in boards]
    return rolled, boards


def test_sample():
    sample_input = utils.read_str_input("2021_4_s.txt")
    rolled, boards = _parse(sample_input)
    assert soln(rolled, boards) == 4512
    assert soln2(rolled, boards) == 1924


def test_real():
    my_input = utils.read_str_input("2021_4.txt")
    rolled, boards = _parse(my_input)
    assert soln(rolled, boards) == 44088
    assert soln2(rolled, boards) == 23670
