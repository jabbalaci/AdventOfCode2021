#!/usr/bin/env python3

"""
terrible solution but at this point I didn't care

It needs a remake for Part 2.
"""

import helper


def take_apart(right: str) -> list[int]:
    result = []
    parts = right.split(",")
    for part in parts:
        _, r = part.split("=")
        a, b = r.split("..")
        result.append(int(a))
        result.append(int(b))
    #
    return result


def main():
    # fname = "example1.txt"
    # fname = "example2.txt"
    fname = "input.txt"
    lines = helper.read_lines(fname)

    bag: set[tuple[int, int, int]] = set()
    for line in lines:
        left, right = line.split()
        x1, x2, y1, y2, z1, z2 = take_apart(right)
        # print(line)
        # print(x1, x2, y1, y2, z1, z2)
        for x in range(x1, x2+1):
            if not (-50 <= x <= 50):
                continue
            #
            for y in range(y1, y2+1):
                if not (-50 <= y <= 50):
                    continue
                #
                for z in range(z1, z2+1):
                    if not (-50 <= z <= 50):
                        continue
                    #
                    t = (x, y, z)
                    if left == "on":
                        bag.add(t)
                    else:
                        try:
                            bag.remove(t)
                        except:
                            pass
                    #
                #
            #
        #
    #
    print(len(bag))

##############################################################################

if __name__ == "__main__":
    main()
