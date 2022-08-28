from rubikssolver import (
    cubies_cube,
    face_turns,
)


class TestToStringMethod:
    solved_cube = cubies_cube.CubieCube()

    def test_solved_cube(self):
        assert (
            self.solved_cube.to_string()
            == "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        )

    def test_u_turn(self):
        assert (
            face_turns.UTurn().to_string()
            == "UUUUUUUUUBBBRRRRRRRRRFFFFFFDDDDDDDDDFFFLLLLLLLLLBBBBBB"
        )

    def test_r_turn(self):
        assert (
            face_turns.RTurn().to_string()
            == "UUFUUFUUFRRRRRRRRRFFDFFDFFDDDBDDBDDBLLLLLLLLLUBBUBBUBB"
        )

    def test_f_turn(self):
        assert (
            face_turns.FTurn().to_string()
            == "UUUUUULLLURRURRURRFFFFFFFFFRRRDDDDDDLLDLLDLLDBBBBBBBBB"
        )

    def test_d_turn(self):
        assert (
            face_turns.DTurn().to_string()
            == "UUUUUUUUURRRRRRFFFFFFFFFLLLDDDDDDDDDLLLLLLBBBBBBBBBRRR"
        )

    def test_l_turn(self):
        assert (
            face_turns.LTurn().to_string()
            == "BUUBUUBUURRRRRRRRRUFFUFFUFFFDDFDDFDDLLLLLLLLLBBDBBDBBD"
        )

    def test_b_turn(self):
        assert (
            face_turns.BTurn().to_string()
            == "RRRUUUUUURRDRRDRRDFFFFFFFFFDDDDDDLLLULLULLULLBBBBBBBBB"
        )
