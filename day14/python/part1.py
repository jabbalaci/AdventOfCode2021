#!/usr/bin/env python3

from collections import Counter
from pprint import pprint

import helper


class Polymer:
    # self.polymer_template: str
    # self.rules: dict[str, str]
    # self.d: dict[str, int]
    # self.last: str

    def __init__(self, fname: str) -> None:
        content = helper.read(fname)
        left, right = content.split("\n\n")
        #
        self.polymer_template: str = left
        self.rules: dict[str, str] = {}
        for rule in right.splitlines():
            key, value = rule.split(" -> ")
            self.rules[key] = value
        #
        self.d: dict[str, int] = {}
        self.last: str = ""
        #
        self.init_d()

    def init_d(self) -> None:
        for i in range(len(self.polymer_template) - 1):
            piece = self.polymer_template[i:i+2]
            self.d[piece] = 1
            if i == len(self.polymer_template) - 2:
                self.last = piece
        #

    def get_key_pairs_for(self, key) -> tuple[str, str]:
        value = self.rules[key]
        key1 = key[0] + value
        key2 = value + key[1]
        #
        return (key1, key2)

    def step(self) -> None:
        new: dict[str,int] = {}

        for key, value in self.d.items():
            new_key1, new_key2 = self.get_key_pairs_for(key)
            for k in (new_key1, new_key2):
                old_value = new.get(k, 0)
                new[k] = old_value + value
            #
            if key == self.last:
                self.last = new_key2
        #
        self.d = new

    def get_occurrences(self) -> dict[str, int]:
        result: dict[str, int] = {}

        for key, value in self.d.items():
            c = key[0]
            old_value = result.get(c, 0)
            result[c] = old_value + value
        #
        last_c = self.last[-1]
        old_value = result.get(last_c, 0)
        result[last_c] = old_value + 1

        return result

    def debug(self) -> None:
        pprint(self.d)
        print("last:", self.last)
        d = self.get_occurrences()
        print()
        print("occurrences: ", end="")
        pprint(d)
        print("---")


def main():
    # fname = "example.txt"
    fname = "input.txt"

    poly = Polymer(fname)

    for i in range(10):
        poly.step()
        # poly.debug()
    #
    d = poly.get_occurrences()
    values = sorted(d.values(), reverse=True)
    result = values[0] - values[-1]
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
