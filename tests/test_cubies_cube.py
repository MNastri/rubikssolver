from rubikssolver import (
    cubies_cube,
    face_turns,
)


class TestToStringMethod:
    solved_cube = cubies_cube.CubieCube()

    def test_solved_cube(self):
        assert (
            str(self.solved_cube)
            == "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        )

    def test_u_turn(self):
        assert (
            str(face_turns.UTurn())
            == "UUUUUUUUUBBBRRRRRRRRRFFFFFFDDDDDDDDDFFFLLLLLLLLLBBBBBB"
        )

    def test_r_turn(self):
        assert (
            str(face_turns.RTurn())
            == "UUFUUFUUFRRRRRRRRRFFDFFDFFDDDBDDBDDBLLLLLLLLLUBBUBBUBB"
        )

    def test_f_turn(self):
        assert (
            str(face_turns.FTurn())
            == "UUUUUULLLURRURRURRFFFFFFFFFRRRDDDDDDLLDLLDLLDBBBBBBBBB"
        )

    def test_d_turn(self):
        assert (
            str(face_turns.DTurn())
            == "UUUUUUUUURRRRRRFFFFFFFFFLLLDDDDDDDDDLLLLLLBBBBBBBBBRRR"
        )

    def test_l_turn(self):
        assert (
            str(face_turns.LTurn())
            == "BUUBUUBUURRRRRRRRRUFFUFFUFFFDDFDDFDDLLLLLLLLLBBDBBDBBD"
        )

    def test_b_turn(self):
        assert (
            str(face_turns.BTurn())
            == "RRRUUUUUURRDRRDRRDFFFFFFFFFDDDDDDLLLULLULLULLBBBBBBBBB"
        )
