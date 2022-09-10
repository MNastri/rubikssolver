from rubikssolver import moves


def test_moves_string():
    moves_to_convert = (moves.Move.U1, moves.Move.R2, moves.Move.F3)
    moves_list = moves.Moves(moves_to_convert)
    assert str(moves_list) == "U1 R2 F3"


def test_create_moves_from_string():
    moves_string = "U1 R2 F3"
    moves_list = moves.Moves.create_moves_from(moves_string)
    assert moves_list == [moves.Move.U1, moves.Move.R2, moves.Move.F3]
