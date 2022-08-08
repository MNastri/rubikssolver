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
        self.corners_permutation = CsP(Corner(idx) for idx in corners())
        self.corners_orientation = CsO(SingleCornerOrientation(0) for _ in corners())

    def _store_solved_edges(self):
        edges = lambda: range(NUMBER_OF_EDGES)  # reusable range
        self.edge_permutation = EsP(Edge(idx) for idx in edges())
        self.edge_orientation = EsO(SingleEdgeOrientation(0) for _ in edges())

    def __str__(self):
        corners = range(NUMBER_OF_CORNERS)
        edges = range(NUMBER_OF_EDGES)
        ss = ""
        for cor in corners:
            ss += f"({self.corners_permutation[cor]},{self.corners_orientation[cor]})"
        ss += "\n"
        for edg in edges:
            ss += f"({self.edge_permutation[edg]},{self.edge_orientation[edg]})"
        return ss

    def __mul__(self, other):
        """
        applies corner and edge multiplication to this cube.
        """
        # TODO docs. motivation? how it works?
        self._corner_multiply(other)
        # TODO EDGE MULTIPLY

    def _corner_multiply(self, other):
        self.corners_permutation = self._multiply_corner_permutation(other)
        self.corners_orientation = self._multiply_corner_orientation(other)

    def _multiply_corner_permutation(self, other):
        """
        let
        A = "some permutation of corners"
        B = "some permutation of corners"
        M = A * B
        A[c] = "corner that replaces corner c in permutation A"
        then
        M[c] = A[B[c]]

        EXAMPLE: if "Y move = F turn * R turn", what corner replaces UBR? Answer: UFL"
            M[c] = A[B[c]]  →    Y[UBR] = F[R[UBR]]
          R[UBR] = URF      →    Y[UBR] = F[URF]
          F[URF] = UFL      →    Y[UBR] = UFL
        """
        new_corners_permutation = [Corner.URF] * NUMBER_OF_CORNERS
        for cor in Corner:
            corner_in_destination = other.corners_permutation[cor]
            corner_in_origin = self.corners_permutation[corner_in_destination]
            new_corners_permutation[cor] = corner_in_origin
        return new_corners_permutation

    def _multiply_corner_orientation(self, other):
        """
        let
        A = "some permutation of corners"
        B = "some permutation of corners"
        M = A * B
        A[c] = "corner that replaces corner c in permutation A"
        A[c].ori = "orientation of corner A[c]"
        then
        M[c].ori = (A[B[c]].ori + B[c].ori) % 3

        EXAMPLE: if "Y move = F turn * R turn", what is the orientation of the corner
        that replaces UBR? Answer: 2"
        M[c].ori = A[B[c]].ori + B[c].ori   →   Y[UBR].ori = F[R[UBR]].ori+R[UBR].ori
        R[UBR]=UFR  and  R[UBR].ori=1       →   Y[UBR].ori = F[UFR].ori+R[UBR].ori
        F[UFR].ori=1  and  R[UBR].ori=1     →   Y[UBR].ori = 2
        """
        new_corners_orientation = [SingleCornerOrientation.normal] * NUMBER_OF_CORNERS
        for cor in Corner:
            corner_in_destination = other.corners_permutation[cor]
            orientation_in_origin = self.corners_orientation[corner_in_destination]
            orientation_in_destination = other.corners_orientation[cor]
            orientation = orientation_in_origin + orientation_in_destination
            new_corners_orientation[cor] = orientation % NUMBER_OF_CORNER_ORIENTATIONS
        return new_corners_orientation


if __name__ == "__main__":
    my_cube = CubieCube()
    print(my_cube.corner_permutation.permutated_to_URF)
    print(my_cube.corner_permutation)
    print(my_cube)
