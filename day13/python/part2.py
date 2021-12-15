#!/usr/bin/env python3

from typing import NamedTuple

import helper

Matrix = list[list[int]]

Instruction = tuple[str, int]


class Point(NamedTuple):
    row: int
    col: int
    value: int


class Paper:
    def __init__(self, fname: str) -> None:
        lines = helper.read(fname)
        part1, part2 = lines.split("\n\n")
        a, b, c = self.build_matrix(part1.splitlines())
        self.matrix: Matrix = a
        self.width: int = b
        self.height: int = c
        self.instructions: list[Instruction] = self.get_instructions(part2.splitlines())

    def get_instructions(self, lines: list[str]) -> list[Instruction]:
        result: list[Instruction] = []

        for line in lines:
            parts = line.split()
            end = parts[-1]
            parts = end.split("=")
            result.append((parts[0], int(parts[1])))
        #
        return result

    def build_matrix(self, lines: list[str]) -> tuple[Matrix, int, int]:
        points = []
        for line in lines:
            parts = line.split(",")
            points.append((int(parts[0]), int(parts[1])))
        #
        width = max(points, key=lambda t: t[0])[0] + 1
        height = max(points, key=lambda t: t[1])[1] + 1

        m: Matrix = []
        for h in range(height):
            m.append([0] * width)
        #
        for j, i in points:
            m[i][j] = 1
        #
        return m, width, height

    def get_number_of_dots(self) -> int:
        width, height = self.width, self.height
        total = 0
        #
        for i in range(height):
            row = self.matrix[i][:width]
            total += sum(row)
        #
        return total

    def fold_up(self, value: int) -> None:
        width, height = self.width, self.height
        #
        for x in range(width):
            cnt = 1
            for y in range(value+1, height):
                i, j = y, x
                if self.matrix[i][j] == 1:
                    self.matrix[value-cnt][j] = 1
                #
                cnt += 1
            #
        #
        self.height //= 2

    def fold_left(self, value: int) -> None:
        width, height = self.width, self.height
        #
        for y in range(height):
            cnt = 1
            for x in range(value+1, width):
                i, j = y, x
                if self.matrix[i][j] == 1:
                    self.matrix[i][value-cnt] = 1
                #
                cnt += 1
            #
        #
        self.width //= 2

    def fold(self, instruction: Instruction) -> None:
        direction, value = instruction
        if direction == 'y':
            self.fold_up(value)
        else:    # direction == 'x'
            self.fold_left(value)

    def start_folding(self) -> None:
        for instr in self.instructions:
            self.fold(instr)
            # self.show()
            # print("---")
        #

    def show(self) -> None:
        width, height = self.width, self.height
        #
        for i in range(height):
            row = self.matrix[i][:width]
            line = "".join([str(value) for value in row])
            line = line.replace("0", ".").replace("1", "#")
            print(line)
        #
        # print("No. of dots: {0}".format(self.get_number_of_dots()))

# endclass


def main():
    # fname = "example.txt"
    fname = "input.txt"

    page = Paper(fname)

    # page.show()
    # print("---")

    page.start_folding()

    page.show()    # RGZLBHFP

##############################################################################

if __name__ == "__main__":
    main()
