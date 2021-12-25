#!/usr/bin/env python3

from typing import NamedTuple

import helper

Matrix = list[list[str]]


class Point(NamedTuple):
    row: int
    col: int
    # value: str    # char, actually
# endclass


class Seafloor:
    def __init__(self, fname: str) -> None:
        self.matrix: Matrix = self.build_matrix(fname)
        self.step_cnt = 0
        self.last_row_idx = len(self.matrix) - 1
        self.last_column_idx = len(self.matrix[0]) - 1
        self.changed = True

    def build_matrix(self, fname: str) -> Matrix:
        m: Matrix = []
        for line in helper.read_lines(fname):
            m.append([c for c in line])
        #
        return m

    def can_go_right(self, i: int, j: int) -> bool:
        row = i
        col = j + 1
        if col > self.last_column_idx:
            col = 0
        #
        return self.matrix[row][col] == '.'

    def can_go_down(self, i: int, j: int) -> bool:
        row = i + 1
        col = j
        if row > self.last_row_idx:
            row = 0
        #
        return self.matrix[row][col] == '.'

    def step_right(self) -> None:
        matrix = self.matrix
        points: list[Point] = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '>':
                    if self.can_go_right(i, j):
                        points.append(Point(i, j))
                    #
                #
            #
        #
        m = matrix
        for p in points:
            i, j = p
            row = i
            col = j + 1
            if col > self.last_column_idx:
                col = 0
            #
            m[i][j], m[row][col] = m[row][col], m[i][j]
            self.changed = True
        #
    #

    def step_down(self) -> None:
        matrix = self.matrix
        points: list[Point] = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'v':
                    if self.can_go_down(i, j):
                        points.append(Point(i, j))
                    #
                #
            #
        #
        m = matrix
        for p in points:
            i, j = p
            row = i + 1
            col = j
            if row > self.last_row_idx:
                row = 0
            #
            m[i][j], m[row][col] = m[row][col], m[i][j]
            self.changed = True
        #

    def step(self) -> None:
        if self.changed:
            self.step_cnt += 1
        #
        self.changed = False
        self.step_right()
        self.step_down()

    def debug(self) -> None:
        print(f"After {self.step_cnt} step(s):")
        print(self)
        print("---")

    def __str__(self) -> str:
        sb = []
        for row in self.matrix:
            sb.append("".join(row))
        #
        return "\n".join(sb)

# endclass Seafloor


def main():
    # fname = "example_small.txt"
    # fname = "example_bigger.txt"
    fname = "input.txt"

    floor = Seafloor(fname)
    # floor.debug()

    while floor.changed:
        floor.step()
        # floor.debug()
    #
    print(floor.step_cnt)

##############################################################################

if __name__ == "__main__":
    main()
