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

    @classmethod
    def is_number_of_colors_correct(cls, facelets):
        colors = list(map(cls.get_color_from, facelets))
        color_count = [colors.count(cc) for cc in Color]
        return all(count == 9 for count in color_count)

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
