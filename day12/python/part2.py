#!/usr/bin/env python3

from collections import Counter
from pprint import pprint
from typing import Dict, List

import helper


def wait() -> None:
    """for debug purposes"""
    print("Press Enter to continue...", end="")
    input()


class Path:
    def __init__(self, nodes: List[str], d: Dict[str, List[str]]) -> None:
        self.nodes: List[str] = nodes.copy()
        self.d: Dict[str, List[str]] = d

    def finished(self) -> bool:
        return self.nodes[-1] == 'end'

    def is_valid(self, path: List[str]) -> bool:
        """
        Modified for Part 2.
        """
        last = path[-1]
        if last.isupper():
            return True
        #
        if last == 'start':
            return False
        #
        # else, if lowercase and not the start node
        # example: start, a, B, c, d, a
        # start: 1, a: 2, B: 1, c: 1, d: 1
        cnt = Counter(path)
        # start: 1, a: 2, c: 1, d: 1
        small = {k: v for k, v in cnt.items() if k.islower()}
        # 1, 2, 1, 1
        values = small.values()
        # 1: 3, 2: 1
        cnt2 = Counter(values)
        # if something appears three times -> not valid, stop
        if 3 in cnt2:
            return False
        # How many things appear twice? Default: just one thing.
        two = cnt2.get(2, 1)
        # If just one thing appears twice, then it's OK.
        result = (two == 1)

        # print("#", path)
        # print('#', result)
        # print("#", cnt2)
        # wait()

        return result

    def extend(self) -> List['Path']:
        can_go_to: List[Path] = []

        last = self.nodes[-1]
        values = self.d[last]
        for v in values:
            new_path = self.nodes + [v]
            if self.is_valid(new_path):
                p = Path(nodes=new_path, d=self.d)
                can_go_to.append(p)
                # print(p)
                # wait()
            #
        #
        return can_go_to

    def __str__(self) -> str:
        return " -> ".join(self.nodes)

# endclass


class Cave:
    def __init__(self, fname: str) -> None:
        lines: List[str] = helper.read_lines(fname)
        self.d: Dict[str, List[str]] = self.build_graph(lines)
        #
        self.to_extend: List[Path] = []
        self.found: List[Path] = []

    def start_exploring(self) -> None:
        # init. the to_extend list
        p = Path(nodes=['start'], d=self.d)
        self.to_extend.append(p)
        #
        while len(self.to_extend) > 0:
            top: Path = self.to_extend.pop()
            if top.finished():
                self.found.append(top)
            else:
                new_nodes = top.extend()
                self.to_extend.extend(new_nodes)
            #
        #

    def build_graph(self, lines: List[str]) -> Dict[str, List[str]]:
        d: Dict[str, List[str]] = {}
        for line in lines:
            a, b = line.split("-")
            li = d.get(a, [])
            li.append(b)
            d[a] = li
            #
            li = d.get(b, [])
            li.append(a)
            d[b] = li
        #
        return d

    def debug(self) -> None:
        pprint(self.d)

# endclass


def main():
    # fname = "example1.txt"    # 36
    # fname = "example2.txt"    # 103
    # fname = "example3.txt"    # 3509
    fname = "input.txt"

    cave = Cave(fname)
    cave.start_exploring()

    # cave.debug()
    result = len(cave.found)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
