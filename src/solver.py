from facelets_rubiks_cube import FaceletsRubiksCube


def solve_first_cross(cube: FaceletsRubiksCube):
    edges_to_solve = ["DB", "DR", "DF", "DL"]
    print(edges_to_solve)
    print()
    edge_locations = [cube.find_location_of_edge(edge) for edge in edges_to_solve]
    print(edge_locations)
    print()
    edges = cube.edges
    print(edges)
    print()
    for edge in edges_to_solve:
        print(cube.find_location_of_edge(edge))
        print()
        # find where the facelet is
        # bring facelet to up layer without scrambling the down layer
        # bring it above its position
        # place it correctly


def solve_cube(cube: FaceletsRubiksCube):
    solve_first_cross(cube)
    # solve_first_face(cube)
    # solve_middle_layer(cube)
    # make_cross_in_up_face(cube)
    # permutate_corners_in_up_face(cube)
    # orient_corners_in_up_face(cube)
    # permutate_edges_in_up_face(cube)


if __name__ == "__main__":
    cube_string = "DUUBULDBFRULBLUFDUBRDFFFBLURBFRRULLLRRBLBDUDLRDBFDFDRF"
    cube = FaceletsRubiksCube(cube_string)
    solve_cube(cube)
