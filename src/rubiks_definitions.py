from colors import Color
from facelets import Facelet as Fac

CORNER_FACELETS = [
    [Fac.U_8_corner, Fac.R_0_corner, Fac.F_2_corner],
    [Fac.U_6_corner, Fac.F_0_corner, Fac.L_2_corner],
    [Fac.U_0_corner, Fac.L_0_corner, Fac.B_corner1],
    [Fac.U_2_corner, Fac.B_corner0, Fac.R_2_corner],
    [Fac.D_2_corner, Fac.F_8_corner, Fac.R_6_corner],
    [Fac.D_0_corner, Fac.L_8_corner, Fac.F_6_corner],
    [Fac.D_6_corner, Fac.B_corner3, Fac.L_6_corner],
    [Fac.D_8_corner, Fac.R_8_corner, Fac.B_corner2],
]
EDGE_FACELETS = [
    [Fac.U_5_edge, Fac.R_1_edge],
    [Fac.U_7_edge, Fac.F_1_edge],
    [Fac.U_3_edge, Fac.L_1_edge],
    [Fac.U_1_edge, Fac.B_edge0],
    [Fac.D_5_edge, Fac.R_7_edge],
    [Fac.D_7_edge, Fac.F_7_edge],
    [Fac.D_3_edge, Fac.L_7_edge],
    [Fac.D_1_edge, Fac.B_edge3],
    [Fac.F_5_edge, Fac.R_3_edge],
    [Fac.F_3_edge, Fac.L_5_edge],
    [Fac.B_edge2, Fac.L_3_edge],
    [Fac.B_edge1, Fac.R_5_edge],
]
CORNER_COLORS = [
    [Color.U, Color.R, Color.F],
    [Color.U, Color.F, Color.L],
    [Color.U, Color.L, Color.B],
    [Color.U, Color.B, Color.R],
    [Color.D, Color.F, Color.R],
    [Color.D, Color.L, Color.F],
    [Color.D, Color.B, Color.L],
    [Color.D, Color.R, Color.B],
]
EDGE_COLORS = [
    [Color.U, Color.R],
    [Color.U, Color.F],
    [Color.U, Color.L],
    [Color.U, Color.B],
    [Color.D, Color.R],
    [Color.D, Color.F],
    [Color.D, Color.L],
    [Color.D, Color.B],
    [Color.F, Color.R],
    [Color.F, Color.L],
    [Color.B, Color.L],
    [Color.B, Color.R],
]
