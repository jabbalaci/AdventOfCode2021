#!/usr/bin/env python3

import math
from functools import lru_cache
from typing import List, Optional

import helper

LITERAL = 4

OPERATORS = {
    0: '+',
    1: '*',
    2: 'min',
    3: 'max',
    5: '>',
    6: '<',
    7: '==',
}

@lru_cache
def hex2bin(c: str) -> str:
    return bin(int(c, 16))[2:].zfill(4)


def binarize(hex_line: str) -> str:
    return "".join([hex2bin(c) for c in hex_line])


def to_dec(bin_str: str) -> int:
    return int(bin_str, 2)


class Packet:
    def __init__(self, bitvector: str, i: int, is_subpacket=False) -> None:
        self.bitvector = bitvector
        self.start_pos = i
        self.i = i
        self.is_subpacket = is_subpacket
        self.value: Optional[int] = None            # will be set if it's a literal
        self.length_type_id: Optional[int] = None   # will be set if it's an operator
        self.subpackets: List[Packet] = []          # will be filled if it's an operator
        self.consume()

    def length(self) -> int:
        return self.i - self.start_pos

    def read(self, n: int) -> str:
        s = self.bitvector[self.i:self.i+n]
        self.i += n
        return s

    def extract_literal(self) -> int:
        collect = ""
        last = False
        while not last:
            part = self.read(5)
            collect += part[1:]
            if part[0] == '0':
                last = True
            #
        #
        if not self.is_subpacket:
            extra_bits_at_end = (4 - (self.length() % 4)) % 4
            self.read(extra_bits_at_end)
        #
        return to_dec(collect)

    def consume(self) -> None:
        self.version = to_dec(self.read(3))
        self.type_id = to_dec(self.read(3))
        if (self.type_id == LITERAL):
            self.value = self.extract_literal()
        else:
            # operator
            self.length_type_id = to_dec(self.read(1))
            if self.length_type_id == 0:
                subpackets_bit_length = to_dec(self.read(15))
                end = self.i + subpackets_bit_length
                while self.i < end:
                    p = Packet(self.bitvector, self.i, is_subpacket=True)
                    self.i += p.length()
                    self.subpackets.append(p)
                #
            else:    # 1
                subpackets_number = to_dec(self.read(11))
                for _ in range(subpackets_number):
                    p = Packet(self.bitvector, self.i, is_subpacket=True)
                    self.i += p.length()
                    self.subpackets.append(p)
                #
            #
        #

    def evaluate(self) -> int:
        if (self.type_id == LITERAL):
            return self.value    # type: ignore
        else:
            op_name = self.get_operator_name()
            values = [p.evaluate() for p in self.subpackets]
            if op_name == '+':
                return sum(values)
            elif op_name == '*':
                return math.prod(values)
            elif op_name == 'min':
                return min(values)
            elif op_name == 'max':
                return max(values)
            elif op_name == '>':
                return int(values[0] > values[1])
            elif op_name == '<':
                return int(values[0] < values[1])
            elif op_name == '==':
                return int(values[0] == values[1])
            else:
                assert False

    def get_operator_name(self) -> str:
        return OPERATORS[self.type_id]

    def __str__(self) -> str:
        s = ""
        #
        if (self.type_id == LITERAL):
            s += f"{self.value}"
        else:    # operator
            op_name = self.get_operator_name()
            s += f"{op_name}("
            s += ", ".join([str(sub) for sub in self.subpackets])
            s += ')'
        #
        return s

# endclass


class Decoder:
    def __init__(self, hex_line: str) -> None:
        self.hex_line = hex_line
        self.bitvector = binarize(hex_line)
        self.i = 0

    def process(self) -> Packet:
        p = Packet(self.bitvector, self.i)
        self.i += p.length()
        return p

    def debug(self) -> None:
        print(self.hex_line)
        print(self.bitvector)
        print("---")

# endclass


def main():
    # hex_line = "C200B40A82"  # finds the sum of 1 and 2, resulting in the value 3.
    # hex_line = "04005AC33890"  # finds the product of 6 and 9, resulting in the value 54.
    # hex_line = "880086C3E88112"  # finds the minimum of 7, 8, and 9, resulting in the value 7.
    # hex_line = "CE00C43D881120"  # finds the maximum of 7, 8, and 9, resulting in the value 9.
    # hex_line = "D8005AC2A8F0"  # produces 1, because 5 is less than 15.
    # hex_line = "F600BC2D8F"  # produces 0, because 5 is not greater than 15.
    # hex_line = "9C005AC2F8F0"  # produces 0, because 5 is not equal to 15.
    # hex_line = "9C0141080250320F1802104A08"  # produces 1, because 1 + 3 = 2 * 2.
    hex_line: str = helper.read("input.txt").strip()
    # bin_line: str = binarize(hex_line)

    dec = Decoder(hex_line)
    # dec.debug()

    p: Packet = dec.process()
    print(p)
    print("---")

    result: int = p.evaluate()
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
