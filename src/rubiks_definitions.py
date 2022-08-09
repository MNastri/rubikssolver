from colors import Color
from facelets import Facelet as Fac

CORNER_FACELETS = [
    [Fac.U_8_corner, Fac.R_0_corner, Fac.F_corner1],
    [Fac.U_6_corner, Fac.F_corner0, Fac.L_corner1],
    [Fac.U_0_corner, Fac.L_corner0, Fac.B_corner1],
    [Fac.U_2_corner, Fac.B_corner0, Fac.R_2_corner],
    [Fac.D_corner1, Fac.F_corner3, Fac.R_6_corner],
    [Fac.D_corner0, Fac.L_corner3, Fac.F_corner2],
    [Fac.D_corner2, Fac.B_corner3, Fac.L_corner2],
    [Fac.D_corner3, Fac.R_8_corner, Fac.B_corner2],
]
EDGE_FACELETS = [
    [Fac.U_5_edge, Fac.R_1_edge],
    [Fac.U_7_edge, Fac.F_edge0],
    [Fac.U_3_edge, Fac.L_edge0],
    [Fac.U_1_edge, Fac.B_edge0],
    [Fac.D_edge2, Fac.R_7_edge],
    [Fac.D_edge3, Fac.F_edge3],
    [Fac.D_edge1, Fac.L_edge3],
    [Fac.D_edge0, Fac.B_edge3],
    [Fac.F_edge2, Fac.R_3_edge],
    [Fac.F_edge1, Fac.L_edge2],
    [Fac.B_edge2, Fac.L_edge1],
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
