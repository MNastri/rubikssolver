from abc import ABC, abstractmethod


class RubiksCube(ABC):
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
