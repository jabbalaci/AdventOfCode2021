#!/usr/bin/env python3

import math
from typing import List, NamedTuple, Set

import helper

Matrix = List[List[int]]


class Point(NamedTuple):
    row: int
    col: int
    value: int


def build_matrix(lines: List[str]) -> Matrix:
    m: Matrix = []
    for line in lines:
        m.append([int(c) for c in line])
    #
    return m


def get_four_neighbors(i: int, j: int, matrix: Matrix) -> List[Point]:
    result: List[Point] = []

    neighbors = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]

    for x, y in neighbors:
        try:
            if (x < 0) or (y < 0):
                raise IndexError
            #
            value = matrix[x][y]
            result.append(Point(row=x, col=y, value=value))
        except IndexError:
            pass
        #
    #
    return result


def is_low_point(i: int, j: int, matrix: Matrix) -> bool:
    four_neighbors: List[Point] = get_four_neighbors(i, j, matrix)
    four_values: List[int] = sorted([p.value for p in four_neighbors])
    # if matrix[i][j] < four_neighbors[0]:
        # p = Point(row=i, col=j, value=matrix[i][j])
        # print("{0} < {1}".format(p, four_neighbors))
    return matrix[i][j] < four_values[0]


def get_low_points(matrix: Matrix) -> List[Point]:
    li: List[Point] = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if is_low_point(i, j, matrix):
                li.append(Point(row=i, col=j, value=matrix[i][j]))
            #
        #
    #
    return li


def extend(p: Point, visited: Set[Point], matrix: Matrix) -> None:
    visited.add(p)
    #
    neighbors: List[Point] = get_four_neighbors(p.row, p.col, matrix)
    for nb in neighbors:
        if nb not in visited:
            if 9 > nb.value > p.value:
                extend(nb, visited, matrix)
            #
        #
    #


def extend_from_low_point(p: Point, matrix: Matrix) -> List[Point]:
    bag: Set[Point] = set()
    extend(p, bag, matrix)

    return list(bag)


def main():
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    matrix: Matrix = build_matrix(lines)
    # for row in matrix:
        # print(row)
    low_points: List[Point] = get_low_points(matrix)
    # for p in points:
        # print(p)
    basins: List[int] = []
    for p in low_points:
        basin: List[Point] = extend_from_low_point(p, matrix)
        basins.append(len(basin))
    #
    basins.sort(reverse=True)
    # print(basins)
    top3 = basins[:3]
    result = math.prod(top3)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
