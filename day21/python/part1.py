#!/usr/bin/env python3

import helper


class Dice:
    def __init__(self) -> None:
        self._value: int = 0
        self.counter = 0

    def next_value(self) -> int:
        self.counter += 1
        #
        self._value += 1
        if self._value > 100:
            self._value = 1
        #
        return self._value

# endclass Dice


class Player:
    def __init__(self, _id: int, line: str) -> None:
        self._id = _id
        self.pos = int(line.split()[-1])
        self.score = 0

    def is_winner(self) -> bool:
        return self.score >= 1000

    def move(self, value: int) -> None:
        for _ in range(value):
            self.pos += 1
            if self.pos > 10:
                self.pos = 1
            #
        #

    def roll(self, rolls: int, dice: Dice) -> None:
        values = sum(dice.next_value() for _ in range(rolls))
        self.move(values)
        self.score += self.pos
        #

    def __str__(self) -> str:
        return f"Player {self._id} (pos={self.pos}, score={self.score})"

# endclass Player


class Game:
    def __init__(self, fname: str) -> None:
        lines = helper.read_lines(fname)
        self.players: list[Player] = [Player(1, lines[0]), Player(2, lines[1])]
        self.next_player_idx = 0
        self.dice = Dice()

    def get_next_player(self) -> Player:
        result: Player = self.players[self.next_player_idx]
        self.next_player_idx = 1 - self.next_player_idx
        return result

    def start(self) -> None:
        # cnt = 0
        while True:
            # cnt += 1
            p: Player = self.get_next_player()
            p.roll(3, self.dice)
            # print(p)
            if p.is_winner():
                break
            #
            # if cnt > 10:
                # break
            #
        #
        loser = self.get_next_player()
        result = loser.score * self.dice.counter
        print(result)

    def debug(self) -> None:
        for p in self.players:
            print(p)

# endclass Game


def main():
    # fname = "example.txt"
    fname = "input.txt"
    game = Game(fname)
    game.debug()
    print("---")
    game.start()

##############################################################################

if __name__ == "__main__":
    main()
