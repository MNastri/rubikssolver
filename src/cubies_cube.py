from corners import Corner
from corners import CornersOrientation as CsO
from corners import CornersPermutation as CsP
from corners import (
    NUMBER_OF_CORNER_ORIENTATIONS,
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
        corners = lambda: range(NUMBER_OF_CORNERS)  # reusable range
        self.corner_permutation = CsP(Corner(idx) for idx in corners())
        self.corner_orientation = CsO(SingleCornerOrientation(0) for _ in corners())

    def _store_solved_edges(self):
        edges = lambda: range(NUMBER_OF_EDGES)  # reusable range
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

    def __mul__(self, other):
        # TODO docs. motivation? how it works?
        self._corner_multiply(other)
        # TODO EDGE MULTIPLY

    def _corner_multiply(self, other):
        new_corner_permutation = self._new_corner_permutation(other)  # TODO necessary?
        new_corner_orientation = self._new_corner_orientation(other)  # TODO necessary?
        for cor in Corner:
            self.corner_permutation[cor] = new_corner_permutation[cor]
            self.corner_orientation[cor] = new_corner_orientation[cor]

    def _new_corner_permutation(self, other):
        new_corner_permutation = [Corner.URF] * NUMBER_OF_CORNERS  # TODO necessary?
        for cor in Corner:
            corner_in_destination = other.corner_permutation[cor]
            corner_in_origin = self.corner_permutation[corner_in_destination]
            new_corner_permutation[cor] = corner_in_origin
        return new_corner_permutation

    def _new_corner_orientation(self, other):
        new_corner_orientation = [SingleCornerOrientation.normal] * NUMBER_OF_CORNERS  # TODO necessary?
        for cor in Corner:
            corner_in_destination = other.corner_permutation[cor]
            orientation_in_origin = self.corner_orientation[corner_in_destination]
            orientation_in_destination = other.corner_orientation[cor]
            orientation = orientation_in_origin + orientation_in_destination
            new_corner_orientation[cor] = orientation % NUMBER_OF_CORNER_ORIENTATIONS
        return new_corner_orientation


if __name__ == "__main__":
    my_cube = CubieCube()
    print(my_cube.corner_permutation.permutated_to_URF)
    print(my_cube.corner_permutation)
    print(my_cube)
