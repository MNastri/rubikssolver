from enum import Enum
from typing import List


# face colors
#                  ──────── ┌──┬──┬──┐
#                /        /││  │  │  │
#               /   0    / │├──┼──┼──┤
#              /        /  ││  │4 │  │
# ┌──┬──┬──┐  ┌──┬──┬──┐   │├──┼──┼──┤
# │  │  │  │  │  │  │  │ 3 ││  │  │  │
# ├──┼──┼──┤  ├──┼──┼──┤   │└──┴──┴──┘
# │  │1 │  │  │  │2 │  │  /
# ├──┼──┼──┤  ├──┼──┼──┤ /
# │  │  │  │  │  │  │  │/
# └──┴──┴──┘  └──┴──┴──┘
#             ┌──┬──┬──┐
#             │  │  │  │
#             ├──┼──┼──┤
#             │  │5 │  │
#             ├──┼──┼──┤
#             │  │  │  │
#             └──┴──┴──┘
class Color(Enum):
    YELLOW = 0
    GREEN = 1
    ORANGE = 2
    BLUE = 3
    RED = 4
    WHITE = 5


# facelet position (id)
#           ┌──┬──┬──┐
#           │0 │1 │2 │
#           ├──┼──┼──┤
#           │3 │4 │5 │
#           ├──┼──┼──┤
#           │6 │7 │8 │
#           └──┴──┴──┘
# ┌──┬──┬──┐┌──┬──┬──┐┌──┬──┬──┐┌──┬──┬──┐
# │9 │10│11││18│19│20││27│28│29││36│37│38│
# ├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤
# │12│13│14││21│22│23││30│31│32││39│40│41│
# ├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤
# │15│16│17││24│25│26││33│34│35││42│43│44│
# └──┴──┴──┘└──┴──┴──┘└──┴──┴──┘└──┴──┴──┘
#           ┌──┬──┬──┐
#           │45│46│47│
#           ├──┼──┼──┤
#           │48│49│50│
#           ├──┼──┼──┤
#           │51│52│53│
#           └──┴──┴──┘
class RubiksCube:
    # 54 facelet positions
    pos = "".join([str(c.value) * 9 for c in Color])  # Solved cube

    def __repr__(self):
        return self.pos

    def _transform(self, destination):
        """Receives a list of destination for all the facelets (ids) and makes the
        corresponding move on the cube
        Upper face clockwise turn example:
        ID:   0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11...18,19,20...27,28,29...36,37,38...
        Dest: 2, 5, 8, 3, 4, 7, 0, 3, 6,18,19,20...29,28,27...36,37,38... 9,10,11...
        """
        assert len(destination) == 54  # TODO remove
        assert len(set(destination)) == len(destination)  # TODO remove
        _pos_copy = list(self.pos)
        for idx, dest in enumerate(destination):
            _pos_copy[dest] = self.pos[idx]
            # print(f"[{idx:02}]=",self.pos[idx], "→", f"[{dest:02}]")
        # print("".join(_pos_copy))
        self.pos = "".join(_pos_copy)

    def upper_layer_clockwise_turn(self):
        """
        >>> from src.cubo import RubiksCube
        >>> my_cube = RubiksCube()
        >>> print(my_cube)
        000000000111111111222222222333333333444444444555555555
        >>> my_cube.upper_layer_clockwise_turn()
        >>> print(my_cube)
        000000000222111111333222222444333333111444444555555555
        """
        self._transform(
            [ 2,  5,  8,  1,  4,  7,  0,  3,  6,
             36, 37, 38, 12, 13, 14, 15, 16, 17,
              9, 10, 11, 21, 22, 23, 24, 25, 26,
             18, 19, 20, 30, 31, 32, 33, 34, 35,
             27, 28, 29, 39, 40, 41, 42, 43, 44,
             45, 46, 47, 48, 49, 50, 51, 52, 53, ]
        )


def unify_transforms(transforms: List[List[int]]) -> List[int]:
    """Unifies the received transformations in a single transformation.
    e.g.: three U turns is the same as one U' turn.
    usage:
    >>> from src.cubo import unify_transforms
    >>> my_transform = [1,2,0] +[i for i in range(3,54)] # three id cycle 0→1→2→0
    >>> result = unify_transforms([my_transform])
    >>> result
    [1, 2, 0, 3, 4, ..., 53]
    >>> unify_transforms([my_transform, my_transform])
    [2, 0, 1, 3, 4, ..., 53]
    >>> unify_transforms([my_transform, my_transform, my_transform])
    [0, 1, 2, 3, 4, ..., 53]
    """
    assert all(
        len(transform) == 54 for transform in transforms
    ), "length of transform must be 54"
    assert all(
        len(set(transform)) == len(transform) for transform in transforms
    ), "destination index in transform must be unique"
    facelets = {i: i for i in range(54)}
    # print(list(facelets.values()))
    for transform in transforms:
        new_facelets = {i: None for i in range(54)}
        for start_idx, end_idx in enumerate(transform):
            if start_idx == end_idx:
                new_facelets[start_idx] = end_idx
                continue
            for idx, current_position in facelets.items():
                if start_idx == current_position:
                    new_facelets[idx] = end_idx
                    break
        facelets = new_facelets
        # print(list(facelets.values()))
    return list(facelets.values())


def test_u_turns():
    u_turn = [
         2,  5,  8,  1,  4,  7,  0,  3,  6,
        36, 37, 38, 12, 13, 14, 15, 16, 17,
         9, 10, 11, 21, 22, 23, 24, 25, 26,
        18, 19, 20, 30, 31, 32, 33, 34, 35,
        27, 28, 29, 39, 40, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50, 51, 52, 53,
    ]
    print(f"{u_turn=}")
    u2_turn = unify_transforms([u_turn, u_turn])
    print(f"{u2_turn=}")
    u_prime_turn_from_u = unify_transforms([u_turn, u_turn, u_turn])
    print(f"{u_prime_turn_from_u=}")
    u_prime_turn_from_u2 = unify_transforms([u2_turn, u_turn])
    print(f"{u_prime_turn_from_u2=}")
    assert(u_prime_turn_from_u2 == u_prime_turn_from_u)


if __name__ == "__main__":
    test_u_turns()
