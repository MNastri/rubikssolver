from typing import List

from rubikssolver.edges import Edge
from rubikssolver.moves import Move
from rubikssolver.puzzle_interface import Puzzle

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


class FirstStageSolver(Puzzle):
    def canonical(self):
        return str(self)

    def is_goal(self, *kwargs):
        edge = kwargs[0]
        orientation = kwargs[1]
        return self._is_buffer_edge_correct(edge, orientation)

    def _is_buffer_edge_correct(self, edge, orientation):
        return (
            self.edges_permutation[Edge.UL] == edge
            and self.edges_orientation[Edge.UL] == orientation
        )
