#!/usr/bin/env python3

from typing import Optional

import helper


class Cell:
    def __init__(self, value: int) -> None:
        self.value = value
        self._mark = False

    def is_marked(self) -> bool:
        return self._mark

    def marked(self):
        self._mark = True

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return "{0}{1}".format(self.value, "*" if self._mark else "")


class Board:
    def __init__(self, line: str) -> None:
        self.matrix: list[list[Cell]] = []
        self.parse(line)

    def parse(self, line: str) -> None:
        parts = line.split("\n")
        for row in parts:
            numbers = [int(s) for s in row.split()]
            cells = [Cell(n) for n in numbers]
            self.matrix.append(cells)

    def mark_number(self, number: int) -> None:
        for rows in self.matrix:
            for cell in rows:
                if cell.value == number:
                    cell.marked()

    def get_column(self, idx: int) -> list[Cell]:
        return [row[idx] for row in self.matrix]

    def is_winner(self) -> bool:
        for row in self.matrix:
            if all([cell.is_marked() for cell in row]):
                return True
            #
        #
        no_of_columns = len(self.matrix[0])
        for i in range(no_of_columns):
            column = self.get_column(i)
            if all([cell.is_marked() for cell in column]):
                return True
            #
        #
        return False

    def get_cells(self, marked=False) -> list[Cell]:
        li = []
        for row in self.matrix:
            for cell in row:
                if cell.is_marked() == marked:
                    li.append(cell)
                #
            #
        #
        return li

    def __str__(self) -> str:
        sb = []
        for row in self.matrix:
            for cell in row:
                sb.append(str(cell))
                sb.append(" ")
            #
            sb.append("\n")
        #
        return "".join(sb)


class Bingo:
    def __init__(self, fname: str) -> None:
        self.numbers: list[Cell] = []
        self.boards: list[Board] = []
        self.winning_order: list[int] = []
        #
        content = helper.read(fname).strip()
        self.parse(content)

    def register_numbers(self, line: str) -> None:
        self.numbers = [Cell(int(s)) for s in line.split(",")]

    def register_boards(self, lines: list[str]) -> None:
        for line in lines:
            self.boards.append(Board(line))

    def parse(self, content: str) -> None:
        parts = content.split("\n\n")
        self.register_numbers(parts[0])
        self.register_boards(parts[1:])

    def register_winning_board(self, idx: int) -> None:
        if idx not in self.winning_order:
            self.winning_order.append(idx)

    def mark_number_on_boards(self, number: int) -> None:
        for idx, board in enumerate(self.boards):
            board.mark_number(number)
            if board.is_winner():
                self.register_winning_board(idx)

    def get_winner_board(self) -> Optional[Board]:
        for board in self.boards:
            if board.is_winner():
                return board
            #
        #
        return None

    def get_last_winner(self) -> Board:
        last_winner_idx = self.winning_order[-1]
        return self.boards[last_winner_idx]

    def start(self) -> None:
        last_number = 0
        for cell in self.numbers:
            number: int = cell.value
            cell.marked()
            self.mark_number_on_boards(number)
            if len(self.boards) == len(self.winning_order):    # all boards won
                last_number = number
                break
        #
        last_winner = self.get_last_winner()
        # print("----------")
        print("Number:", last_number)
        print()
        print(last_winner)
        result = self.get_result(last_number, last_winner)
        print(result)

    def get_result(self, number: int, board: Board) -> int:
        total = sum([cell.value for cell in board.get_cells(marked=False)])
        return number * total

    def __str__(self) -> str:
        sb = []
        sb.append(str(self.numbers))
        sb.append("\n")
        sb.append("\n")
        for board in self.boards:
            sb.append(str(board))
            sb.append("\n")
        #
        return "".join(sb)


def main():
    # game = Bingo("example.txt")
    game = Bingo("input.txt")

    # print(game)
    game.start()

##############################################################################

if __name__ == "__main__":
    main()
