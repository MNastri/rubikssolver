from corners import Corner as Co
from corners import CornersOrientation as CsO
from corners import CornersPermutation as CsP
from corners import SingleCornerOrientation as CorOri
from cube_transformations import CubeTransformation
from edges import Edge as Ed
from edges import EdgesOrientation as EsO
from edges import EdgesPermutation as EsP
from edges import SingleEdgeOrientation as EdgOri
from cubies_cube import CubieCube


class UTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.UBR, Co.URF, Co.UFL, Co.ULB,
            Co.DFR, Co.DLF, Co.DBL, Co.DRB
        ]
        corner_orientation = [
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UB, Ed.UR, Ed.UF, Ed.UL,
            Ed.DR, Ed.DF, Ed.DL, Ed.DB,
            Ed.FR, Ed.FL, Ed.BL, Ed.BR
        ]
        edge_orientation = [
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ]
        super().__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class RTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CsP([
            Co.DFR, Co.UFL, Co.ULB, Co.URF,
            Co.DRB, Co.DLF, Co.DBL, Co.UBR
        ])
        corner_orientation = CsO([
            CorOri.anticlockwised, CorOri.normal, CorOri.normal, CorOri.clockwised,
            CorOri.clockwised, CorOri.normal, CorOri.normal, CorOri.anticlockwised,
        ])
        edge_permutation = EsP([
            Ed.FR, Ed.UF, Ed.UL, Ed.UB,
            Ed.BR, Ed.DF, Ed.DL, Ed.DB,
            Ed.DR, Ed.FL, Ed.BL, Ed.UR
        ])
        edge_orientation = EsO([
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ])
        super(RTurn, self).__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class FTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CsP([
            Co.UFL, Co.DLF, Co.ULB, Co.UBR,
            Co.URF, Co.DFR, Co.DBL, Co.DRB
        ])
        corner_orientation = CsO([
            CorOri.clockwised, CorOri.anticlockwised, CorOri.normal, CorOri.normal,
            CorOri.anticlockwised, CorOri.clockwised, CorOri.normal, CorOri.normal,
        ])
        edge_permutation = EsP([
            Ed.UR, Ed.FL, Ed.UL, Ed.UB,
            Ed.DR, Ed.FR, Ed.DL, Ed.DB,
            Ed.UF, Ed.DF, Ed.BL, Ed.BR
        ])
        edge_orientation = EsO([
            EdgOri.normal, EdgOri.fliped, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.fliped, EdgOri.normal, EdgOri.normal,
            EdgOri.fliped, EdgOri.fliped, EdgOri.normal, EdgOri.normal,
        ])
        super(FTurn, self).__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class DTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CsP([
            Co.URF, Co.UFL, Co.ULB, Co.UBR,
            Co.DLF, Co.DBL, Co.DRB, Co.DFR
        ])
        corner_orientation = CsO([
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ])
        edge_permutation = EsP([
            Ed.UR, Ed.UF, Ed.UL, Ed.UB,
            Ed.DF, Ed.DL, Ed.DB, Ed.DR,
            Ed.FR, Ed.FL, Ed.BL, Ed.BR
        ])
        edge_orientation = EsO([
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ])
        super(DTurn, self).__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class LTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CsP([
            Co.URF, Co.ULB, Co.DBL, Co.UBR,
            Co.DFR, Co.UFL, Co.DLF, Co.DRB
        ])
        corner_orientation = CsO([
            CorOri.normal, CorOri.clockwised, CorOri.anticlockwised, CorOri.normal,
            CorOri.normal, CorOri.anticlockwised, CorOri.clockwised, CorOri.normal,
        ])
        edge_permutation = EsP([
            Ed.UR, Ed.UF, Ed.BL, Ed.UB,
            Ed.DR, Ed.DF, Ed.FL, Ed.DB,
            Ed.FR, Ed.UL, Ed.DL, Ed.BR
        ])
        edge_orientation = EsO([
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ])
        super(LTurn, self).__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class BTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CsP([
            Co.URF, Co.UFL, Co.UBR, Co.DRB,
            Co.DFR, Co.DLF, Co.ULB, Co.DBL
        ])
        corner_orientation = CsO([
            CorOri.normal, CorOri.normal, CorOri.clockwised, CorOri.anticlockwised,
            CorOri.normal, CorOri.normal, CorOri.anticlockwised, CorOri.clockwised,
        ])
        edge_permutation = EsP([
            Ed.UR, Ed.UF, Ed.UL, Ed.BR,
            Ed.DR, Ed.DF, Ed.DL, Ed.BL,
            Ed.FR, Ed.FL, Ed.UB, Ed.DB
        ])
        edge_orientation = EsO([
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.fliped,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.fliped,
            EdgOri.normal, EdgOri.normal, EdgOri.fliped, EdgOri.fliped,
        ])
        super(BTurn, self).__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )