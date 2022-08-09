from enum import IntEnum
from typing import List

NUMBER_OF_CORNER_ORIENTATIONS = 3
NUMBER_OF_CORNERS = 8


class Corner(IntEnum):
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7

    @classmethod
    def get_corner_from(cls, name: str):
        name = name.upper()
        assert name in Corner.__dict__
        return Corner.__getattr__(name)

    # ┌──┬──┬──┐
    # │2 │  │3 │
    # ├──┼──┼──┤
    # │  │  │  │
    # ├──┼──┼──┤
    # │1 │  │0 │
    # └──┴──┴──┘
    # ┌──┬──┬──┐
    # │  │  │  │
    # ├──┼──┼──┤
    # │  │  │  │
    # ├──┼──┼──┤
    # │  │  │  │
    # └──┴──┴──┘
    # ┌──┬──┬──┐
    # │6 │  │7 │
    # ├──┼──┼──┤
    # │  │  │  │
    # ├──┼──┼──┤
    # │5 │  │4 │
    # └──┴──┴──┘


class SingleCornerOrientation(IntEnum):
    """The U and D facelets are the reference for orientation on the corner as
    well as for the corner positions.
    If the reference facelet for the corner matches the reference facelet of the
    corner position, we define this a normal orientation. If the reference
    facelet of the corner is found after turning clockwise the reference facelet
    of the corner position, then the orientation is called clockwised.

    When the orientations of all edges and corners are 0 the used reference
    frame has the property that 10 of the 18 possible cube moves do not change
    these orientations.

    --------
    EXAMPLES
    --------
    URF corner in URF positions:
        U facelet in U position => NORMAL ORIENTATION
        R facelet in R position
        F facelet in F position
    URF corner in URF positions:
        F facelet in U position
        U facelet in R position => CLOCKWISED
        R facelet in F position
    URF corner in UFL positions:
        U facelet in U position => NORMAL ORIENTATION
        R facelet in F position
        F facelet in L position
    URF corner in UFL positions
        F facelet in U position
        U facelet in F position => CLOCKWISED
        R facelet in L position
    URF corner in UFL position
        R facelet in U position
        F facelet in F position
        U facelet in L position => ANTICLOCKWISED
    DRF corner in UFL position = normal orientation
        D facelet in U position => NORMAL
        F facelet in F position
        R facelet in L position
    """

    normal = 0
    clockwised = 1
    anticlockwised = 2

    @classmethod
    def get_corner_orientation_from(cls, name: str):
        name = name.upper()
        assert name in Corner.__dict__
        return Corner.__getattr__(name)


class CornersPermutation(List):
    @property
    def replaces_URF(self):
        return self.__getitem__(0)

    @property
    def replaces_UFL(self):
        return self.__getitem__(1)

    @property
    def replaces_ULB(self):
        return self.__getitem__(2)

    @property
    def replaces_UBR(self):
        return self.__getitem__(3)

    @property
    def replaces_DFR(self):
        return self.__getitem__(4)

    @property
    def replaces_DLF(self):
        return self.__getitem__(5)

    @property
    def replaces_DBL(self):
        return self.__getitem__(6)

    @property
    def replaces_DRB(self):
        return self.__getitem__(7)


if __name__ == "__main__":
    test_permutation = CornersPermutation([10, 11, 12, 13, 14, 15, 16, 17])
    print(test_permutation)
    print(test_permutation.replaces_URF)


class CornersOrientation(List):
    @property
    def orientation_of_URF(self):
        return self.__getitem__(0)

    @property
    def orientation_of_UFL(self):
        return self.__getitem__(1)

    @property
    def orientation_of_ULB(self):
        return self.__getitem__(2)

    @property
    def orientation_of_UBR(self):
        return self.__getitem__(3)

    @property
    def orientation_of_DFR(self):
        return self.__getitem__(4)

    @property
    def orientation_of_DLF(self):
        return self.__getitem__(5)

    @property
    def orientation_of_DBL(self):
        return self.__getitem__(6)

    @property
    def orientation_of_DRB(self):
        return self.__getitem__(7)


if __name__ == "__main__":
    test_orientation = CornersOrientation([20, 21, 22, 23, 24, 25, 26, 27])
    print(test_orientation)
    print(test_orientation.orientation_of_URF)
