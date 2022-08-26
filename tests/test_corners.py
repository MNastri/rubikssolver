from enum import Enum

from rubikssolver import corners


def test_number_of_corner_orientations_is_3():
    assert corners.NUMBER_OF_CORNER_ORIENTATIONS == 3


def test_number_of_corners_is_8():
    assert corners.NUMBER_OF_CORNERS == 8


class TestCorner:
    def test_class_is_int(self):
        assert issubclass(corners.Corner, int)

    def test_class_is_enum(self):
        assert issubclass(corners.Corner, Enum)


class TestGetCornerFromMethod:
    def test_get_corner_urf(self):
        assert corners.Corner.get_corner_from(name="URF") == corners.Corner.URF

    def test_get_corner_ufl(self):
        assert corners.Corner.get_corner_from(name="UFL") == corners.Corner.UFL

    def test_get_corner_ulb(self):
        assert corners.Corner.get_corner_from(name="ULB") == corners.Corner.ULB

    def test_get_corner_ubr(self):
        assert corners.Corner.get_corner_from(name="UBR") == corners.Corner.UBR

    def test_get_corner_dfr(self):
        assert corners.Corner.get_corner_from(name="DFR") == corners.Corner.DFR

    def test_get_corner_dlf(self):
        assert corners.Corner.get_corner_from(name="DLF") == corners.Corner.DLF

    def test_get_corner_dbl(self):
        assert corners.Corner.get_corner_from(name="DBL") == corners.Corner.DBL

    def test_get_corner_drb(self):
        assert corners.Corner.get_corner_from(name="DRB") == corners.Corner.DRB

    def test_uppercase_corner_name_works(self):
        assert corners.Corner.get_corner_from(name="URF") == corners.Corner.URF

    def test_lowercase_corner_name_works(self):
        assert corners.Corner.get_corner_from(name="urf") == corners.Corner.URF

    def test_mixedcase_corner_name_works(self):
        assert corners.Corner.get_corner_from(name="urF") == corners.Corner.URF


class TestSingleCornerOrientation:
    def test_class_is_int(self):
        assert issubclass(corners.SingleCornerOrientation, int)

    def test_class_is_enum(self):
        assert issubclass(corners.SingleCornerOrientation, Enum)


class TestGetCornerOrientationFromMethod:
    def test_get_corner_orientation_normal(self):
        assert (
            corners.SingleCornerOrientation.get_corner_orientation_from(name="normal")
            == corners.SingleCornerOrientation.normal
        )

    def test_get_corner_orientation_clockwised(self):
        assert (
            corners.SingleCornerOrientation.get_corner_orientation_from(
                name="clockwised"
            )
            == corners.SingleCornerOrientation.clockwised
        )

    def test_get_corner_orientation_anticlockwised(self):
        assert (
            corners.SingleCornerOrientation.get_corner_orientation_from(
                name="anticlockwised"
            )
            == corners.SingleCornerOrientation.anticlockwised
        )

    def test_uppercase_corner_orientation_name_works(self):
        assert (
            corners.SingleCornerOrientation.get_corner_orientation_from(name="NORMAL")
            == corners.SingleCornerOrientation.normal
        )

    def test_lowercase_corner_orientation_name_works(self):
        assert (
            corners.SingleCornerOrientation.get_corner_orientation_from(name="normal")
            == corners.SingleCornerOrientation.normal
        )

    def test_mixedcase_corner_orientation_name_works(self):
        assert (
            corners.SingleCornerOrientation.get_corner_orientation_from(name="NoRmAl")
            == corners.SingleCornerOrientation.normal
        )
