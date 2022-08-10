from typing import List

from colors import Color
from facelets import NUMBER_OF_FACELETS


class FaceletsRubiksCube:
    def __init__(self, facelets=None):
        if facelets is None:
            self._store_solved_cube()
        else:
            self._check_facelets(facelets)
            self._store_color_names(facelets)

    def __repr__(self):
        return str([f.value for f in self.facelets])

    # def __str__(self):  # TODO
    #     s = ""
    #     for idx in range(NUMBER_OF_FACELETS):
    #         for c in Color:
    #             if self.facelets[idx] == c:
    #                 s += c.value
    #                 break
    #     return s

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
        position 2, the facelet in position 1 go to position 5, the facelet in 3 go to 8
        , etc.
        Start: 0,1,2,3,4,5,6,7,8, 9,10,11,12...17,18,19,20,21...26,27,28,29,30...35,36,
        37,38,39...53
        Dest:  2,5,8,1,4,7,0,3,6,36,37,38,12...17, 9,10,11,21...26,18,19,20,30...35,27,
        28,29,39...53
        """
        assert len(destination) == NUMBER_OF_FACELETS  # TODO remove
        assert len(set(destination)) == len(destination)  # TODO remove
        facelets_copy = self.facelets[:]
        for idx, dest in enumerate(destination):
            facelets_copy[dest] = self.facelets[idx]
            # print(f"[{idx:02}]=",self.pos[idx], "→", f"[{dest:02}]")
        # print("".join(facelets_copy))
        self.facelets = facelets_copy

    def upper_layer_clockwise_turn(self):
        """
        >>> from src.facelets_rubiks_cube import FaceletsRubiksCube
        >>> my_cube = FaceletsRubiksCube()
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

    def _check_facelets(self, facelets):
        if isinstance(facelets, (List, str)):
            assert len(facelets) == NUMBER_OF_FACELETS
            assert Color.is_number_of_colors_correct(facelets)
        else:
            allowed_types = [str, List, None]
            raise TypeError(f"facelets should be one of {allowed_types}")

    def _store_solved_cube(self):
        faces = [[face] * 9 for face in Color]
        self.facelets = [facelet for face in faces for facelet in face]

    def _store_color_names(self, facelets):
        self.facelets = [Color.get_color_from(ff) for ff in facelets]


def unify_transforms(transforms: List[List[int]]) -> List[int]:
    """Unifies the received transformations in a single transformation.
    e.g.: three U turns is the same as one U' turn.
    usage:
    >>> from src.facelets_rubiks_cube import unify_transforms
    >>> my_transform = [1, 2, 0] +[ii for ii in range(3, 54)] # three id cycle 0→1→2→0
    >>> unify_transforms([my_transform])
    [1, 2, 0, 3, 4, ..., 53]
    >>> unify_transforms([my_transform, my_transform])
    [2, 0, 1, 3, 4, ..., 53]
    >>> unify_transforms([my_transform, my_transform, my_transform])
    [0, 1, 2, 3, 4, ..., 53]
    """
    assert all(
        len(transform) == NUMBER_OF_FACELETS for transform in transforms
    ), f"length of transform must be {NUMBER_OF_FACELETS}"
    assert all(
        len(set(transform)) == len(transform) for transform in transforms
    ), "destination in transform must be unique"
    facelets = {ii: ii for ii in range(NUMBER_OF_FACELETS)}
    # print(list(facelets.values()))
    for transform in transforms:
        new_facelets = {ii: None for ii in range(NUMBER_OF_FACELETS)}
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


if __name__ == "__main__":
    print(FaceletsRubiksCube())
    print(str(FaceletsRubiksCube()))
    print(repr(FaceletsRubiksCube()))
    print(FaceletsRubiksCube().facelets)
    print(FaceletsRubiksCube("U" * 9 + "L" * 9 + "F" * 9 + "R" * 9 + "B" * 9 + "D" * 9))
    print(FaceletsRubiksCube(["U", "L", "F", "R", "B", "D"] * 9))
