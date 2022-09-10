import rubikssolver.move

from rubikssolver import moves


def test_moves_string():
    moves_to_convert = (
        rubikssolver.move.Move.U1,
        rubikssolver.move.Move.R2,
        rubikssolver.move.Move.F3,
    )
    moves_list = moves.Moves(moves_to_convert)
    assert str(moves_list) == "U1 R2 F3"


def test_create_moves_from_string():
    moves_string = "U1 R2 F3"
    moves_list = moves.Moves.create_moves_from(moves_string)
    assert moves_list == [
        rubikssolver.move.Move.U1,
        rubikssolver.move.Move.R2,
        rubikssolver.move.Move.F3,
    ]


def test_make_algorithm_from():
    algorithm_swap_two_edges = (
        rubikssolver.move.Move.R1,
        rubikssolver.move.Move.U1,
        rubikssolver.move.Move.R3,
        rubikssolver.move.Move.U3,
        rubikssolver.move.Move.R3,
        rubikssolver.move.Move.F1,
        rubikssolver.move.Move.R2,
        rubikssolver.move.Move.U3,
        rubikssolver.move.Move.R3,
        rubikssolver.move.Move.U3,
        rubikssolver.move.Move.R1,
        rubikssolver.move.Move.U1,
        rubikssolver.move.Move.R3,
        rubikssolver.move.Move.F3,
    )
    moves_list = moves.Moves(algorithm_swap_two_edges)
    one_edge_to_go = "UUUUUUUUUBLFRRRRRRFFRFFFFFFDDDDDDDDDLRLLLLLLLRBBBBBBBB"
    algo = moves.make_algorithm_from(moves_list)
    assert str(algo) == one_edge_to_go
