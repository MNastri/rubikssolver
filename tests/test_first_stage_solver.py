from rubikssolver import (
    edges,
    first_stage_solver,
)


def test_edge_buffer_is_ur():
    assert first_stage_solver.EDGE_BUFFER == edges.Edge.UR


def test_setup_edge_is_ul():
    assert first_stage_solver.SETUP_EDGE == edges.Edge.UL


def test_ul_edge_in_buffer():
    one_edge_to_go = "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
    assert first_stage_solver.edge_in_buffer(one_edge_to_go) == edges.Edge.UL
