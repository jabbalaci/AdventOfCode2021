#!/usr/bin/env python3

import helper


def get_column(i: int, lines: list[str]) -> list[str]:
    return [line[i] for line in lines]


def main():
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    # for line in lines:
        # print(line)
    no_of_columns = len(lines[0])
    # print(no_of_columns)
    result = []
    for i in range(no_of_columns):
        column = get_column(i, lines)
        zeros = column.count('0')
        ones = column.count('1')
        result.append('0' if zeros > ones else '1')
        # print("".join(column))
    #
    gamma_str = "".join(result)
    epsilon_str = gamma_str.replace('0', 'x').replace('1', '0').replace('x', '1')
    # print(gamma_str)
    # print(epsilon_str)
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    print(gamma * epsilon)

##############################################################################

if __name__ == "__main__":
    main()
