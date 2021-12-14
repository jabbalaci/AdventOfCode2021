#!/usr/bin/env python3

from collections import Counter
from pprint import pprint

import helper


class Polymer:
    # self.current: list[str]    # list of chars, actually
    # self.rules: dict[str, str]

    def __init__(self, fname: str) -> None:
        content = helper.read(fname)
        left, right = content.split("\n\n")
        #
        self.current: list[str] = list(left)
        d: dict[str, str] = {}
        for rule in right.splitlines():
            key, value = rule.split(" -> ")
            d[key] = value
        #
        self.rules: dict[str, str] = d

    def step(self) -> None:
        result: list[str] = []

        curr = self.current
        for i in range(len(curr) - 1):
            key = curr[i] + curr[i+1]
            value = self.rules[key]
            if len(result) > 0 and result[-1] == curr[i]:
                result.pop()
            #
            result.extend([curr[i], value, curr[i+1]])
        #

        self.current = result

    def debug(self) -> None:
        print(len(self.current))
        # print("---")
        # pprint(self.rules)


def main():
    # fname = "example.txt"
    fname = "input.txt"

    poly = Polymer(fname)
    for i in range(10):
        poly.step()
    #
    # poly.debug()
    cnt = Counter(poly.current)
    values = sorted(cnt.values(), reverse=True)
    result = values[0] - values[-1]
    pprint(result)

##############################################################################

if __name__ == "__main__":
    main()
