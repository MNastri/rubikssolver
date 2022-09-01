from rubikssolver import edges
from rubikssolver.edges import Edge
from rubikssolver.puzzle_interface import Puzzle

EDGE_BUFFER = edges.Edge.UR
SETUP_EDGE = edges.Edge.UL


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

    def edge_in_buffer(self):
        buffer = (
            self.edges_permutation[EDGE_BUFFER],
            self.edges_orientation[EDGE_BUFFER],
        )
        return buffer
