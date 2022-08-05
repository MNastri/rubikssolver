from enum import Enum
from typing import List

NUMBER_OF_EDGES = 12


class Edge(Enum):
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


class EdgePermutation(List):
    # TODO check if args/kwargs are necessary when calling super
    def __init__(self, *args, **kwargs):
        super(EdgePermutation, self).__init__(*args, **kwargs)
        assert len(self) == NUMBER_OF_EDGES
        self.permutated_to_UR = self.__getitem__(0)
        self.permutated_to_UF = self.__getitem__(1)
        self.permutated_to_UL = self.__getitem__(2)
        self.permutated_to_UB = self.__getitem__(3)
        self.permutated_to_DR = self.__getitem__(4)
        self.permutated_to_DF = self.__getitem__(5)
        self.permutated_to_DL = self.__getitem__(6)
        self.permutated_to_DB = self.__getitem__(7)
        self.permutated_to_FR = self.__getitem__(8)
        self.permutated_to_FL = self.__getitem__(9)
        self.permutated_to_BL = self.__getitem__(10)
        self.permutated_to_BR = self.__getitem__(11)


if __name__ == "__main__":
    # fmt: off
    # TODO ↑ remover ↑
    test_permutation = EdgePermutation([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    # TODO ↓ remover ↓
    # fmt: on
    print(test_permutation)
    print(test_permutation.permutated_to_UR)


class EdgeOrientation(List):
    # TODO check if args/kwargs are necessary when calling super
    def __init__(self, *args, **kwargs):
        super(EdgeOrientation, self).__init__(*args, **kwargs)
        assert len(self) == NUMBER_OF_EDGES
        self.orientation_of_UR = self.__getitem__(0)
        self.orientation_of_UF = self.__getitem__(1)
        self.orientation_of_UL = self.__getitem__(2)
        self.orientation_of_UB = self.__getitem__(3)
        self.orientation_of_DR = self.__getitem__(4)
        self.orientation_of_DF = self.__getitem__(5)
        self.orientation_of_DL = self.__getitem__(6)
        self.orientation_of_DB = self.__getitem__(7)
        self.orientation_of_FR = self.__getitem__(8)
        self.orientation_of_FL = self.__getitem__(9)
        self.orientation_of_BL = self.__getitem__(10)
        self.orientation_of_BR = self.__getitem__(11)


if __name__ == "__main__":
    # fmt: off
    # TODO ↑ remover ↑
    test_orientation = EdgeOrientation([200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211])
    # TODO ↓ remover ↓
    # fmt: on
    print(test_orientation)
    print(test_orientation.orientation_of_UR)
