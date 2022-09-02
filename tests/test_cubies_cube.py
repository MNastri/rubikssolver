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


class TestAreAllEdgesSolvedMethod:
    def test_all_edges_are_solved(self):
        cube = cubies_cube.CubieCube()
        assert cube.are_all_edges_solved() is True

    def test_one_edge_to_go(self):
        one_edge_to_go = cubies_cube.CubieCube().from_string(
            "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
        )
        assert one_edge_to_go.are_all_edges_solved() is False
