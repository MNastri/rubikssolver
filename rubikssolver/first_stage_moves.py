from collections import deque
from sys import intern

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


class Puzzle(CubieCube):
    def canonical(self):
        return str(self)

    def find_setup_moves(self, edge, orientation):
        solutions = list()
        queue = deque()
        trail = {intern(self.canonical()): None}
        # append_move_into_queue = queue.append if depth_first else queue.appendleft

        return solutions

    def _is_buffer_edge_correct(self, edge, orientation):
        return (
            self.edges_permutation[Edge.UL] == edge
            and self.edges_orientation[Edge.UL] == orientation
        )
