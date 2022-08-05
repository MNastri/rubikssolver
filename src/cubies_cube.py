from corners import Corner
from corners import CornersOrientation as CO
from corners import CornersPermutation as CP
from corners import NUMBER_OF_CORNERS
from corners import Orientation as single_corner_orientation
from edges import Edge
from edges import EdgesOrientation as EO
from edges import EdgesPermutation as EP
from edges import NUMBER_OF_EDGES
from edges import Orientation as single_edge_orientation
from interface import RubiksCube


class CubieCube(RubiksCube):
    def __init__(self):
        self._store_solved_corners()
        self._store_solved_edges()

    def _store_solved_corners(self):
        corners = lambda: range(NUMBER_OF_CORNERS)
        self.corner_permutation = CP(Corner(id) for id in corners())
        self.corner_orientation = CO(single_corner_orientation(0) for _ in corners())

    def _store_solved_edges(self):
        edges = lambda: range(NUMBER_OF_EDGES)
        self.edge_permutation = EP(Edge(id) for id in edges())
        self.edge_orientation = EO(single_edge_orientation(0) for _ in edges())

    def __str__(self):
        corners = range(NUMBER_OF_CORNERS)
        edges = range(NUMBER_OF_EDGES)
        ss = ""
        for cor in corners:
            ss += f"({self.corner_permutation[cor]},{self.corner_orientation[cor]})"
        for edg in edges:
            ss += f"({self.edge_permutation[edg]},{self.edge_orientation[edg]})"
        return ss


if __name__ == "__main__":
    my_cube = CubieCube()
    print(my_cube.corner_permutation.permutated_to_URF)
    print(my_cube.corner_permutation)
    print(my_cube)
