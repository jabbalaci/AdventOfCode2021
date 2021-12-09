#!/usr/bin/env python3

import helper


def main():
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    total = 0
    ok_lengths = (2, 3, 4, 7)
    for line in lines:
        _, right = line.split("|")
        words = right.split()
        for w in words:
            if len(w) in ok_lengths:
                total += 1
            #
        #
    #
    print(total)

##############################################################################

if __name__ == "__main__":
    main()
