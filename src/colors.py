from enum import Enum

FACELETS_PER_COLOR = 9


class Color(Enum):
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5

    @classmethod
    def get_color_from(cls, character: str):
        character = character.upper()
        assert character in Color.__dict__
        return Color.__getattr__(character)

    #                  ──────── ┌──┬──┬──┐
    #                /        /││  │  │  │
    #               /   0    / │├──┼──┼──┤
    #              /        /  ││  │5 │  │
    # ┌──┬──┬──┐  ┌──┬──┬──┐   │├──┼──┼──┤
    # │  │  │  │  │  │  │  │ 1 ││  │  │  │
    # ├──┼──┼──┤  ├──┼──┼──┤   │└──┴──┴──┘
    # │  │4 │  │  │  │2 │  │  /
    # ├──┼──┼──┤  ├──┼──┼──┤ /
    # │  │  │  │  │  │  │  │/
    # └──┴──┴──┘  └──┴──┴──┘
    #             ┌──┬──┬──┐
    #             │  │  │  │
    #             ├──┼──┼──┤
    #             │  │3 │  │
    #             ├──┼──┼──┤
    #             │  │  │  │
    #             └──┴──┴──┘
