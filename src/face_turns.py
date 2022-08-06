from corners import Corner as Co
from corners import CornersOrientation as CO
from corners import CornersPermutation as CP
from corners import SingleCornerOrientation as CorOri
from cube_transformations import CubeTransformation
from edges import Edge as Ed
from edges import EdgesOrientation as EO
from edges import EdgesPermutation as EP
from edges import SingleEdgeOrientation as EdgOri


class UTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CP([
            Co.UBR, Co.URF, Co.UFL, Co.ULB,
            Co.DFR, Co.DLF, Co.DBL, Co.DRB
        ])
        corner_orientation = CO([
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ])
        edge_permutation = EP([
            Ed.UB, Ed.UR, Ed.UF, Ed.UL,
            Ed.DR, Ed.DF, Ed.DL, Ed.DB,
            Ed.FR, Ed.FL, Ed.BL, Ed.BR
        ])
        edge_orientation = EO([
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.normal,
        ])
        super(UTurn, self).__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class RTurn(CubeTransformation):
    def __init__(self):
        corner_permutation = CP([
            Co.DFR, Co.UFL, Co.ULB, Co.URF,
            Co.DRB, Co.DLF, Co.DBL, Co.UBR
        ])
        corner_orientation = CO([
            CorOri.turned_twice, CorOri.normal, CorOri.normal, CorOri.turned_once,
            CorOri.turned_once, CorOri.normal, CorOri.normal, CorOri.turned_twice,
        ])
        edge_permutation = EP([
            Ed.FR, Ed.UF, Ed.UL, Ed.UB,
            Ed.BR, Ed.DF, Ed.DL, Ed.DB,
            Ed.DR, Ed.FL, Ed.BL, Ed.UR
        ])
        edge_orientation = EO([
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
        corner_permutation = CP([
            Co.UFL, Co.DLF, Co.ULB, Co.UBR,
            Co.URF, Co.DFR, Co.DBL, Co.DRB
        ])
        corner_orientation = CO([
            CorOri.turned_once, CorOri.turned_twice, CorOri.normal, CorOri.normal,
            CorOri.turned_twice, CorOri.turned_once, CorOri.normal, CorOri.normal,
        ])
        edge_permutation = EP([
            Ed.UR, Ed.FL, Ed.UL, Ed.UB,
            Ed.DR, Ed.FR, Ed.DL, Ed.DB,
            Ed.UF, Ed.DF, Ed.BL, Ed.BR
        ])
        edge_orientation = EO([
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
        corner_permutation = CP([
            Co.URF, Co.UFL, Co.ULB, Co.UBR,
            Co.DLF, Co.DBL, Co.DRB, Co.DFR
        ])
        corner_orientation = CO([
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ])
        edge_permutation = EP([
            Ed.UR, Ed.UF, Ed.UL, Ed.UB,
            Ed.DF, Ed.DL, Ed.DB, Ed.DR,
            Ed.FR, Ed.FL, Ed.BL, Ed.BR
        ])
        edge_orientation = EO([
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
        corner_permutation = CP([
            Co.URF, Co.ULB, Co.DBL, Co.UBR,
            Co.DFR, Co.UFL, Co.DLF, Co.DRB
        ])
        corner_orientation = CO([
            CorOri.normal, CorOri.turned_once, CorOri.turned_twice, CorOri.normal,
            CorOri.normal, CorOri.turned_twice, CorOri.turned_once, CorOri.normal,
        ])
        edge_permutation = EP([
            Ed.UR, Ed.UF, Ed.BL, Ed.UB,
            Ed.DR, Ed.DF, Ed.FL, Ed.DB,
            Ed.FR, Ed.UL, Ed.DL, Ed.BR
        ])
        edge_orientation = EO([
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
        corner_permutation = CP([Co.URF, Co.UFL, Co.UBR, Co.DRB, Co.DFR, Co.DLF, Co.ULB, Co.DBL])
        corner_orientation = CO([0, 0, 1, 2, 0, 0, 2, 1])
        edge_permutation = EP([Ed.UR, Ed.UF, Ed.UL, Ed.BR, Ed.DR, Ed.DF, Ed.DL, Ed.BL, Ed.FR, Ed.FL, Ed.UB, Ed.DB])
        edge_orientation = EO([0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1])
        super(BTurn, self).__init__(corner_permutation, corner_orientation, edge_permutation, edge_orientation)
