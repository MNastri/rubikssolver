def test_u_turns():
    from facelets_rubiks_cube import unify_transforms

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
    from facelets_rubiks_cube import FaceletsRubiksCube

    cube = FaceletsRubiksCube()
    print(cube)
    cube.upper_layer_clockwise_turn()
    print(cube)
    assert str(cube) == "UUUUUUUUUFFFLLLLLLRRRFFFFFFBBBRRRRRRLLLBBBBBBDDDDDDDDD"


if __name__ == "__main__":
    test_u_turns()
    test_transformation()
