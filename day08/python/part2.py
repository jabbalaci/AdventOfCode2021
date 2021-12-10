#!/usr/bin/env python3

"""
tip from here: https://old.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/hnqza2g/

according to /u/PZon:

For the 6-segment numbers:

* 6 is the only one that does not contain 1
* 9 is the one containing both 1 and 4
* 0 is left

And for the 5-segment numbers:

* 3 is the only one that includes 1
* 5 is the one that doesn't include 1 but is included in 9
* 2 is left
"""

from pprint import pprint

import helper


class Decoder:
    NOT_SET = -1

    def __init__(self, line: str) -> None:
        self.line: str = line
        self.word2digit: dict[str, int] = {}        # will be set later
        self.digit2set: dict[int, set[str]] = {}    # will be set later, used as cache

    def set_trivial_numbers(self) -> None:
        d = self.word2digit
        #
        for key in d:
            length = len(key)
            if length == 2:
                d[key] = 1
                self.digit2set[1] = set(key)
            elif length == 4:
                d[key] = 4
                self.digit2set[4] = set(key)
            elif length == 3:
                d[key] = 7
                self.digit2set[7] = set(key)
            elif length == 7:
                d[key] = 8
                self.digit2set[8] = set(key)
            #
        #

    def set_six_segment_numbers(self) -> None:
        d = self.word2digit
        #
        for w in d:
            if len(w) == 6:
                one_set = self.digit2set[1]
                if set(w).intersection(one_set) != one_set:
                    d[w] = 6
                    self.digit2set[6] = set(w)
                    continue
                #
                one_and_four = self.digit2set[1].union(self.digit2set[4])
                if set(w).intersection(one_and_four) == one_and_four:
                    d[w] = 9
                    self.digit2set[9] = set(w)
                    continue
                #
                d[w] = 0
                self.digit2set[0] = set(w)
            #
        #

    def set_five_segment_numbers(self) -> None:
        d = self.word2digit
        #
        for w in d:
            if len(w) == 5:
                one_set = self.digit2set[1]
                if set(w).intersection(one_set) == one_set:
                    d[w] = 3
                    self.digit2set[3] = set(w)
                    continue
                #
                if set(w).intersection(one_set) != one_set:
                    nine_set = self.digit2set[9]
                    if nine_set.intersection(set(w)) == set(w):
                        d[w] = 5
                        self.digit2set[5] = set(w)
                        continue
                    #
                #
                d[w] = 2
                self.digit2set[2] = set(w)
            #
        #

    def get_right_side_value(self) -> int:
        right = self.line.split("|")[1]
        s = ""
        for word in right.split():
            s += str(self.word2digit[word])
        #
        return int(s)

    def start(self) -> None:
        self.word2digit = {w: Decoder.NOT_SET for w in self.line.split() if w != '|'}
        self.set_trivial_numbers()
        self.set_six_segment_numbers()
        self.set_five_segment_numbers()

# endclass


def main():
    # line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    total = 0
    for line in lines:
        dec = Decoder(line)
        dec.start()
        value = dec.get_right_side_value()
        total += value
    #
    print(total)

    # pprint(dec.word2digit)
    # print("---")
    # pprint(dec.digit2set)

##############################################################################

if __name__ == "__main__":
    main()
