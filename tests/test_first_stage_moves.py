from rubikssolver.edges import (
    Edge,
    SingleEdgeOrientation,
)
from rubikssolver.first_stage_solver import FirstStageSolver
from rubikssolver.moves import Move


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
