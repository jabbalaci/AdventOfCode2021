#!/usr/bin/env python3

from pprint import pprint
from typing import Dict, List

import helper


class Path:
    def __init__(self, nodes: List[str], d: Dict[str, List[str]]) -> None:
        self.nodes: List[str] = nodes.copy()
        self.d: Dict[str, List[str]] = d

    def finished(self) -> bool:
        return self.nodes[-1] == 'end'

    def is_valid(self, path: List[str]) -> bool:
        last = path[-1]
        if last.isupper():
            return True
        #
        # else, if lowercase
        beginning = path[:-1]
        return last not in beginning

    def extend(self) -> List['Path']:
        can_go_to: List[Path] = []

        last = self.nodes[-1]
        values = self.d[last]
        for v in values:
            new_path = self.nodes + [v]
            if self.is_valid(new_path):
                can_go_to.append(Path(nodes=new_path, d=self.d))
            #
        #
        return can_go_to

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
    # fname = "example1.txt"    # 10
    # fname = "example2.txt"    # 19
    # fname = "example3.txt"    # 226
    fname = "input.txt"

    cave = Cave(fname)
    cave.start_exploring()

    # cave.debug()
    result = len(cave.found)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
