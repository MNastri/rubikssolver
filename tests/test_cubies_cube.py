from rubikssolver import (
    cubies_cube,
    face_turns,
)


class TestToString:
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
