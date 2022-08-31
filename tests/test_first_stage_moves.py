from rubikssolver.edges import (
    Edge,
    SingleEdgeOrientation,
)
from rubikssolver.first_stage_moves import Puzzle


class TestIsBufferEdgeCorrectMethod:
    def test_solved_puzzle(self):
        puzzle = Puzzle()
        edge = Edge.UL
        orientation = SingleEdgeOrientation.normal
        assert puzzle._is_buffer_edge_correct(edge, orientation) == True


# class TestFindSetupMoveMethod:
#     def test_buffer_has_dr_normal_oriented_then_setup_is_d2l2(self):
#         edge = Edge.DR
#         orientation = SingleEdgeOrientation.normal
#         assert find_setup_moves(edge, orientation) == "D2L2"
