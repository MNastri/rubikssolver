from rubikssolver.colors import Color
from rubikssolver.corners import Corner
from rubikssolver.corners import CornersOrientation as CsO
from rubikssolver.corners import CornersPermutation as CsP
from rubikssolver.corners import (
    NUMBER_OF_CORNER_ORIENTATIONS,
    NUMBER_OF_CORNERS,
    SingleCornerOrientation,
)
from rubikssolver.edges import Edge
from rubikssolver.edges import EdgesOrientation as EsO
from rubikssolver.edges import EdgesPermutation as EsP
from rubikssolver.edges import (
    NUMBER_OF_EDGES,
    NUMBER_OF_EDGES_ORIENTATIONS,
    SingleEdgeOrientation,
)
from rubikssolver.facelets import NUMBER_OF_FACELETS
from rubikssolver.rubiks_definitions import (
    CORNER_FACELETS,
    EDGE_FACELETS,
    get_edge_name_from,
)


class CubieCube:
    """
    A Rubik's cube on the cubie level. Cubies are represented by corners/edges
    with their orientations.
    """
    corners_permutation: CsP
    corners_orientation: CsO
    edges_permutation: EsP
    edges_orientation: EsO

    def __init__(self, corners_permutation=None, corners_orientation=None, edges_permutation=None, edges_orientation=None):
        if not any([corners_permutation, corners_orientation, edges_permutation, edges_orientation]):
            self._store_solved_corners()
            self._store_solved_edges()
        else:
            self._store_initialized_parameters(corners_permutation, corners_orientation, edges_permutation, edges_orientation)

    def _store_solved_corners(self):
        corners = lambda: range(NUMBER_OF_CORNERS)  # reusable range
        self.corners_permutation = CsP(Corner(idx) for idx in corners())
        self.corners_orientation = CsO(SingleCornerOrientation(0) for _ in corners())

    def _store_solved_edges(self):
        edges = lambda: range(NUMBER_OF_EDGES)  # reusable range
        self.edges_permutation = EsP(Edge(idx) for idx in edges())
        self.edges_orientation = EsO(SingleEdgeOrientation(0) for _ in edges())

    def _store_initialized_parameters(self, corners_permutation, corners_orientation, edges_permutation, edges_orientation):
        if not all(
            [corners_permutation, corners_orientation, edges_permutation,
             edges_orientation]
        ):
            raise NotImplementedError("all fields must not be None")
        self.corners_permutation = CsP(corners_permutation)
        self.corners_orientation = CsO(corners_orientation)
        self.edges_permutation = EsP(edges_permutation)
        self.edges_orientation = EsO(edges_orientation)

    def __str__(self):
        corners = self._corners_to_string()
        edges = self._edges_to_string()
        centers = self._centers_to_string()
        facelets = [
            corner if corner != " " else edge if edge != " " else center
            for corner, edge, center in zip(corners, edges, centers)
        ]
        ss = "".join(facelets)
        return ss

    def _corners_to_string(self) -> str:
        ss = [" "] * NUMBER_OF_FACELETS
        for corner_number in range(NUMBER_OF_CORNERS):
            corner = self.corners_permutation[corner_number]
            orientation = self.corners_orientation[corner_number]

            positions = CORNER_FACELETS[corner_number]
            facelets = CORNER_FACELETS[corner]

            for orientation_number in range(NUMBER_OF_CORNER_ORIENTATIONS):
                new_orientation = -orientation + orientation_number
                adjusted_orientation = new_orientation % NUMBER_OF_CORNER_ORIENTATIONS

                position = positions[orientation_number]
                facelet = facelets[adjusted_orientation]

                character = facelet.name[0]
                ss[position] = character
        return "".join(ss)

    def _edges_to_string(self) -> str:
        ss = [" "] * NUMBER_OF_FACELETS
        for edge_number in range(NUMBER_OF_EDGES):
            edge = self.edges_permutation[edge_number]
            orientation = self.edges_orientation[edge_number]

            positions = EDGE_FACELETS[edge_number]
            facelets = EDGE_FACELETS[edge]

            for orientation_number in range(NUMBER_OF_EDGES_ORIENTATIONS):
                new_orientation = -orientation + orientation_number
                adjusted_orientation = new_orientation % NUMBER_OF_EDGES_ORIENTATIONS

                position = positions[orientation_number]
                facelet = facelets[adjusted_orientation]

                character = facelet.name[0]
                ss[position] = character
        return "".join(ss)

    def _centers_to_string(self):
        prefix = suffix = "    "
        faces = [prefix + color.name + suffix for color in Color]
        return "".join(faces)

    def __repr__(self):
        corners = range(NUMBER_OF_CORNERS)
        edges = range(NUMBER_OF_EDGES)
        ss = "Corners (id,ori):"
        for cor in corners:
            ss += f"({self.corners_permutation[cor]},{self.corners_orientation[cor]})"
        ss += "\nEdges (id,ori):"
        for edg in edges:
            ss += f"({self.edges_permutation[edg]},{self.edges_orientation[edg]})"
        return ss

    def from_string(self, s):  # TODO
        """
        Reads a string of facelets and replaces the cubies with the cubies created from
        the string
        """
        assert len(s) == NUMBER_OF_FACELETS
        self._create_corners_from_string(s)
        self._create_edges_from_string(s)
        # self._check_number_of_colors_is_correct(s)  # TODO checking number of colors
        return self

    def _create_corners_from_string(self, s):
        corners_characters = self._get_corners_characters_from(s)
        # TODO check if received corners are valid
        reference_facelets = self._get_corners_reference_facelet_from(
            corners_characters
        )
        corners_names = self._get_corners_from(corners_characters, reference_facelets)
        corners_permutation = [Corner.get_corner_from(name) for name in corners_names]
        corners_orientation = [
            SingleCornerOrientation(value) for value in reference_facelets
        ]
        self.corners_permutation = CsP(corners_permutation)
        self.corners_orientation = CsO(corners_orientation)

    def _create_edges_from_string(self, s):
        edge_characters = self._get_edges_characters_from(s)
        # TODO check if received edges are valid
        reference_facelets = self._get_edges_reference_facelet_from(edge_characters)
        edges_names = self._get_edges_from(edge_characters, reference_facelets)
        edges_permutation = [Edge.get_edge_from(name) for name in edges_names]
        edges_orientation = [
            SingleEdgeOrientation(value) for value in reference_facelets
        ]
        self.edges_permutation = EsP(edges_permutation)
        self.edges_orientation = EsO(edges_orientation)

    @staticmethod
    def _get_corners_characters_from(s):
        corners = []
        for facelets_idx in CORNER_FACELETS:
            get_character = lambda idx: s[idx]
            corner_as_characters = map(get_character, facelets_idx)
            corners += (list(corner_as_characters),)
        return corners

    @staticmethod
    def _get_corners_reference_facelet_from(corner_characters):
        references = []
        for corner in corner_characters:
            if Color.U.name in corner:
                reference_to_add = corner.index(Color.U.name)
            else:
                reference_to_add = corner.index(Color.D.name)
            references += (reference_to_add,)
        return references

    @staticmethod
    def _get_corners_from(corner_characters, reference_facelets):
        corners = []
        for cor, ref in zip(corner_characters, reference_facelets):
            reference_facelet = cor[ref]
            clockwised_facelet = cor[(ref + 1) % NUMBER_OF_CORNER_ORIENTATIONS]
            anticlockwised_facelet = cor[(ref + 2) % NUMBER_OF_CORNER_ORIENTATIONS]
            corners += (
                (reference_facelet + clockwised_facelet + anticlockwised_facelet),
            )
        return corners

    @staticmethod
    def _get_edges_characters_from(s):
        edges = []
        for edge in EDGE_FACELETS:
            character = lambda idx: s[idx]
            mapped_edges = map(character, edge)
            edges += (list(mapped_edges),)
        return edges

    @staticmethod
    def _get_edges_reference_facelet_from(edge_characters):
        references = []
        for edge in edge_characters:
            if Color.U.name in edge:
                reference_to_add = edge.index(Color.U.name)
            elif Color.D.name in edge:
                reference_to_add = edge.index(Color.D.name)
            elif Color.F.name in edge:
                reference_to_add = edge.index(Color.F.name)
            else:
                reference_to_add = edge.index(Color.B.name)
            references += (reference_to_add,)
        return references

    @staticmethod
    def _get_edges_from(edge_characters, reference_facelets):
        edges = []
        for edg, ref in zip(edge_characters, reference_facelets):
            reference_facelet = edg[ref]
            flipped_facelet = edg[(ref + 1) % NUMBER_OF_EDGES_ORIENTATIONS]
            edges += ((reference_facelet + flipped_facelet),)
        return edges

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

    def are_all_edges_solved(self):
        compare = []
        for edge in range(NUMBER_OF_EDGES):
            actual_edge = self.edges_permutation[edge].name
            orientation = self.edges_orientation[edge]
            should_be_edge = get_edge_name_from(edge_number=edge)
            compare += (
                actual_edge == should_be_edge
                and orientation == SingleEdgeOrientation.normal,
            )
        return all(compare)


if __name__ == "__main__":
    my_cube = CubieCube()
    print(my_cube.corners_permutation.replaces_URF)
    print(my_cube.corners_orientation.orientation_of_URF)
    print()
    print(my_cube.edges_permutation.permutated_to_UR)
    print(my_cube.edges_orientation.orientation_of_UR)
    print()
    print(my_cube.corners_permutation)
    print(my_cube.corners_orientation)
    print()
    print(my_cube.edges_permutation)
    print(my_cube.edges_orientation)
    print()
    print(my_cube)
    print()
    print()
    print()

    cube_strings = {
        "Example": "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL",
        "Solved": "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB",
        "U3": "UUUUUUUUUFFFRRRRRRLLLFFFFFFDDDDDDDDDBBBLLLLLLRRRBBBBBB",
        "F": "UUUUUULLLURRURRURRFFFFFFFFFRRRDDDDDDLLDLLDLLDBBBBBBBBB",
        "R2": "UUDUUDUUDRRRRRRRRRFFBFFBFFBDDUDDUDDULLLLLLLLLFBBFBBFBB",
    }

    my_cube = CubieCube().from_string(cube_strings["Example"])
    print(my_cube.corners_permutation.replaces_URF)
    print(my_cube.corners_orientation.orientation_of_URF)
    print()
    print(my_cube.edges_permutation.permutated_to_UR)
    print(my_cube.edges_orientation.orientation_of_UR)
    print()
    print(my_cube.corners_permutation)
    print(my_cube.corners_orientation)
    print()
    print(my_cube.edges_permutation)
    print(my_cube.edges_orientation)
    print()
    print(repr(my_cube))
    print()
    print(my_cube)
