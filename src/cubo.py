from enum import Enum
import timing


class Color(Enum):
    YELLOW = 0
    GREEN = 1
    ORANGE = 2
    BLUE = 3
    RED = 4
    WHITE = 5

# cublet face position (id)
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

# cube face colors
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
class RubiksCube:
    # 54 cublet face positions
    pos = "".join([str(c.value) * 9 for c in Color])  # Solved cube

    def __repr__(self):
        return self.pos

    def _transform(self, destination):
        # Receives a list of destination for all the cublet face positions (ids) and
        # makes the corresponding move in the cube
        # Upper face clockwise turn example:
        # ID:   0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11...18,19,20...27,28,29...36,37,38...
        # Dest: 2, 5, 8, 3, 4, 7, 0, 3, 6,18,19,20...29,28,27...36,37,38... 9,10,11...
        assert len(destination) == 54  # TODO remove
        _pos_copy = list(self.pos)
        for idx, dest in enumerate(destination):
            _pos_copy[dest] = self.pos[idx]
            # print(f"[{idx:02}]=",self.pos[idx], "→", f"[{dest:02}]")
        # print("".join(_pos_copy))
        self.pos = "".join(_pos_copy)

    def upper_layer_clockwise_turn(self):
        # >>> from src.cubo import RubiksCube
        # >>> my_cube = RubiksCube()
        # >>> print(my_cube)
        # 000000000111111111222222222333333333444444444555555555
        # >>> my_cube.upper_layer_clockwise_turn()
        # >>> print(my_cube)
        # 000000000444111111111222222222333333333444444555555555
        self._transform(
            [ 2,  5,  8,  3,  4,  7,  0,  3,  6,
             36, 37, 38, 12, 13, 14, 15, 16, 17,
              9, 10, 11, 21, 22, 23, 24, 25, 26,
             18, 19, 20, 30, 31, 32, 33, 34, 35,
             27, 28, 29, 39, 40, 41, 42, 43, 44,
             45, 46, 47, 48, 49, 50, 51, 52, 53, ]
        )
    def upper_layer_anticlockwise_turn(self):
        # TODO
        #  self._transform(
        #      [ 6,  3,  0,  7,  4,  1,  8,  5,  2,
        #       36, 37, 38, 12, 13, 14, 15, 16, 17,
        #        9, 10, 11, 21, 22, 23, 24, 25, 26,
        #       18, 19, 20, 30, 31, 32, 33, 34, 35,
        #       27, 28, 29, 39, 40, 41, 42, 43, 44,
        #       45, 46, 47, 48, 49, 50, 51, 52, 53, ]
        #  )
        self.upper_layer_clockwise_turn()
        self.upper_layer_clockwise_turn()
        self.upper_layer_clockwise_turn()

    def r_move(self):
        pass

    def r_prime_move(self):
        pass

if __name__ == "__main__":
    my_cube = RubiksCube()
    print(my_cube)
    my_cube.upper_layer_clockwise_turn()
    print(my_cube)
    my_cube.upper_layer_anticlockwise_turn()
    print(my_cube)
    my_cube.upper_layer_anticlockwise_turn()
    print(my_cube)


