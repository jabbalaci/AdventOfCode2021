#!/usr/bin/env python3

import helper

class ShouldNeverGetHere(Exception):
    pass

def main():
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    horizontal, depth = (0, 0)

    for line in lines:
        parts = line.split()
        instruction = parts[0]
        value = int(parts[1])
        if instruction == "forward":
            horizontal += value
        elif instruction == "down":
            depth += value
        elif instruction == "up":
            depth -= value
        else:
            raise ShouldNeverGetHere()
        #
    #
    print(f"{horizontal=}")
    print(f"{depth=}")
    print("---")
    print(horizontal * depth)

##############################################################################

if __name__ == "__main__":
    main()
