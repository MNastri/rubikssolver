from interface import RubiksCube


def solve_rubiks_cube(cube: RubiksCube):
    cube.solve_first_cross()
    cube.solve_first_face()
    cube.solve_middle_layer()
    cube.make_cross_in_up_face()
    cube.permutate_corners_in_up_face()
    cube.orient_corners_in_up_face()
    cube.permutate_edges_in_up_face()


if __name__ == "__main__":
    cube_string = "DUUBULDBFRULBLUFDUBRDFFFBLURBFRRULLLRRBLBDUDLRDBFDFDRF"
    cube = RubiksCube(cube_string)
    solve_rubiks_cube(cube=cube)
