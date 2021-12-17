#!/usr/bin/env python3

from functools import lru_cache
from typing import List, Optional

import helper

LITERAL = 4

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

    def get_version_sum(self) -> int:
        total = self.version

        for p in self.subpackets:
            total += p.get_version_sum()
        #
        return total

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

    def __str__(self) -> str:
        s = "Pk("
        #
        if (self.type_id == LITERAL):
            s += f"lit={self.value}"
        else:    # operator
            s += ", ".join([str(sub) for sub in self.subpackets])
        #
        s += ')'
        return s

# endclass


class Decoder:
    def __init__(self, hex_line: str) -> None:
        self.hex_line = hex_line
        self.bitvector = binarize(hex_line)
        self.i = 0
        self.version_sum = 0

    def process(self) -> None:
        p = Packet(self.bitvector, self.i)
        self.i += p.length()
        # print(p)
        self.version_sum = p.get_version_sum()
        # print(len(self.bitvector), self.i)
        # print(self.bitvector[self.i:])

    def debug(self) -> None:
        print(self.hex_line)
        print(self.bitvector)
        print("---")

# endclass


def main():
    # hex_line = "D2FE28"             # literal 2021
    # hex_line = "38006F45291200"     # operator packet with two subpackets: literal values 10 and 20
    # hex_line = "EE00D40C823060"     # operator packet with three subpackets: literal values 1, 2 and 3
    # hex_line = "8A004A801A8002F478"     # operator packet
    # hex_line = "620080001611562C8802118E34"     # operator packet
    # hex_line = "C0015000016115A2E0802F182340"     # operator packet
    # hex_line = "A0016C880162017C3686B18A3D4780"     # operator packet
    hex_line: str = helper.read("input.txt").strip()
    # bin_line: str = binarize(hex_line)

    dec = Decoder(hex_line)
    # dec.debug()

    dec.process()
    result: int = dec.version_sum
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
