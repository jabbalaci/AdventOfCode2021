#!/usr/bin/env python3

from typing import NamedTuple

import helper

Matrix = list[list[int]]


class Point(NamedTuple):
    row: int
    col: int
    value: int


class Dumbos:
    def __init__(self, lines: list[str]) -> None:
        self.matrix: Matrix = self.build_matrix(lines)
        self.will_flash: list[Point] = []    # collect octopussies that will flash
        self.step_counter = 0

    def build_matrix(self, lines: list[str]) -> Matrix:
        m: Matrix = []
        for line in lines:
            m.append([int(c) for c in line])
        #
        return m

    def print_matrix(self) -> None:
        for row in self.matrix:
            print(row)

    def get_neighbors(self, p: Point) -> list[Point]:
        result: list[Point] = []

        i, j, _ = p

        neighbors = [(i-1, j), (i, j+1), (i+1, j), (i, j-1),
                     (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1) ]

        for x, y in neighbors:
            try:
                if (x < 0) or (y < 0):
                    raise IndexError
                #
                value = self.matrix[x][y]
                result.append(Point(row=x, col=y, value=value))
            except IndexError:
                pass
            #
        #
        return result

    def flash(self, p: Point) -> None:
        matrix = self.matrix
        neighbors: list[Point] = self.get_neighbors(p)
        #
        for nb in neighbors:
            i, j, _ = nb
            matrix[i][j] += 1
            # instead of >9, check if ==10. This way we add it to the list just once.
            if matrix[i][j] == 10:    # Can only flash once!
                self.will_flash.append(Point(row=i, col=j, value=matrix[i][j]))
            #
        #

    def all_zeros(self) -> bool:
        total = 0
        for row in self.matrix:
            total += sum(row)
        #
        return total == 0

    def step(self) -> None:
        self.step_counter += 1
        #
        matrix = self.matrix
        #
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += 1
                if matrix[i][j] > 9:
                    self.will_flash.append(Point(row=i, col=j, value=matrix[i][j]))
                #
            #
        #
        while len(self.will_flash) > 0:
            pussy: Point = self.will_flash.pop()
            self.flash(pussy)
        #
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 9:
                    matrix[i][j] = 0
                #
            #
        #

# endclass


def main():
    # lines = helper.read_lines("example0.txt")
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    dumbos = Dumbos(lines)
    # dumbos.print_matrix()
    while True:
        dumbos.step()
        if dumbos.all_zeros():
            break
        #
    #
    print(dumbos.step_counter)

##############################################################################

if __name__ == "__main__":
    main()
