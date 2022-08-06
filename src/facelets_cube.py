from colors import (
    Color,
    FACELETS_PER_COLOR,
)
from facelets import (
    FACELETS_PER_FACE,
    NUMBER_OF_FACELETS,
)
from interface import RubiksCube


class FaceletsCube(RubiksCube):
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
            col = Color.get_color_from(character=s[pos])
            facelets += (col,)
        assert self._has_all_the_colors(facelets)
        self.facelets = facelets

    def _has_all_the_colors(self, facelets):
        unique_count = [facelets.count(col) for col in Color]
        return all(count == FACELETS_PER_COLOR for count in unique_count)


if __name__ == "__main__":
    print(FaceletsCube())
    print(FaceletsCube().facelets)
    cube_str = "DUUBULDBFRULBLUFDUBRDFFFBLURBFRRULLLRRBLBDUDLRDBFDFDRF"
    test_string_cube = FaceletsCube()
    test_string_cube.from_string(cube_str)
    print(test_string_cube)
