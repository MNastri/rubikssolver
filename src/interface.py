from abc import (
    ABC,
    abstractmethod,
)


class RubiksCube(ABC):
    # TODO verificar se @abstractmethod pode ser usado com __init__
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


def solve_rubiks_cube(cube: RubiksCube):
    cube.solve_first_cross()
    cube.solve_first_face()
    cube.solve_middle_layer()
    cube.make_cross_in_up_face()
    cube.permutate_corners_in_up_face()
    cube.orient_corners_in_up_face()
    cube.permutate_edges_in_up_face()
