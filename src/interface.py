from abc import (
    ABC,
    abstractmethod,
)
from enum import Enum


class RubiksCube(ABC):
    @abstractmethod
    def __init__(self, facelets=None):
        if facelets:
            self.facelets = facelets
        else:
            self.facelets = ""

    @abstractmethod
    def solve_first_cross(self):
        """solves the cross on the first face"""
        raise NotImplementedError

    @abstractmethod
    def solve_first_face(self):
        """solves the corners on the first face without undoing the first cross"""
        raise NotImplementedError

    @abstractmethod
    def solve_middle_layer(self):
        """solves the M layer without undoing the first face"""
        raise NotImplementedError

    @abstractmethod
    def make_cross_in_up_face(self):
        """returns the cube with the U face with a cross of the correct color
        on the U face without undoing the first two layers"""
        raise NotImplementedError

    @abstractmethod
    def permutate_corners_in_up_face(self):
        """returns the cube with the corners in their correct position without
        undoing the cross in up face and without undoing the first two layers"""
        raise NotImplementedError

    @abstractmethod
    def orient_corners_in_up_face(self):
        """returns the cube with the corners in their correct orientation and
        with a cross of the correct color on the U face without undoing the
         first two layers"""
        raise NotImplementedError

    @abstractmethod
    def permutate_edges_in_up_face(self):
        """returns the solved cube"""
        raise NotImplementedError


# face colors
#                  ──────── ┌──┬──┬──┐
#                /        /││  │  │  │
#               /   0    / │├──┼──┼──┤
#              /        /  ││  │4 │  │
# ┌──┬──┬──┐  ┌──┬──┬──┐   │├──┼──┼──┤
# │  │  │  │  │  │  │  │ 3 ││  │  │  │
# ├──┼──┼──┤  ├──┼──┼──┤   │└──┴──┴──┘
# │  │1 │  │  │  │2 │  │  /
# ├──┼──┼──┤  ├──┼──┼──┤ /
# │  │  │  │  │  │  │  │/
# └──┴──┴──┘  └──┴──┴──┘
#             ┌──┬──┬──┐
#             │  │  │  │
#             ├──┼──┼──┤
#             │  │5 │  │
#             ├──┼──┼──┤
#             │  │  │  │
#
class Color(Enum):
    """The colors present on each face of a Rubik's cube"""

    UP = "U"
    LEFT = "L"
    FRONT = "F"
    RIGHT = "R"
    BACK = "B"
    DOWN = "D"


COLOR_VALUE_TO_COLOR_NAME = {c.value: c for c in Color}


def is_number_of_colors_correct(facelets):
    color_count = [facelets.count(c.value) for c in Color]
    return all(count == 9 for count in color_count)
