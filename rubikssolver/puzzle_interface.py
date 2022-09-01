from collections import deque
from copy import deepcopy
from sys import intern
from typing import List

from rubikssolver.cubies_cube import CubieCube
from rubikssolver.moves import (
    Move,
    MOVES,
)

AVAILABLE_MOVES = {
    Move.D1,
    Move.D2,
    Move.D3,
    Move.L1,
    Move.L2,
    Move.L3,
    Move.E1,
    Move.E2,
    Move.E3,
    Move.M1,
    Move.M2,
    Move.M3,
}


class Moves(List):
    def __str__(self):
        to_string = [str(move.name) for move in self]
        return " ".join(to_string)


class Puzzle(CubieCube):
    def canonical(self):
        raise NotImplementedError

    def is_goal(self, *kwargs):
        raise NotImplementedError

    def find_setup_moves(self, piece, orientation):
        setup_move = deque()
        queue = deque()
        puzzle_trail = {intern(self.canonical()): None}
        moves_trail = {intern(self.canonical()): None}
        while not self.is_goal(piece, orientation):
            for mv in AVAILABLE_MOVES:
                current_puzzle = str(self)
                copied_puzzle = deepcopy(self)
                puzzle_to_move = copied_puzzle.from_string(current_puzzle)
                moved_puzzle = puzzle_to_move * MOVES[mv]
                if moved_puzzle.canonical() in puzzle_trail:
                    continue
                puzzle_trail[intern(moved_puzzle.canonical())] = self
                moves_trail[intern(moved_puzzle.canonical())] = mv
                queue.appendleft(moved_puzzle)
            self = queue.pop()
        while self:
            move = moves_trail[self.canonical()]
            setup_move.appendleft(move)
            self = puzzle_trail[self.canonical()]
        setup_move.popleft()
        return Moves(setup_move)
