from rubikssolver import colors


def test_number_of_facelets_per_color_is_9():
    assert colors.FACELETS_PER_COLOR == 9


def test_number_of_colors_is_6():
    assert len(colors.Color) == 6


class TestColorMethod:
    def test_get_color_U(self):
        assert colors.Color.get_color_from(character="U") == colors.Color.U

    def test_get_color_R(self):
        assert colors.Color.get_color_from(character="R") == colors.Color.R

    def test_get_color_F(self):
        assert colors.Color.get_color_from(character="F") == colors.Color.F

    def test_get_color_D(self):
        assert colors.Color.get_color_from(character="D") == colors.Color.D

    def test_get_color_L(self):
        assert colors.Color.get_color_from(character="L") == colors.Color.L

    def test_get_color_B(self):
        assert colors.Color.get_color_from(character="B") == colors.Color.B
