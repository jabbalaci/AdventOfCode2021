#!/usr/bin/env python3

import helper

OXYGEN = 1
CO2 = 2


def get_column(i: int, lines: list[str]) -> list[str]:
    return [line[i] for line in lines]


def get_value(data: tuple[str, ...], which=OXYGEN) -> int:
    lines = list(data)

    col_idx = 0
    while len(lines) != 1:
        column: list[str] = get_column(col_idx, lines)
        zeros = column.count('0')
        ones = column.count('1')
        to_keep = ''
        if which == OXYGEN:
            to_keep = '1'    # if ones >= zeros
            if zeros > ones:
                to_keep = '0'
            #
        else:    # CO2
            to_keep = '0'    # if zeros <= ones
            if ones < zeros:
                to_keep = '1'
            #
        #
        lines = [line for line in lines if line[col_idx] == to_keep]
        col_idx += 1
    #
    return int(lines[0], 2)


def main():
    # data = tuple(helper.read_lines("example.txt"))
    data = tuple(helper.read_lines("input.txt"))

    oxygen = get_value(data, which=OXYGEN)
    print(oxygen)
    co2 = get_value(data, which=CO2)
    print(co2)
    print("---")
    print(oxygen * co2)

##############################################################################

if __name__ == "__main__":
    main()
