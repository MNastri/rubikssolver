from abc import ABC
from typing import List


class CubeTransformation(ABC):
    def __init__(
        self,
        corners_permutation: List = None,
        corners_orientation: List = None,
        edges_permutation: List = None,
        edges_orientation: List = None,
    ):
        if not all([corners_permutation, corners_orientation, edges_permutation, edges_orientation]):
            raise AttributeError
        # TODO check for other errors? it currently only checks if they are not None
        self.corner_permutation = corners_permutation
        self.corner_orientation = corners_orientation
        self.edge_permutation = edges_permutation
        self.edge_orientation = edges_orientation
