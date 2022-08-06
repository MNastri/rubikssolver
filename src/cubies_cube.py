from corners import Corner
from corners import CornersOrientation as CsO
from corners import CornersPermutation as CsP
from corners import (
    NUMBER_OF_CORNERS,
    SingleCornerOrientation,
)
from edges import Edge
from edges import EdgesOrientation as EsO
from edges import EdgesPermutation as EsP
from edges import (
    NUMBER_OF_EDGES,
    SingleEdgeOrientation,
)
from interface import RubiksCube


class CubieCube(RubiksCube):
    def __init__(self):
        self._store_solved_corners()
        self._store_solved_edges()

    def _store_solved_corners(self):
        corners = lambda: range(NUMBER_OF_CORNERS)
        self.corner_permutation = CsP(Corner(idx) for idx in corners())
        self.corner_orientation = CsO(SingleCornerOrientation(0) for _ in corners())

    def _store_solved_edges(self):
        edges = lambda: range(NUMBER_OF_EDGES)
        self.edge_permutation = EsP(Edge(idx) for idx in edges())
        self.edge_orientation = EsO(SingleEdgeOrientation(0) for _ in edges())

    def __str__(self):
        corners = range(NUMBER_OF_CORNERS)
        edges = range(NUMBER_OF_EDGES)
        ss = ""
        for cor in corners:
            ss += f"({self.corner_permutation[cor]},{self.corner_orientation[cor]})"
        ss += "\n"
        for edg in edges:
            ss += f"({self.edge_permutation[edg]},{self.edge_orientation[edg]})"
        return ss


if __name__ == "__main__":
    my_cube = CubieCube()
    print(my_cube.corner_permutation.permutated_to_URF)
    print(my_cube.corner_permutation)
    print(my_cube)
