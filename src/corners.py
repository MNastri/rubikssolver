from enum import Enum
from typing import List

NUMBER_OF_CORNERS = 8


class Corner(Enum):
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


class SingleCornerOrientation(Enum):
    normal = 0
    turned_once = 1
    turned_twice = 2


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
