from colors import Color
from facelets import (
    FACELETS_PER_FACE,
    NUMBER_OF_FACELETS,
)
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

    def from_string(self, s):
        assert len(s) == NUMBER_OF_FACELETS
        positions = range(NUMBER_OF_FACELETS)
        facelets = []
        for pos in positions:
            col = get_color_from(character=s[pos])
            facelets += (col,)
        self.facelets = facelets


def get_color_from(character: str):
    character = character.upper()
    assert character in Color.__dict__
    return Color.__getattr__(character)


if __name__ == "__main__":
    print(FaceletsRubiksCube())
    print(FaceletsRubiksCube().facelets)
    cube_str = "DUUBULDBFRULBLUFDUBRDFFFBLURBFRRULLLRRBLBDUDLRDBFDFDRF"
    test_string_cube = FaceletsRubiksCube()
    test_string_cube.from_string(cube_str)
    print(test_string_cube)
