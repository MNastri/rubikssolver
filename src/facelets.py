from enum import IntEnum

NUMBER_OF_FACELETS = 54
FACELETS_PER_FACE = 9


class Facelet(IntEnum):
    U_0_corner = 0
    U_1_edge = 1
    U_2_corner = 2
    U_3_edge = 3
    U_4_center = 4
    U_5_edge = 5
    U_6_corner = 6
    U_7_edge = 7
    U_8_corner = 8
    R_0_corner = 9
    R_1_edge = 10
    R_2_corner = 11
    R_3_edge = 12
    R_4_center = 13
    R_5_edge = 14
    R_6_corner = 15
    R_7_edge = 16
    R_8_corner = 17
    F_corner0 = 18
    F_edge0 = 19
    F_corner1 = 20
    F_edge1 = 21
    F = 22
    F_edge2 = 23
    F_corner2 = 24
    F_edge3 = 25
    F_corner3 = 26
    D_corner0 = 27
    D_edge0 = 28
    D_corner1 = 29
    D_edge1 = 30
    D = 31
    D_edge2 = 32
    D_corner2 = 33
    D_edge3 = 34
    D_corner3 = 35
    L_corner0 = 36
    L_edge0 = 37
    L_corner1 = 38
    L_edge1 = 39
    L = 40
    L_edge2 = 41
    L_corner2 = 42
    L_edge3 = 43
    L_corner3 = 44
    B_corner0 = 45
    B_edge0 = 46
    B_corner1 = 47
    B_edge1 = 48
    B = 49
    B_edge2 = 50
    B_corner2 = 51
    B_edge3 = 52
    B_corner3 = 53
    #           ┌──┬──┬──┐
    #           │0 │1 │2 │
    #           ├──┼──┼──┤
    #           │3 │4 │5 │
    #           ├──┼──┼──┤
    #           │6 │7 │8 │
    #           └──┴──┴──┘
    # ┌──┬──┬──┐┌──┬──┬──┐┌──┬──┬──┐┌──┬──┬──┐
    # │36│37│38││18│19│20││9 │10│11││45│46│47│
    # ├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤
    # │39│40│41││21│22│23││12│13│14││48│49│50│
    # ├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤
    # │42│43│44││24│25│26││15│16│17││51│52│53│
    # └──┴──┴──┘└──┴──┴──┘└──┴──┴──┘└──┴──┴──┘
    #           ┌──┬──┬──┐
    #           │27│28│29│
    #           ├──┼──┼──┤
    #           │30│31│32│
    #           ├──┼──┼──┤
    #           │33│34│35│
    #           └──┴──┴──┘
