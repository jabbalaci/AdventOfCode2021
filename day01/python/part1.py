#!/usr/bin/env python3

import helper

NOT_AVAILABLE = 0
INC = 1
DEC = -1

def main():
    # numbers = helper.read_lines_as_ints("example.txt")
    numbers = helper.read_lines_as_ints("input.txt")

    sonar = [NOT_AVAILABLE]
    for i in range(1, len(numbers)):
        prev = numbers[i-1]
        curr = numbers[i]
        if curr - prev > 0:
            sonar.append(INC)
        else:
            sonar.append(DEC)
        #
    #
    result = sum([1 for value in sonar if value == INC])
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
