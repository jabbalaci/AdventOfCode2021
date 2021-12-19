#!/usr/bin/env python3

import math

import helper


class SnailMath:
    def __init__(self, line: str) -> None:
        self.internal: list[str] = self.take_apart(line)

    def take_apart(self, line: str) -> list[str]:
        result: list[str] = []
        #
        i = 0
        while i < len(line):
            c = line[i]
            if not c.isdigit():
                result.append(c)
                i += 1
            else:
                j = i + 1
                while line[j].isdigit():
                    j += 1
                #
                result.append(line[i:j])
                i = j
            #
        #
        return result

    def reduce(self) -> None:
        while True:
            changed = self.explode()
            if changed:
                continue
            # else
            changed = self.split()
            if not changed:
                break
            #
        #

    def split(self) -> bool:
        """
        Split the formula.

        If the formula must split, then it'll modify `self.internal`.
        Returns True if the formula was modified, otherwise it returns False.
        """
        changed = False
        new: list[str] = self.internal.copy()

        # find the first (leftmost) big number (which is >= 10)
        first = -1
        number = -1
        for idx, value in enumerate(new):
            if value[0].isdigit():
                if int(value) >= 10:
                    first = idx
                    number = int(value)
                    break
            #
        #
        if first > -1:
            half = number / 2
            a = math.floor(half)
            b = math.ceil(half)
            new[first:first+1] = ['[', str(a), ',', str(b), ']']

        if new != self.internal:
            changed = True
            self.internal = new
        #
        return changed

    def explode(self) -> bool:
        """
        Explode the formula.

        If the formula must explode, then it'll modify `self.internal`.
        Returns True if the formula was modified, otherwise it returns False.
        """
        changed = False
        new: list[str] = self.internal.copy()

        (start, end) = (-1, -1)
        cnt = 0
        for idx, c in enumerate(new):
            if c == '[':
                cnt += 1
            #
            if c == ']':
                cnt -= 1
            #
            if c == '[' and cnt > 4:
                start = idx
                end = start + 1
                while new[end] != ']':
                    end += 1
                #
                break
            #
        #
        if start > -1:
            a = int(new[start+1])
            b = int(new[end-1])
            new[:start] = self.explode_left(new[:start], a)
            new[end+1:] = self.explode_right(new[end+1:], b)
            new[start:end+1] = ['0']

        if new != self.internal:
            changed = True
            self.internal = new
        #
        return changed

    def explode_left(self, li: list[str], add: int) -> list[str]:
        part = li.copy()

        # find the last number (rightmost)
        last = -1
        for idx, value in enumerate(part):
            if value[0].isdigit():
                last = idx
            #
        #
        if last > -1:
            old = int(part[last])
            new = old + add
            part[last] = str(new)
        #
        return part

    def explode_right(self, li: list[str], add: int) -> list[str]:
        part = li.copy()

        # find the first number (leftmost)
        first = -1
        for idx, value in enumerate(part):
            if value[0].isdigit():
                first = idx
                break
            #
        #
        if first > -1:
            old = int(part[first])
            new = old + add
            part[first] = str(new)
        #
        return part

    def to_str(self) -> str:
        return "".join(self.internal)

    def __str__(self) -> str:
        return self.to_str()

    def debug(self) -> None:
        print(self.to_str())
        print(str(self.internal)[1:-1])

    def __add__(self, other: 'SnailMath') -> 'SnailMath':
        s1 = self.to_str()
        s2 = other.to_str()
        combined = f"[{s1},{s2}]"
        sm = SnailMath(combined)
        sm.reduce()
        return sm

    def get_left_right(self) -> tuple[str, str]:
        inside = self.internal[1:-1]  # cut off '[' and ']' on both sides
        left = []
        cnt = 0
        i = 0
        while True:
            token = inside[i]
            left.append(token)
            i += 1

            if token == '[':
                cnt += 1
            #
            if cnt == 0 and token[0].isdigit():
                break
            #
            if token == ']':
                cnt -= 1
                if cnt == 0:
                    break
                #
            #
        #
        assert inside[i] == ','
        i += 1
        #
        right = inside[i:]
        #
        return ("".join(left), "".join(right))

    def magnitude(self) -> int:
        # self.debug()

        left, right = self.get_left_right()
        # print(f"left: {left}, right: {right}")

        left_magnitude = -1
        if left[0].isdigit():
            left_magnitude = int(left)
        else:
            left_magnitude = SnailMath(left).magnitude()
        #
        right_magnitude = -1
        if right[0].isdigit():
            right_magnitude = int(right)
        else:
            right_magnitude = SnailMath(right).magnitude()
        #
        return 3 * left_magnitude + 2 * right_magnitude

# endclass SnailMath


class Adder:
    def __init__(self, fname: str) -> None:
        self.lines: list[str] = helper.read_lines(fname)

    def sum(self) -> SnailMath:
        sm = SnailMath(self.lines[0])    # init.

        for i in range(1, len(self.lines)):
            curr = SnailMath(self.lines[i])
            sm = sm + curr
        #
        return sm

# endclass Adder


def main():
    # fname = "example5.txt"
    fname = "input.txt"

    lines: list[str] = helper.read_lines(fname)
    maxi = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                sm1 = SnailMath(lines[i])
                sm2 = SnailMath(lines[j])
                magnitude: int = (sm1 + sm2).magnitude()
                if magnitude > maxi:
                    maxi = magnitude
                #
            #
        #
    #
    print(maxi)

##############################################################################

if __name__ == "__main__":
    main()
