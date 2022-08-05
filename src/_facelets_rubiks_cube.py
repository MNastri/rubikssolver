from colors import Color
from facelets import FACELETS_PER_FACE
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


if __name__ == "__main__":
    print(FaceletsRubiksCube().facelets)
