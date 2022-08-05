from colors import Color
from facelets import Facelet as Fac

CORNER_FACELETS = [
    [Fac.U_corner3, Fac.R_corner0, Fac.F_corner1],
    [Fac.U_corner2, Fac.F_corner0, Fac.L_corner1],
    [Fac.U_corner0, Fac.L_corner0, Fac.B_corner1],
    [Fac.U_corner1, Fac.B_corner0, Fac.R_corner1],
    [Fac.D_corner1, Fac.F_corner3, Fac.R_corner2],
    [Fac.D_corner0, Fac.L_corner3, Fac.F_corner2],
    [Fac.D_corner2, Fac.B_corner3, Fac.L_corner2],
    [Fac.D_corner3, Fac.R_corner3, Fac.B_corner2],
]
EDGE_FACELETS = [
    [Fac.U_edge2, Fac.R_edge0],
    [Fac.U_edge3, Fac.F_edge0],
    [Fac.U_edge1, Fac.L_edge0],
    [Fac.U_edge0, Fac.B_edge0],
    [Fac.D_edge2, Fac.R_edge3],
    [Fac.D_edge3, Fac.F_edge3],
    [Fac.D_edge1, Fac.L_edge3],
    [Fac.D_edge0, Fac.B_edge3],
    [Fac.F_edge2, Fac.R_edge1],
    [Fac.F_edge1, Fac.L_edge2],
    [Fac.B_edge2, Fac.L_edge1],
    [Fac.B_edge1, Fac.R_edge2],
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
