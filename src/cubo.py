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
    UP = "U"
    LEFT = "L"
    FRONT = "F"
    RIGHT = "R"
    BACK = "B"
    DOWN = "D"


# facelet position
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
    faces = [[face] * 9 for face in Color]  # Solved cube
    facelets = [cc for face in faces for cc in face]

    def __repr__(self):
        return str([fcl.value for fcl in self.facelets])

    def __str__(self):
        s = ""
        for idx in range(54):
            for color in Color:
                if self.facelets[idx] == color:
                    s += color.value
        return s

    def _transform(self, destination):
        """Receives a list of destination for all the facelets and makes the
        corresponding move on the cube.
        Upper face clockwise turn example:
        u_move =
           [  2,  5,  8,  1,  4,  7,  0,  3,  6,
             36, 37, 38, 12, 13, 14, 15, 16, 17,
              9, 10, 11, 21, 22, 23, 24, 25, 26,
             18, 19, 20, 30, 31, 32, 33, 34, 35,
             27, 28, 29, 39, 40, 41, 42, 43, 44,
             45, 46, 47, 48, 49, 50, 51, 52, 53, ]
        This represents the transformation that makes the facelet in position 0 go to
        position 2, the facelet in position 1 go to position 5, the facelet in 3 go to 8,
        etc.
        Start: 0,1,2,3,4,5,6,7,8, 9,10,11,12...17,18,19,20,21...26,27,28,29,30...35,36,37,38,39...53
        Dest:  2,5,8,1,4,7,0,3,6,36,37,38,12...17, 9,10,11,21...26,18,19,20,30...35,27,28,29,39...53
        """
        assert len(destination) == 54  # TODO remove
        assert len(set(destination)) == len(destination)  # TODO remove
        facelets_copy = self.facelets[:]
        for idx, dest in enumerate(destination):
            facelets_copy[dest] = self.facelets[idx]
            # print(f"[{idx:02}]=",self.pos[idx], "→", f"[{dest:02}]")
        # print("".join(facelets_copy))
        self.facelets = facelets_copy

    def upper_layer_clockwise_turn(self):
        """
        >>> from src.cubo import RubiksCube
        >>> my_cube = RubiksCube()
        >>> print(my_cube)
        UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD
        >>> my_cube.upper_layer_clockwise_turn()
        >>> print(my_cube)
        UUUUUUUUUFFFLLLLLLRRRFFFFFFBBBRRRRRRLLLBBBBBBDDDDDDDDD
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
    >>> my_transform = [1,2,0] +[ii for ii in range(3,54)] # three id cycle 0→1→2→0
    >>> unify_transforms([my_transform])
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
    ), "destination in transform must be unique"
    facelets = {ii: ii for ii in range(54)}
    # print(list(facelets.values()))
    for transform in transforms:
        new_facelets = {ii: None for ii in range(54)}
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
    assert u_prime_turn_from_u2 == u_prime_turn_from_u


def test_transformation():
    cube = RubiksCube()
    print(cube)
    cube.upper_layer_clockwise_turn()
    print(cube)
    assert str(cube) == "UUUUUUUUUFFFLLLLLLRRRFFFFFFBBBRRRRRRLLLBBBBBBDDDDDDDDD"


if __name__ == "__main__":
    test_transformation()
    test_u_turns()
    print(RubiksCube())
    print(str(RubiksCube()))
    print(repr(RubiksCube()))
    print(RubiksCube().facelets)
