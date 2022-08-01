from facelets_rubiks_cube import FaceletsRubiksCube
from interface import solve_rubiks_cube


def solve_cube_string(cube_string):
    cube = FaceletsRubiksCube(cube_string)
    solve_rubiks_cube(cube)


if __name__ == "__main__":
    cube_str = "DUUBULDBFRULBLUFDUBRDFFFBLURBFRRULLLRRBLBDUDLRDBFDFDRF"
    solve_cube_string(cube_str)
