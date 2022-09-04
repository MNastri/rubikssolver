from rubikssolver.edges import (
    Edge,
    SingleEdgeOrientation,
)
from rubikssolver.first_stage_solver import (
    EDGE_BUFFER,
    FirstStageSolver,
    SETUP_EDGE,
)
from rubikssolver.moves import Move


def test_edge_buffer_defined_as_ur():
    assert EDGE_BUFFER == Edge.UR


def test_setup_edge_defined_as_ul():
    assert SETUP_EDGE == Edge.UL


class TestEdgeInBuffer:
    def test_buffer_edge_is_ul_with_normal_orienation(self):
        one_edge_to_go = "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
        cube = FirstStageSolver().from_string(one_edge_to_go)
        assert cube.edge_in_buffer() == (Edge.UL, SingleEdgeOrientation.normal)

    def test_buffer_edge_is_ul_with_fliped_orienation(self):
        one_edge_to_go = "UUURULUUUBUFRRRRRRFFRFFFFFFDDDDDDDDDLULLLLLLLRBBBBBBBB"
        cube = FirstStageSolver().from_string(one_edge_to_go)
        assert cube.edge_in_buffer() == (Edge.UL, SingleEdgeOrientation.fliped)

    def test_buffer_edge_is_uf_with_normal_orienation(self):
        u_prime_move = "UUUUUUUUUFFFRRRRRRLLLFFFFFFDDDDDDDDDBBBLLLLLLRRRBBBBBB"
        cube = FirstStageSolver().from_string(u_prime_move)
        assert cube.edge_in_buffer() == (Edge.UF, SingleEdgeOrientation.normal)


class TestIsBufferEdgeCorrectMethod:
    def test_ul_normal_orientation_in_buffer(self):
        cube = FirstStageSolver()
        edge = Edge.UL
        orientation = SingleEdgeOrientation.normal
        assert cube._is_buffer_edge_correct(edge, orientation) is True


class TestFindSetupMoveMethod:
    def test_buffer_has_dr_normal_oriented_then_setup_is_d2l2(self):
        cube = FirstStageSolver().from_string(
            "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
        )
        edge = Edge.DR
        orientation = SingleEdgeOrientation.normal
        assert cube.find_setup_moves(edge, orientation) == [Move.D2, Move.L2]
