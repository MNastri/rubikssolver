from collections import deque
from sys import intern
from typing import List

from rubikssolver.cubies_cube import CubieCube
from rubikssolver.edges import Edge
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
        return str(self)

    def is_goal(self, *kwargs):
        edge = kwargs[0]
        orientation = kwargs[1]
        return self._is_buffer_edge_correct(edge, orientation)

    def find_setup_moves(self, edge, orientation):
        setup_move = deque()
        queue = deque()
        puzzle_trail = {intern(self.canonical()): None}
        moves_trail = {intern(self.canonical()): None}
        while not self.is_goal(edge, orientation):
            for mv in AVAILABLE_MOVES:
                new_puzzle = Puzzle().from_string(str(self))
                moved_puzzle = new_puzzle * MOVES[mv]
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

    def _is_buffer_edge_correct(self, edge, orientation):
        return (
            self.edges_permutation[Edge.UL] == edge
            and self.edges_orientation[Edge.UL] == orientation
        )
