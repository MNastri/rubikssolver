from typing import List

from rubikssolver.move import Move
from rubikssolver.moves_definition import MOVES
from rubikssolver.puzzle_interface import Puzzle


class Moves(List):
    def __str__(self):
        to_string = [str(move.name) for move in self]
        return " ".join(to_string)

    @classmethod
    def create_moves_from(cls, s):
        moves_names = s.split()
        moves_to_initialize = (Move.__getitem__(mv) for mv in moves_names)
        return cls(moves_to_initialize)


def make_algorithm_from(moves_list):  # todo rename make cube from
    cube = Puzzle()
    for mv in moves_list:
        cube * MOVES[mv]
    return cube
