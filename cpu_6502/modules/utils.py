from enum import Enum

class stage_e(Enum):
    T1 = 0
    T2 = 1
    T3 = 2
    T4 = 3
    T5 = 4
    T6 = 5
    UNUSED = 6
    T0 = 7

class ctrl_t:
    def __init__(self):
        self.o_rw = 1
        self.en_ir = 0
        self.sel_st = 0
        self.en_p = 0
        self.sel_p = 0
        self.sel_b = 0
        self.sel_main = 0
        self.sel_sub = 0
        self.en_x = 0
        self.en_y = 0
        self.en_a = 0
        self.en_sp = 0
        self.sel_ain = 0
        self.sel_bin = 0
        self.sel_cin = 0
        self.sel_alu = 0
        self.sel_abh = 0
        self.sel_abl = 0
        self.sel_pch = 0
        self.sel_pcl = 0

    def update(self, diff):
        for key, val in diff.items():
            setattr(self, key, val)

    def __repr__(self):
        return " ".join(
            f"{k}:{v:02X}"
            for k, v in self.__dict__.items()
            if (v != 0 or k == 'o_rw')
        )

