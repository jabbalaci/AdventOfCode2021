#!/usr/bin/env python3

import helper


def main():
    # fname = "example.txt"
    fname = "input.txt"
    numbers = [int(s) for s in helper.read(fname).split(",")]
    # print(numbers)

    for k in range(80):
        print(f"{k+1}: {len(numbers)}", flush=True)
        cnt = 0
        for i in range(len(numbers)):
            value = numbers[i]
            value -= 1
            if value == -1:
                value = 6
                cnt += 1
            #
            numbers[i] = value
        #
        for i in range(cnt):
            numbers.append(8)
        #
        # print(numbers)

        # if k == 17:
            # break
        #
    #
    print("---")
    result = len(numbers)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
