from rubikssolver.edges import (
    Edge,
    SingleEdgeOrientation,
)
from rubikssolver.first_stage_moves import (
    EDGE_BUFFER,
    FirstStageSolver,
    SETUP_EDGE,
)


def test_edge_buffer_is_ur():
    assert EDGE_BUFFER == Edge.UR


def test_setup_edge_is_ul():
    assert SETUP_EDGE == Edge.UL


def test_buffer_is_ul_edge_with_normal_orienation():
    one_edge_to_go = "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
    cube = FirstStageSolver().from_string(one_edge_to_go)
    assert cube.edge_in_buffer() == (Edge.UL, SingleEdgeOrientation.normal)


def test_buffer_is_ul_edge_with_fliped_orienation():
    one_edge_to_go = "UUURULUUUBUFRRRRRRFFRFFFFFFDDDDDDDDDLULLLLLLLRBBBBBBBB"
    cube = FirstStageSolver().from_string(one_edge_to_go)
    assert cube.edge_in_buffer() == (Edge.UL, SingleEdgeOrientation.fliped)


def test_buffer_is_uf_edge_with_normal_orienation():
    u_prime_move = "UUUUUUUUUFFFRRRRRRLLLFFFFFFDDDDDDDDDBBBLLLLLLRRRBBBBBB"
    cube = FirstStageSolver().from_string(u_prime_move)
    assert cube.edge_in_buffer() == (Edge.UF, SingleEdgeOrientation.normal)
