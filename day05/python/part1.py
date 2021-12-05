#!/usr/bin/env python3

from collections import Counter
from typing import NamedTuple

import helper


class Point(NamedTuple):
    x: int
    y: int


def to_point(s: str) -> Point:
    parts = s.split(",")
    x = int(parts[0])
    y = int(parts[1])
    return Point(x=x, y=y)


def get_line_points(p_one: Point, p_two: Point) -> list[Point]:
    p1, p2 = sorted([p_one, p_two])
    result: list[Point] = []

    if p1.x == p2.x:
        for y in range(p1.y, p2.y + 1):
            result.append(Point(p1.x, y))
        #
    elif p1.y == p2.y:
        for x in range(p1.x, p2.x + 1):
            result.append(Point(x, p1.y))

    return result


def main():
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    filtered: list[tuple[Point, Point]] = []
    for line in lines:
        left, right = line.split(" -> ")
        p1 = to_point(left)
        p2 = to_point(right)
        if p1.x == p2.x or p1.y == p2.y:
            filtered.append((p1, p2))
        #
    #
    all_points: list[Point] = []
    for p1, p2 in filtered:
        # print(p1, "->", p2)
        line_points: list[Point] = get_line_points(p1, p2)
        # print(line)
        all_points.extend(line_points)
    #
    # print("---")
    # print(points)
    cnt = Counter(all_points)
    result = sum([1 for v in cnt.values() if v > 1])
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
