from rubikssolver import colors


def test_number_of_facelets_per_color():
    assert colors.FACELETS_PER_COLOR == 9


def test_number_of_colors():
    assert len(colors.Color) == 6


class TestColorMethod:
    def test_U(self):
        assert colors.Color.get_color_from(character="U") == colors.Color.U

    def test_R(self):
        assert colors.Color.get_color_from(character="R") == colors.Color.R

    def test_F(self):
        assert colors.Color.get_color_from(character="F") == colors.Color.F

    def test_D(self):
        assert colors.Color.get_color_from(character="D") == colors.Color.D

    def test_L(self):
        assert colors.Color.get_color_from(character="L") == colors.Color.L

    def test_B(self):
        assert colors.Color.get_color_from(character="B") == colors.Color.B
