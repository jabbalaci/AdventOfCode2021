#!/usr/bin/env python3

from collections import Counter
from typing import NamedTuple

import helper


class Pair(NamedTuple):
    position: int
    cost: int


def my_print(d: dict[int, int]) -> None:
    li = []
    for key in sorted(d.keys()):
        li.append(f"{key}: {d[key]}")
    #
    print("Cnt(", end="")
    print('{' + ", ".join(li) + '}', end="")
    print(")")


def modified(n: int) -> int:
    """
    Take the sum of the first `n` natural numbers.

    If `n` (the distance) is 4, then
    return 1 + 2 + 3 + 4
    """
    return (n * (n+1)) // 2


def get_pair(pos: int, d: dict[int, int]) -> Pair:
    cost = 0
    for p in d.keys():
        distance = abs(pos - p)
        cost += modified(distance) * d[p]
    #
    return Pair(position=pos, cost=cost)


def main():
    # fname = "example.txt"
    fname = "input.txt"
    numbers = [int(s) for s in helper.read(fname).split(",")]
    d = dict(Counter(numbers))
    # print(sorted(numbers))
    # my_print(d)
    li = []
    mini = min(d.keys())
    maxi = max(d.keys())
    for pos in range(mini, maxi+1):
        pair = get_pair(pos, d)
        li.append(pair)
    #
    # print(li)
    winner = min(li, key=lambda p: p.cost)
    # print("---")
    print(winner)
    # print("---")
    # print(winner.cost)

##############################################################################

if __name__ == "__main__":
    main()
