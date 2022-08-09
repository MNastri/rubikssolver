from enum import IntEnum
from typing import List

NUMBER_OF_EDGES_ORIENTATIONS = 2
NUMBER_OF_EDGES = 12


class Edge(IntEnum):
    UR = 0
    UF = 1
    UL = 2
    UB = 3
    DR = 4
    DF = 5
    DL = 6
    DB = 7
    FR = 8
    FL = 9
    BL = 10
    BR = 11

    @classmethod
    def get_edge_from(cls, name: str):
        name = name.upper()
        assert name in Edge.__dict__
        return Edge.__getattr__(name)

    # ┌──┬──┬──┐
    # │  │3 │  │
    # ├──┼──┼──┤
    # │2 │  │0 │
    # ├──┼──┼──┤
    # │  │1 │  │
    # └──┴──┴──┘
    # ┌──┬──┬──┐
    # │10│  │11│
    # ├──┼──┼──┤
    # │  │  │  │
    # ├──┼──┼──┤
    # │9 │  │8 │
    # └──┴──┴──┘
    # ┌──┬──┬──┐
    # │  │7 │  │
    # ├──┼──┼──┤
    # │6 │  │4 │
    # ├──┼──┼──┤
    # │  │5 │  │
    # └──┴──┴──┘


class SingleEdgeOrientation(IntEnum):
    """The U and D facelets and the F and B facelets of the FR, FL, BL and BR
    edges are the reference for orientation on the edge as well as for the edge
    positions.
    If the reference facelet for the edge matches the reference facelet of the
    edge position, we define this a normal orientation. If the reference
    facelet of the edge is found after flipping the reference facelet of the
    edge position, then the orientation is called fliped.

    When the orientations of all edges and corners are 0 the used reference
    frame has the property that 10 of the 18 possible cube moves do not change
    these orientations.
    """

    normal = 0
    fliped = 1


class EdgesPermutation(List):
    @property
    def permutated_to_UR(self):
        return self.__getitem__(0)

    @property
    def permutated_to_UF(self):
        return self.__getitem__(1)

    @property
    def permutated_to_UL(self):
        return self.__getitem__(2)

    @property
    def permutated_to_UB(self):
        return self.__getitem__(3)

    @property
    def permutated_to_DR(self):
        return self.__getitem__(4)

    @property
    def permutated_to_DF(self):
        return self.__getitem__(5)

    @property
    def permutated_to_DL(self):
        return self.__getitem__(6)

    @property
    def permutated_to_DB(self):
        return self.__getitem__(7)

    @property
    def permutated_to_FR(self):
        return self.__getitem__(8)

    @property
    def permutated_to_FL(self):
        return self.__getitem__(9)

    @property
    def permutated_to_BL(self):
        return self.__getitem__(10)

    @property
    def permutated_to_BR(self):
        return self.__getitem__(11)


if __name__ == "__main__":
    test_permutation = EdgesPermutation(
        [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
    )
    print(test_permutation)
    print(test_permutation.permutated_to_UR)


class EdgesOrientation(List):
    @property
    def orientation_of_UR(self):
        return self.__getitem__(0)

    @property
    def orientation_of_UF(self):
        return self.__getitem__(1)

    @property
    def orientation_of_UL(self):
        return self.__getitem__(2)

    @property
    def orientation_of_UB(self):
        return self.__getitem__(3)

    @property
    def orientation_of_DR(self):
        return self.__getitem__(4)

    @property
    def orientation_of_DF(self):
        return self.__getitem__(5)

    @property
    def orientation_of_DL(self):
        return self.__getitem__(6)

    @property
    def orientation_of_DB(self):
        return self.__getitem__(7)

    @property
    def orientation_of_FR(self):
        return self.__getitem__(8)

    @property
    def orientation_of_FL(self):
        return self.__getitem__(9)

    @property
    def orientation_of_BL(self):
        return self.__getitem__(10)

    @property
    def orientation_of_BR(self):
        return self.__getitem__(11)


if __name__ == "__main__":
    test_orientation = EdgesOrientation(
        [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]
    )
    print(test_orientation)
    print(test_orientation.orientation_of_UR)
