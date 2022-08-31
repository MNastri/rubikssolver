from enum import IntEnum

from rubikssolver.face_turns import (
    BTurn,
    DTurn,
    FTurn,
    LTurn,
    RTurn,
    UTurn,
)
from rubikssolver.slice_turns import (
    ETurn,
    MTurn,
    STurn,
)


class Move(IntEnum):
    U1 = 0
    U2 = 1
    U3 = 2
    R1 = 3
    R2 = 4
    R3 = 5
    F1 = 6
    F2 = 7
    F3 = 8
    D1 = 9
    D2 = 10
    D3 = 11
    L1 = 12
    L2 = 13
    L3 = 14
    B1 = 15
    B2 = 16
    B3 = 17
    E1 = 18
    E2 = 19
    E3 = 20
    M1 = 21
    M2 = 22
    M3 = 23
    S1 = 24
    S2 = 25
    S3 = 26


MOVES = [
    UTurn(),
    UTurn() * UTurn(),
    UTurn() * UTurn() * UTurn(),
    RTurn(),
    RTurn() * RTurn(),
    RTurn() * RTurn() * RTurn(),
    FTurn(),
    FTurn() * FTurn(),
    FTurn() * FTurn() * FTurn(),
    DTurn(),
    DTurn() * DTurn(),
    DTurn() * DTurn() * DTurn(),
    LTurn(),
    LTurn() * LTurn(),
    LTurn() * LTurn() * LTurn(),
    BTurn(),
    BTurn() * BTurn(),
    BTurn() * BTurn() * BTurn(),
    ETurn(),
    ETurn() * ETurn(),
    ETurn() * ETurn() * ETurn(),
    MTurn(),
    MTurn() * MTurn(),
    MTurn() * MTurn() * MTurn(),
    STurn(),
    STurn() * STurn(),
    STurn() * STurn() * STurn(),
]
