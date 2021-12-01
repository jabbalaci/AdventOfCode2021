#!/usr/bin/env python3

import helper

NOT_AVAILABLE = 0
NO_CHANGE = 0
INC = 1
DEC = -1

def main():
    # data = helper.read_lines_as_ints("example.txt")
    data = helper.read_lines_as_ints("input.txt")

    windows = zip(data, data[1:], data[2:])
    numbers = [sum(t) for t in windows]

    # print(numbers)

    sonar = [NOT_AVAILABLE]
    for i in range(1, len(numbers)):
        prev = numbers[i-1]
        curr = numbers[i]
        diff = curr - prev
        if diff > 0:
            sonar.append(INC)
        elif diff == 0:
            sonar.append(NO_CHANGE)
        else:
            sonar.append(DEC)
        #
    #
    result = sum([1 for value in sonar if value == INC])
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
