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
    # line = "[[[[[9,8],1],2],3],4]"    # explode -> [[[[0,9],2],3],4]
    # line = "[7,[6,[5,[4,[3,2]]]]]"    # explode -> [7,[6,[5,[7,0]]]]
    # line = "[[6,[5,[4,[3,2]]]],1]"    # explode -> [[6,[5,[7,0]]],3]
    # line = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"    # explode once  -> [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
                                                      # explode again -> [[3,[2,[8,0]]],[9,[5,[7,0]]]]
    # line = "[[[[0,7],4],[15,[0,13]]],[1,1]]"    # split once  -> [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
                                                # split again -> [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    # line = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"    # at the end: [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    # sm = SnailMath(line)

    # sm.debug()
    # print("---")
    # sm.reduce()
    # sm.split()
    # sm.split()
    # sm.debug()

    # fname = "example4.txt"
    # fname = "input.txt"
    # adder = Adder(fname)
    # result: SnailMath = adder.sum()
    # print(result)

    # line = "[9,1]"          # magn: 3*9 + 2*1 = 29
    # line = "[1,9]"          # magn: 3*1 + 2*9 = 21
    # line = "[[9,1],[1,9]]"  # magn: 3*29 + 2*21 = 129

    # line = "[[1,2],[[3,4],5]]"                                      # magn: 143
    # line = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"                      # magn: 1384
    # line = "[[[[1,1],[2,2]],[3,3]],[4,4]]"                          # magn: 445
    # line = "[[[[3,0],[5,3]],[4,4]],[5,5]]"                          # magn: 791
    # line = "[[[[5,0],[7,4]],[5,5]],[6,6]]"                          # magn: 1137
    # line = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"  # magn: 3488

    # fname = "example5.txt"
    fname = "input.txt"
    adder = Adder(fname)
    summa: SnailMath = adder.sum()
    print(summa)
    print("---")
    result = summa.magnitude()
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
