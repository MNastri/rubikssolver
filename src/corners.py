from enum import IntEnum
from typing import List

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


class CornersPermutation(List):
    def __init__(self, *args, **kwargs):
        super(CornersPermutation, self).__init__(*args, **kwargs)
        assert len(self) == NUMBER_OF_CORNERS
        self.permutated_to_URF = self.__getitem__(0)
        self.permutated_to_UFL = self.__getitem__(1)
        self.permutated_to_ULB = self.__getitem__(2)
        self.permutated_to_UBR = self.__getitem__(3)
        self.permutated_to_DFR = self.__getitem__(4)
        self.permutated_to_DLF = self.__getitem__(5)
        self.permutated_to_DBL = self.__getitem__(6)
        self.permutated_to_DRB = self.__getitem__(7)


if __name__ == "__main__":
    test_permutation = CornersPermutation([10, 11, 12, 13, 14, 15, 16, 17])
    print(test_permutation)
    print(test_permutation.permutated_to_URF)


class CornersOrientation(List):
    def __init__(self, *args, **kwargs):
        super(CornersOrientation, self).__init__(*args, **kwargs)
        assert len(self) == NUMBER_OF_CORNERS
        self.orientation_of_URF = self.__getitem__(0)
        self.orientation_of_UFL = self.__getitem__(1)
        self.orientation_of_ULB = self.__getitem__(2)
        self.orientation_of_UBR = self.__getitem__(3)
        self.orientation_of_DFR = self.__getitem__(4)
        self.orientation_of_DLF = self.__getitem__(5)
        self.orientation_of_DBL = self.__getitem__(6)
        self.orientation_of_DRB = self.__getitem__(7)


if __name__ == "__main__":
    test_orientation = CornersOrientation([20, 21, 22, 23, 24, 25, 26, 27])
    print(test_orientation)
    print(test_orientation.orientation_of_URF)
