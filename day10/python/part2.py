#!/usr/bin/env python3

from typing import List

import helper


class Completer:
    SCORES = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def __init__(self, stack: str):
        self.stack: str = stack
        self.completion_string: str = self.get_completion_string()

    def get_completion_string(self) -> str:
        d = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }
        return "".join(d[c] for c in self.stack[::-1])

    def get_completion_score(self) -> int:
        total = 0
        for c in self.completion_string:
            total *= 5
            total += Completer.SCORES[c]
        #
        return total

# endclass Completer


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
    scores: List[int] = []
    for line in lines:
        # print(line)
        t = Checker(line)
        _ = t.check()
        if t.error == "":
            # print(f"line: {t.line}, stack: {''.join(t.stack)}")
            comp = Completer("".join(t.stack))
            scores.append(comp.get_completion_score())
            # print("---")
    #
    no_of_elems = len(scores)
    result = sorted(scores)[no_of_elems // 2]
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
