from colors import Color
from facelets import FACELETS_PER_FACE, NUMBER_OF_FACELETS
from interface import RubiksCube


class FaceletsRubiksCube(RubiksCube):
    def __init__(self):
        self._store_solved_cube()

    def _store_solved_cube(self):
        facelets_range = range(FACELETS_PER_FACE)
        facelets = []
        for clr in Color:
            for _ in facelets_range:
                facelets += (clr,)
        self.facelets = facelets

    def __str__(self):
        ss = ""
        positions = range(NUMBER_OF_FACELETS)
        for pos in positions:
            ss += self.facelets[pos].name
        return ss


if __name__ == "__main__":
    print(FaceletsRubiksCube())
    print(FaceletsRubiksCube().facelets)
