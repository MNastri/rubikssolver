from rubikssolver.colors import (
    Color,
    FACELETS_PER_COLOR,
)
from rubikssolver.facelets import (
    FACELETS_PER_FACE,
    NUMBER_OF_FACELETS,
)


class FaceletsCube:
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
        return self

    def _has_all_the_colors(self, facelets):
        unique_count = [facelets.count(col) for col in Color]
        return all(count == FACELETS_PER_COLOR for count in unique_count)


if __name__ == "__main__":
    print(FaceletsCube())
    print(FaceletsCube().facelets)
    # TODO test these two strings everywhere ↓
    # cube_str = "DUUBULDBFRULBLUFDUBRDFFFBLURBFRRULLLRRBLBDUDLRDBFDFDRF"  # OLD STRING WHEN IT WAS U→L→F→R→B→D. NEEDS TESTING
    cube_str = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"  # NEW STRING. NEEDS TESTING
    test_string_cube = FaceletsCube().from_string(cube_str)
    print(test_string_cube)
