from rubikssolver.corners import Corner as Co
from rubikssolver.corners import SingleCornerOrientation as CorOri
from rubikssolver.cubies_cube import CubieCube
from rubikssolver.edges import Edge as Ed
from rubikssolver.edges import SingleEdgeOrientation as EdgOri


class ETurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.URF, Co.UFL, Co.ULB, Co.UBR,
            Co.DFR, Co.DLF, Co.DBL, Co.DRB
        ]
        corner_orientation = [
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UR, Ed.UF, Ed.UL, Ed.UB,
            Ed.DR, Ed.DF, Ed.DL, Ed.DB,
            Ed.FL, Ed.BL, Ed.BR, Ed.FR
        ]
        edge_orientation = [
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.fliped, EdgOri.fliped, EdgOri.fliped, EdgOri.fliped,
        ]
        super().__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class MTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.URF, Co.UFL, Co.ULB, Co.UBR,
            Co.DFR, Co.DLF, Co.DBL, Co.DRB
        ]
        corner_orientation = [
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UR, Ed.UB, Ed.UL, Ed.DB,
            Ed.DR, Ed.UF, Ed.DL, Ed.DF,
            Ed.FR, Ed.FL, Ed.BL, Ed.BR
        ]
        edge_orientation = [
            EdgOri.normal, EdgOri.fliped, EdgOri.normal, EdgOri.fliped,
            EdgOri.normal, EdgOri.fliped, EdgOri.normal, EdgOri.fliped,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ]
        super().__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class STurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.URF, Co.UFL, Co.ULB, Co.UBR,
            Co.DFR, Co.DLF, Co.DBL, Co.DRB
        ]
        corner_orientation = [
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UL, Ed.UF, Ed.DL, Ed.UB,
            Ed.UR, Ed.DF, Ed.DR, Ed.DB,
            Ed.FR, Ed.FL, Ed.BL, Ed.BR
        ]
        edge_orientation = [
            EdgOri.fliped, EdgOri.normal, EdgOri.fliped, EdgOri.normal,
            EdgOri.fliped, EdgOri.normal, EdgOri.fliped, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ]
        super().__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )
