#!/usr/bin/env python3

import helper

class ShouldNeverGetHere(Exception):
    pass

def main():
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    horizontal, depth, aim = (0, 0, 0)

    for line in lines:
        parts = line.split()
        instruction = parts[0]
        value = int(parts[1])
        if instruction == "forward":
            horizontal += value
            depth += aim * value
        elif instruction == "down":
            aim += value
        elif instruction == "up":
            aim -= value
        else:
            raise ShouldNeverGetHere()
        #
    #
    print(f"{horizontal=}")
    print(f"{depth=}")
    print(f"{aim=}")
    print("---")
    print(horizontal * depth)

##############################################################################

if __name__ == "__main__":
    main()
