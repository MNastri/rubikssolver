from rubikssolver import edges
from rubikssolver.edges import Edge
from rubikssolver.moves import Move
from rubikssolver.puzzle_interface import Puzzle

BUFFER_EDGE = edges.Edge.UR
SETUP_EDGE = edges.Edge.UL

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


class FirstStageSolver(Puzzle):
    available_moves = AVAILABLE_MOVES
    buffer_edge = BUFFER_EDGE
    setup_edge = SETUP_EDGE

    def canonical(self):
        return str(self)

    def is_goal(self, *kwargs):
        edge = kwargs[0]
        orientation = kwargs[1]
        return self._is_setup_edge_correct(edge, orientation)

    def _is_setup_edge_correct(self, edge, orientation):
        return (
            self.edges_permutation[self.setup_edge] == edge
            and self.edges_orientation[self.setup_edge] == orientation
        )

    def edge_in_buffer(self):
        buffer = (
            self.edges_permutation[self.buffer_edge],
            self.edges_orientation[self.buffer_edge],
        )
        return buffer
