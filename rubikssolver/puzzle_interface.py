from collections import deque
from copy import deepcopy
from sys import intern
from typing import List

from rubikssolver.cubies_cube import CubieCube
from rubikssolver.moves import MOVES


class Moves(List):
    def __str__(self):
        to_string = [str(move.name) for move in self]
        return " ".join(to_string)


class Puzzle(CubieCube):
    available_moves = []

    def canonical(self):
        raise NotImplementedError

    def is_goal(self, *args):
        raise NotImplementedError

    def find_setup_moves(self, piece, orientation):
        setup_move = deque()
        queue = deque()
        puzzle_trail = {intern(self.canonical()): None}
        moves_trail = {intern(self.canonical()): None}
        while not self.is_goal(piece, orientation):
            for mv in self.available_moves:
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
