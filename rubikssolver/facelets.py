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
    F_0_corner = 18
    F_1_edge = 19
    F_2_corner = 20
    F_3_edge = 21
    F_4_center = 22
    F_5_edge = 23
    F_6_corner = 24
    F_7_edge = 25
    F_8_corner = 26
    D_0_corner = 27
    D_1_edge = 28
    D_2_corner = 29
    D_3_edge = 30
    D_4_center = 31
    D_5_edge = 32
    D_6_corner = 33
    D_7_edge = 34
    D_8_corner = 35
    L_0_corner = 36
    L_1_edge = 37
    L_2_corner = 38
    L_3_edge = 39
    L_4_center = 40
    L_5_edge = 41
    L_6_corner = 42
    L_7_edge = 43
    L_8_corner = 44
    B_0_corner = 45
    B_1_edge = 46
    B_2_corner = 47
    B_3_edge = 48
    B_4_center = 49
    B_5_edge = 50
    B_6_corner = 51
    B_7_edge = 52
    B_8_corner = 53

    #           ┌──┬──┬──┐
    #           │U0│U1│U2│
    #           ├──┼──┼──┤
    #           │U3│U4│U5│
    #           ├──┼──┼──┤
    #           │U6│U7│U8│
    #           └──┴──┴──┘
    # ┌──┬──┬──┐┌──┬──┬──┐┌──┬──┬──┐┌──┬──┬──┐
    # │L0│L1│L2││F0│F1│F2││R0│R1│R2││B0│B1│B2│
    # ├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤
    # │L3│L4│L5││F3│F4│F5││R3│R4│R5││B3│B4│B5│
    # ├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤├──┼──┼──┤
    # │L6│L7│L8││F6│F7│F8││R6│R7│R8││B6│B7│B8│
    # └──┴──┴──┘└──┴──┴──┘└──┴──┴──┘└──┴──┴──┘
    #           ┌──┬──┬──┐
    #           │D0│D1│D2│
    #           ├──┼──┼──┤
    #           │D3│D4│D5│
    #           ├──┼──┼──┤
    #           │D6│D7│D8│
    #           └──┴──┴──┘

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
