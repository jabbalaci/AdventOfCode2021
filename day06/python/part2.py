#!/usr/bin/env python3

from collections import Counter

import helper


def my_print(d: dict[int, int], msg: str = "") -> None:
    sb = []
    for key in range(0, 8+1):
        sb.append(f"{key}: {d[key]}")
    #
    print(f"{msg}: ", end="")
    print('{' + ", ".join(sb) + '}')


def main():
    # fname = "example.txt"
    fname = "input.txt"

    numbers = [int(s) for s in helper.read(fname).split(",")]
    d = dict(Counter(numbers))
    for key in range(0, 8+1):
        if key not in d:
            d[key] = 0
        #
    #

    for k in range(256):
        my_print(d, msg=f"{k}")

        cnt = 0
        for key in range(0, 8+1):
            if key == 0:
                cnt = d[key]
            else:
                d[key-1] = d[key]
                d[key] = 0
            #
        #
        d[6] += cnt
        d[8] = cnt

        # if k == 6:
            # break
        #
    #
    print("---")
    result = sum(d.values())
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
