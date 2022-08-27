from rubikssolver.edges import (
    Edge,
    SingleEdgeOrientation,
)
from rubikssolver.first_stage_solver import (
    EDGE_BUFFER,
    edge_in_buffer,
    SETUP_EDGE,
)


def test_edge_buffer_is_ur():
    assert EDGE_BUFFER == Edge.UR


def test_setup_edge_is_ul():
    assert SETUP_EDGE == Edge.UL


def test_buffer_is_ul_edge_with_normal_orienation():
    one_edge_to_go = "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
    assert edge_in_buffer(one_edge_to_go) == (Edge.UL, SingleEdgeOrientation.normal)


def test_buffer_is_ul_edge_with_fliped_orienation():
    one_edge_to_go = "UUURULUUUBUFRRRRRRFFRFFFFFFDDDDDDDDDLULLLLLLLRBBBBBBBB"
    assert edge_in_buffer(one_edge_to_go) == (Edge.UL, SingleEdgeOrientation.fliped)


def test_buffer_is_uf_edge_with_normal_orienation():
    u_prime_move = "UUUUUUUUUFFFRRRRRRLLLFFFFFFDDDDDDDDDBBBLLLLLLRRRBBBBBB"
    assert edge_in_buffer(u_prime_move) == (Edge.UF, SingleEdgeOrientation.normal)
