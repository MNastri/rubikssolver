from rubikssolver.corners import Corner as Co
from rubikssolver.corners import SingleCornerOrientation as CorOri
from rubikssolver.edges import Edge as Ed
from rubikssolver.edges import SingleEdgeOrientation as EdgOri
from rubikssolver.cubies_cube import CubieCube


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


if __name__ == "__main__":
    print(UTurn())
    print()
    print(UTurn() * UTurn())
    print()
    print(UTurn() * UTurn() * UTurn())
    print()
    print(UTurn() * UTurn() * UTurn() * UTurn())


class RTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.DFR, Co.UFL, Co.ULB, Co.URF,
            Co.DRB, Co.DLF, Co.DBL, Co.UBR
        ]
        corner_orientation = [
            CorOri.anticlockwised, CorOri.normal, CorOri.normal, CorOri.clockwised,
            CorOri.clockwised, CorOri.normal, CorOri.normal, CorOri.anticlockwised,
        ]
        edge_permutation = [
            Ed.FR, Ed.UF, Ed.UL, Ed.UB,
            Ed.BR, Ed.DF, Ed.DL, Ed.DB,
            Ed.DR, Ed.FL, Ed.BL, Ed.UR
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


class FTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.UFL, Co.DLF, Co.ULB, Co.UBR,
            Co.URF, Co.DFR, Co.DBL, Co.DRB
        ]
        corner_orientation = [
            CorOri.clockwised, CorOri.anticlockwised, CorOri.normal, CorOri.normal,
            CorOri.anticlockwised, CorOri.clockwised, CorOri.normal, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UR, Ed.FL, Ed.UL, Ed.UB,
            Ed.DR, Ed.FR, Ed.DL, Ed.DB,
            Ed.UF, Ed.DF, Ed.BL, Ed.BR
        ]
        edge_orientation = [
            EdgOri.normal, EdgOri.fliped, EdgOri.normal, EdgOri.normal,
            EdgOri.normal, EdgOri.fliped, EdgOri.normal, EdgOri.normal,
            EdgOri.fliped, EdgOri.fliped, EdgOri.normal, EdgOri.normal,
        ]
        super().__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )


class DTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.URF, Co.UFL, Co.ULB, Co.UBR,
            Co.DLF, Co.DBL, Co.DRB, Co.DFR
        ]
        corner_orientation = [
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
            CorOri.normal, CorOri.normal, CorOri.normal, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UR, Ed.UF, Ed.UL, Ed.UB,
            Ed.DF, Ed.DL, Ed.DB, Ed.DR,
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


class LTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.URF, Co.ULB, Co.DBL, Co.UBR,
            Co.DFR, Co.UFL, Co.DLF, Co.DRB
        ]
        corner_orientation = [
            CorOri.normal, CorOri.clockwised, CorOri.anticlockwised, CorOri.normal,
            CorOri.normal, CorOri.anticlockwised, CorOri.clockwised, CorOri.normal,
        ]
        edge_permutation = [
            Ed.UR, Ed.UF, Ed.BL, Ed.UB,
            Ed.DR, Ed.DF, Ed.FL, Ed.DB,
            Ed.FR, Ed.UL, Ed.DL, Ed.BR
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


class BTurn(CubieCube):
    def __init__(self):
        corner_permutation = [
            Co.URF, Co.UFL, Co.UBR, Co.DRB,
            Co.DFR, Co.DLF, Co.ULB, Co.DBL
        ]
        corner_orientation = [
            CorOri.normal, CorOri.normal, CorOri.clockwised, CorOri.anticlockwised,
            CorOri.normal, CorOri.normal, CorOri.anticlockwised, CorOri.clockwised,
        ]
        edge_permutation = [
            Ed.UR, Ed.UF, Ed.UL, Ed.BR,
            Ed.DR, Ed.DF, Ed.DL, Ed.BL,
            Ed.FR, Ed.FL, Ed.UB, Ed.DB
        ]
        edge_orientation = [
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.fliped,
            EdgOri.normal, EdgOri.normal, EdgOri.normal, EdgOri.fliped,
            EdgOri.normal, EdgOri.normal, EdgOri.fliped, EdgOri.fliped,
        ]
        super().__init__(
            corner_permutation, corner_orientation,
            edge_permutation, edge_orientation
        )