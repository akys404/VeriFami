from enum import Enum
from dataclasses import dataclass

class stage_e(Enum):
    T1 = 0
    T2 = 1
    T3 = 2
    T4 = 3
    T5 = 4
    T6 = 5
    UNUSED = 6
    T0 = 7

@dataclass
class ctrl_t:
    o_rw: int = 1
    en_ir: int = 0
    sel_st: int = 0
    en_p: int = 0
    sel_p: int = 0
    sel_b: int = 0
    sel_main: int = 0
    sel_sub: int = 0
    en_x: int = 0
    en_y: int = 0
    en_a: int = 0
    en_sp: int = 0
    sel_ain: int = 0
    sel_bin: int = 0
    sel_cin: int = 0
    sel_alu: int = 0
    sel_abh: int = 0
    sel_abl: int = 0
    sel_pch: int = 0
    sel_pcl: int = 0