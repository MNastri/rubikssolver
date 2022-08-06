from abc import ABC
from typing import List


class CubeTransformation(ABC):
    def __init__(
        self,
        corner_permutation: List = None,
        corner_orientation: List = None,
        edge_permutation: List = None,
        edge_orientation: List = None,
    ):
        if not all([corner_permutation, corner_orientation, edge_permutation, edge_orientation]):
            raise AttributeError
        # TODO check for other errors? it currently only checks if they are not None
        self.corner_permutation = corner_permutation
        self.corner_orientation = corner_orientation
        self.edge_permutation = edge_permutation
        self.edge_orientation = edge_orientation
