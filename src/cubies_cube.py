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
    NUMBER_OF_EDGES_ORIENTATIONS,
    SingleEdgeOrientation,
)
from rubiks_definitions import CORNER_FACELETS
from facelets import NUMBER_OF_FACELETS


class CubieCube:
    def __init__(self):
        self._store_solved_corners()
        self._store_solved_edges()

    def _store_solved_corners(self):
        corners = lambda: range(NUMBER_OF_CORNERS)  # reusable range
        self.corners_permutation = CsP(Corner(idx) for idx in corners())
        self.corners_orientation = CsO(SingleCornerOrientation(0) for _ in corners())

    def _store_solved_edges(self):
        edges = lambda: range(NUMBER_OF_EDGES)  # reusable range
        self.edges_permutation = EsP(Edge(idx) for idx in edges())
        self.edges_orientation = EsO(SingleEdgeOrientation(0) for _ in edges())

    def __str__(self):
        corners = range(NUMBER_OF_CORNERS)
        edges = range(NUMBER_OF_EDGES)
        ss = "Corners:"
        for cor in corners:
            ss += f"({self.corners_permutation[cor]},{self.corners_orientation[cor]})"
        ss += "\nEdges:"
        for edg in edges:
            ss += f"({self.edges_permutation[edg]},{self.edges_orientation[edg]})"
        return ss

    def from_string(self, s):  # TODO
        """
        Reads a string of facelets and replaces the cubies with the cubies created from
        the string
        """
        assert len(s) == NUMBER_OF_FACELETS
        corners_characters = self._get_corners_characters_from(s)
        # TODO check if received corners are valid
        print(corners_characters)
        reference_facelets = self._get_corner_reference_facelets_from(corners_characters)
        print(reference_facelets)
        corners_names = self._get_corners_from(corners_characters, reference_facelets)
        print(corners_names)
        corners_permutation = [Corner.get_corner_from(name) for name in corners_names]
        print(corners_permutation)
        corners_orientation = [SingleCornerOrientation(value) for value in reference_facelets]
        print(corners_orientation)
        # self._check_the_edge_facelets_from(s)  # TODO EDGES
        # self._check_number_of_colors_is_correct(s)  # TODO checking number of colors
        # self._check_orientation(s)  # TODO check if orientation of corners is (0 mod 3) and of edges is (0 mod 2)
        return self

    def _get_corners_characters_from(self, s: str):  # TODO renaming overhaul?
        corners = []
        for corner in CORNER_FACELETS:
            character_in_string = lambda facelet: s[facelet]
            mapped_corners = map(character_in_string, corner)
            corners += (list(mapped_corners),)
        return corners

    def _get_reference_facelets_from(self, corner_names):  # TODO renaming overhaul!
        new_list = []
        for sublist in corner_names:
            new_list += (
                (sublist.index("U") if "U" in sublist else sublist.index("D")),
            )
        return new_list

    def _get_corners_from(self, corner_names, reference_facelets):  # TODO renaming overhaul?
        corners = []
        for cor, ref in zip(corner_names, reference_facelets):
            reference_facelet = cor[ref]
            clockwised_facelet = cor[(ref + 1) % 3]
            anticlockwised_facelet = cor[(ref + 2) % 3]
            corners += (
                (reference_facelet + clockwised_facelet + anticlockwised_facelet),
            )
        return corners

    def __mul__(self, other):
        """
        applies corners and edges multiplication to this cube.
        """
        self._corners_multiply(other)
        self._edges_multiply(other)
        return self

    def _corners_multiply(self, other):
        self.corners_permutation = self._multiply_corners_permutation(other)
        self.corners_orientation = self._multiply_corners_orientation(other)

    def _multiply_corners_permutation(self, other):
        """
        let
        A = "some permutation of corners"
        B = "some permutation of corners"
        M = A * B
        A[c] = "corner that replaces corner c in permutation A"
        then
        M[c] = A[B[c]]

        EXAMPLE: if "Y move = F turn * R turn", what corner replaces UBR? Answer: UFL
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

    def _multiply_corners_orientation(self, other):
        """
        let
        A = "some permutation of corners"
        B = "some permutation of corners"
        M = A * B
        A[c] = "corner that replaces corner c in permutation A"
        A[c].ori = "orientation of corner A[c]"
        then
        M[c].ori = (A[B[c]].ori + B[c].ori) mod 3

        EXAMPLE: if "Y move = F turn * R turn", what is the orientation of the corner
        that replaces UBR? Answer: 2"
          M[c].ori = A[B[c]].ori + B[c].ori     → Y[UBR].ori = F[R[UBR]].ori+R[UBR].ori
            R[UBR] = UFR  and  R[UBR].ori = 1   → Y[UBR].ori = F[UFR].ori+R[UBR].ori
        F[UFR].ori = 1    and  R[UBR].ori = 1   → Y[UBR].ori = 2
        """
        new_corners_orientation = [SingleCornerOrientation.normal] * NUMBER_OF_CORNERS
        for cor in Corner:
            corner_in_destination = other.corners_permutation[cor]
            orientation_in_origin = self.corners_orientation[corner_in_destination]
            orientation_in_destination = other.corners_orientation[cor]
            orientation = orientation_in_origin + orientation_in_destination
            new_corners_orientation[cor] = orientation % NUMBER_OF_CORNER_ORIENTATIONS
        return new_corners_orientation

    def _edges_multiply(self, other):
        self.edges_permutation = self._multiply_edges_permutation(other)
        self.edges_orientation = self._multiply_edges_orientation(other)

    def _multiply_edges_permutation(self, other):
        """
        let
        A = "some permutation of edges"
        B = "some permutation of edges"
        M = A * B
        A[e] = "edge that replaces edge c in permutation A"
        then
        M[e] = A[B[e]]

        EXAMPLE: if "Y move = F turn * R turn", what edge replaces UR? Answer: UF
         M[e] = A[B[e]] →    Y[UR] = F[R[UR]]
        R[UR] = FR      →    Y[UR] = F[FR]
        F[FR] = UF      →    Y[UR] = UF
        """
        new_edges_permutation = [Edge.UR] * NUMBER_OF_EDGES
        for edg in Edge:
            edge_in_destination = other.edges_permutation[edg]
            edge_in_origin = self.edges_permutation[edge_in_destination]
            new_edges_permutation[edg] = edge_in_origin
        return new_edges_permutation

    def _multiply_edges_orientation(self, other):
        """
        let
        A = "some permutation of edges"
        B = "some permutation of edges"
        M = A * B
        A[e] = "edge that replaces edge e in permutation A"
        A[e].ori = "orientation of edge A[e]"
        then
        M[e].ori = (A[B[e]].ori + B[e].ori) mod 2

        EXAMPLE: if "Y move = F turn * R turn", what is the orientation of the edge
        that replaces UR? Answer: 1"
         M[e].ori = A[B[e]].ori + B[e].ori  →   Y[UR].ori = F[R[UR]].ori+R[UR].ori
            R[UR] = FR  and  R[UR].ori=0    →   Y[UR].ori = F[FR].ori+R[UR].ori
        F[FR].ori = 1   and  R[UR].ori=0    →  Y[UBR].ori = 1
        """
        new_edges_orientation = [SingleEdgeOrientation.normal] * NUMBER_OF_EDGES
        for edg in Edge:
            edge_in_destination = other.edges_permutation[edg]
            orientation_in_origin = self.edges_orientation[edge_in_destination]
            orientation_in_destination = other.edges_orientation[edg]
            orientation = orientation_in_origin + orientation_in_destination
            new_edges_orientation[edg] = orientation % NUMBER_OF_EDGES_ORIENTATIONS
        return new_edges_orientation


if __name__ == "__main__":
    my_cube = CubieCube()
    print(my_cube.corners_permutation.replaces_URF)
    print(my_cube.corners_permutation)
    print(my_cube)
    cube_str = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
    CubieCube().from_string(cube_str)
