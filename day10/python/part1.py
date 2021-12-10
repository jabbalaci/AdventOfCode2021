#!/usr/bin/env python3

from typing import List

import helper


class Checker:
    OPENER = '([{<'
    GOOD_PAIRS = ( ('(', ')'), ('[', ']'), ('{', '}'), ('<', '>') )
    SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def __init__(self, line: str) -> None:
        self.line = line
        self.error = ""    # will be set later if a wrong char. is found
        self.stack: List[str] = []    # list of chars, actually

    def get_error_score(self) -> int:
        return Checker.SCORES.get(self.error, 0)

    def matches(self, c1: str, c2: str) -> bool:
        """
        c1 and c2 are actually characters
        """
        t = (c1, c2)
        return t in Checker.GOOD_PAIRS

    def check(self) -> bool:
        for c in self.line:
            if c in Checker.OPENER:
                self.stack.append(c)
            else:    # closing char.
                if len(self.stack) == 0:
                    self.error = c
                    return False
                # else, not empty
                if self.matches(self.stack[-1], c):
                    self.stack.pop()
                else:
                    self.error = c
                    return False
        #
        return len(self.stack) == 0

# endclass


def main():
    # line = "<{([([[(<>()){}]>(<<{{"
    # t = Tester(line)
    # ok = t.check()
    # print(f"ok: {ok}, error: {t.error}")

    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    total = 0
    for line in lines:
        # print(line)
        t = Checker(line)
        _ = t.check()
        total += t.get_error_score()
        # ok = t.check()
        # print(f"ok: {ok}, error: {t.error}, score: {t.get_error_score()}")
        # print("---")
    #
    print(total)

##############################################################################

if __name__ == "__main__":
    main()
