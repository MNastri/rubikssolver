from rubikssolver import (
    cubies_cube,
    edges,
)

EDGE_BUFFER = edges.Edge.UR
SETUP_EDGE = edges.Edge.UL


def edge_in_buffer(cube: str):
    cc = cubies_cube.CubieCube().from_string(cube)
    buffer = cc.edges_permutation[EDGE_BUFFER], cc.edges_orientation[EDGE_BUFFER]
    return buffer


# def where_is_the_first_piece(cube: str):
#     edge_to_find = edges.Edge(4)
#     cc = cubies_cube.CubieCube().from_string(cube)
#     position = cc.edges_permutation.index(edge_to_find)
#     return position
#
#
# if __name__ == "__main__":
#     cube_str = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
#     initial_position = where_is_the_first_piece(cube_str)
#     edge_in_up_layer = raise_to_up_layer(initial_position)
#     edge_above_its_destination = rotate_to_destination(edge_in_up_layer)
#     place_edge_in_destination(edge_above_its_destination)
#     print(pos)
#
#
# def where_are_the_pieces(cube: str):
#     edges_to_find = [edges.Edge(val) for val in range(4, 8)]
#     print(edges_to_find)
#     cc = cubies_cube.CubieCube().from_string(cube)
#     print(cc.edges_permutation)
#     print(cc.edges_permutation.permutated_to_UR)
#     print([edge for edge in cc.edges_permutation])
#
#
# if __name__ == "__main__":
#     cube_str = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
#     where_are_the_pieces(cube_str)
