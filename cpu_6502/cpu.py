from cpu_6502.modules.utils import stage_e
from cpu_6502.modules.decoder import decoder

class mod_cpu:
    def __init__(self, debug=False):
        # Control Region
        self.r_ir = 0
        self.r_stage = stage_e.T1
        self.r_res = 0
        self.r_rst_old = 1
        self.r_nmi = 0
        self.r_nmi_old = 1
        self.r_nmi_latch = 0
        self.r_irq = 0
        self.r_cout_old = 0
        self.r_p = 0b0000_0100
        # Register Region
        self.r_x = 0
        self.r_y = 0
        self.r_a = 0
        self.r_sp = 0xFD
        self.r_ain = 0
        self.r_bin = 0
        self.r_abh = 0
        self.r_abl = 0
        self.r_pch = 0
        self.r_pcl = 0
        self.r_dor = 0
        self.r_rw = 1
        # for debug
        self.p_debug = debug
        self.r_main = 0
        self.r_sub = 0
        self.r_alu = 0
        self.r_alu_op = 0

    def step(self, d_data, rst_n=1, i_nmi=1, i_irq=1, i_rdy=1):
    # Read only register
        # Control Region
        r_ir = self.r_ir
        r_stage = self.r_stage
        r_res = self.r_res
        r_rst_old = self.r_rst_old
        r_nmi = self.r_nmi
        r_nmi_old = self.r_nmi_old
        r_nmi_latch = self.r_nmi_latch
        r_irq = self.r_irq
        r_cout_old = self.r_cout_old
        r_p = self.r_p
        # Register Region
        r_x = self.r_x
        r_y = self.r_y
        r_a = self.r_a
        r_sp = self.r_sp
        r_ain = self.r_ain
        r_bin = self.r_bin
        r_abh = self.r_abh
        r_abl = self.r_abl
        r_pch = self.r_pch
        r_pcl = self.r_pcl
        r_dor = self.r_dor
        r_rw = self.r_rw

    # Evaluate
        # Decoder
        ctrl = decoder(self)

        # input signals
        f_rdy = i_rdy & r_rw

        # output signals
        o_rw = r_rw
        o_address = r_abh << 8 | r_abl
        o_data = 'zz' if r_rw else r_dor
        o_sync = r_stage == stage_e.T1
        
        if self.p_debug:
            if not r_rw:
                print(f'── WRITE ── address: 0x{o_address:04X}  data: 0x{o_data:02X}')
            elif not f_rdy:
                print('── HALT ──')
            elif o_sync:
                print('── SYNC ──')

        # ALU
        if ctrl.sel_cin == 0:
            f_cin = 0
        elif ctrl.sel_cin == 1:
            f_cin = 1
        elif ctrl.sel_cin == 2:
            f_cin = r_p & 0b0000_0001
        elif ctrl.sel_cin == 3:
            f_cin = r_cout_old

        if ctrl.sel_alu == 0:   # ADD
            d_alu_internal = r_ain + r_bin + f_cin
        elif ctrl.sel_alu == 1: # SUB
            d_alu_internal = r_ain + (~r_bin & 0xFF) + f_cin
        elif ctrl.sel_alu == 2: # AND
            d_alu_internal = r_ain & r_bin
        elif ctrl.sel_alu == 3: # OR
            d_alu_internal = r_ain | r_bin
        elif ctrl.sel_alu == 4: # XOR
            d_alu_internal = r_ain ^ r_bin
        elif ctrl.sel_alu == 5: # SLL
            d_alu_internal = r_ain << 1
        elif ctrl.sel_alu == 6: # SRL
            d_alu_internal = r_ain >> 1
        elif ctrl.sel_alu == 7: # ROL
            d_alu_internal = (r_ain << 1) | (f_cin)
        elif ctrl.sel_alu == 8: # ROR
            d_alu_internal = ((r_ain << 9) | (f_cin << 8) | (r_ain)) >> 1

        d_alu = d_alu_internal & 0xFF
        f_cout = d_alu_internal >> 8 & 0x01
        if ctrl.sel_alu == 0:
            f_vout = ((~r_ain & ~r_bin & d_alu) | (r_ain & r_bin & ~d_alu)) >> 7
        elif ctrl.sel_alu == 1:
            f_vout = ((~r_ain & r_bin & d_alu) | (r_ain & ~r_bin & ~d_alu)) >> 7
        else:
            f_vout = 0

        # Main bus
        d_p_mem = r_p | ctrl.sel_b << 4
        
        if ctrl.sel_main == 0:
            d_main = d_alu
        elif ctrl.sel_main == 1:
            d_main = d_data
        elif ctrl.sel_main == 2:
            d_main = r_x
        elif ctrl.sel_main == 3:
            d_main = r_y
        elif ctrl.sel_main == 4:
            d_main = r_a
        elif ctrl.sel_main == 5:
            d_main = r_sp
        elif ctrl.sel_main == 6:
            d_main = r_pch
        elif ctrl.sel_main == 7:
            d_main = r_pcl
        elif ctrl.sel_main == 8:
            d_main = d_p_mem

        # Sub bus
        d_pc_inc = (r_pch << 8 | r_pcl) + 1

        if ctrl.sel_sub == 0:
            d_sub = d_alu
        elif ctrl.sel_sub == 1:
            d_sub = d_data
        elif ctrl.sel_sub == 2:
            d_sub = d_pc_inc & 0xFF
        elif ctrl.sel_sub == 3:
            d_sub = r_sp

        # P state
        f_neg = d_main >> 7 & 0x01
        f_zero = d_main == 0
        if ctrl.sel_p == 0:
            d_p = 0x00
        elif ctrl.sel_p == 1:
            d_p = 0xFF
        elif ctrl.sel_p == 2:
            d_p = f_neg << 7 | f_vout << 6 | f_zero << 1 | f_cout
        elif ctrl.sel_p == 3:
            d_p = d_data

        # Branch flag
        if ctrl.sel_st == 0x5:   # BPL
            if not (r_p & 0b1000_0000):
                f_branch = 1
        elif ctrl.sel_st == 0x6: # BMI
            if r_p & 0b1000_0000:
                f_branch = 1
        elif ctrl.sel_st == 0x7: # BVC
            if not (r_p & 0b0100_0000):
                f_branch = 1
        elif ctrl.sel_st == 0x8: # BVS
            if r_p & 0b0100_0000:
                f_branch = 1
        elif ctrl.sel_st == 0x9: # BCC
            if not (r_p & 0b0000_0001):
                f_branch = 1
        elif ctrl.sel_st == 0xA: # BCS
            if r_p & 0b0000_0001:
                f_branch = 1
        elif ctrl.sel_st == 0xB: # BNE
            if not (r_p & 0b0000_0010):
                f_branch = 1
        elif ctrl.sel_st == 0xC: # BEQ
            if r_p & 0b0000_0010:
                f_branch = 1
        else:
            f_branch =0

        # Next stage
        if ctrl.sel_st == 0x0:
            d_nextstage = stage_e((r_stage.value + 1) % 7)
        elif ctrl.sel_st == 0x1:
            d_nextstage = stage_e.T0
        elif ctrl.sel_st == 0x2:
            d_nextstage = stage_e.T1
        elif ctrl.sel_st == 0x3:
            if f_cout == 0:
                d_nextstage = stage_e.T0
            if f_cout == 1:
                d_nextstage = stage_e((r_stage.value + 1) % 7)
        elif ctrl.sel_st == 0x4:
            if r_ain >> 7 ^ f_cout:
                d_nextstage = stage_e.T0
            else:
                d_nextstage = stage_e.T1
        elif ctrl.sel_st in [0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC]:
            if f_branch:
                d_nextstage = stage_e.T1
            else:
                d_nextstage = stage_e((r_stage.value + 1) % 7)

    # Control register
        # RES detector
        if not rst_n:
            self.r_res = 0
        elif not r_rst_old and rst_n:
            self.r_res = 1
        elif f_rdy and r_stage == stage_e.T1:
            self.r_res = 0

        if not rst_n:
            self.r_rst_old = 0
        else:
            self.r_rst_old = rst_n

        # NMI detector
        if not rst_n:
            self.r_nmi = 0
        elif f_rdy and r_stage == stage_e.T1:
            self.r_nmi = r_nmi_latch

        if not rst_n:
            self.r_nmi_latch = 0
        elif not r_nmi_old and i_nmi:
            self.r_nmi_latch = 1
        elif f_rdy and r_stage == stage_e.T1:
            self.r_nmi_latch = 0

        if not rst_n:
            self.r_nmi_old = 1
        else:
            self.r_nmi_old = i_nmi

        # IRQ detector
        if not rst_n:
            self.r_irq = 0
        elif f_rdy and r_stage == stage_e.T1:
            if not (r_p & 0b0000_0100):
                self.r_irq = not i_irq
            else:
                self.r_irq = 0

        # State Machine
        if not rst_n:
            self.r_ir = 0
        elif f_rdy and ctrl.en_ir:
            self.r_ir = d_data

        if not rst_n:
            self.r_stage = stage_e.T1
        elif f_rdy:
            self.r_stage = d_nextstage

        if f_rdy:
            self.r_cout_old = f_cout

        # P register
        if not rst_n:
            self.r_p = 0b0000_0100
        elif f_rdy:
            masked_en_p = ctrl.en_p & 0b1100_1111
            self.r_p = (r_p & ~masked_en_p) | (d_p & masked_en_p)

    # Data register
        if not rst_n:
            self.r_x = 0
        elif f_rdy and ctrl.en_x:
            self.r_x = d_main

        if not rst_n:
            self.r_y = 0
        elif f_rdy and ctrl.en_y:
            self.r_y = d_main

        if not rst_n:
            self.r_a = 0
        elif f_rdy and ctrl.en_a:
            self.r_a = d_main

        if not rst_n:
            self.r_sp = 0
        elif f_rdy and ctrl.en_sp:
            self.r_sp = d_main

        if not rst_n:
            self.r_rw = 1
        else:
            self.r_rw = ctrl.sel_rw

        if f_rdy:
            self.r_dor = d_main

        if f_rdy:
            if ctrl.sel_ain == 0:
                self.r_ain = 0x00
            elif ctrl.sel_ain == 1:
                self.r_ain = 0xFF
            elif ctrl.sel_ain == 2:
                self.r_ain = d_main

        if f_rdy:
            if ctrl.sel_bin == 0:
                self.r_bin = 0x00
            elif ctrl.sel_bin == 1:
                self.r_bin = 0xFF
            elif ctrl.sel_bin == 2:
                self.r_bin = d_sub
            elif ctrl.sel_bin == 3:
                if not (r_ain >> 7):
                    self.r_bin = 0x00
                elif r_ain >> 7:
                    self.r_bin = 0xFF

    # Address register
        if not rst_n:
            self.r_abh = 0
        elif f_rdy:
            if ctrl.sel_abh == 0x1:
                self.r_abh = d_pc_inc >> 8 & 0xFF
            elif ctrl.sel_abh == 0x2 and r_cout_old:
                self.r_abh = d_alu
            elif ctrl.sel_abh == 0x3:
                self.r_abh = d_data
            elif ctrl.sel_abh == 0x4:
                self.r_abh = r_pch
            elif ctrl.sel_abh == 0x5:
                self.r_abh = 0x00
            elif ctrl.sel_abh == 0x6:
                self.r_abh = 0x01
            elif ctrl.sel_abh == 0x7:
                self.r_abh = 0xFF
                
        if not rst_n:
            self.r_abl = 0
        elif f_rdy:
            if ctrl.sel_abl == 0x1:
                self.r_abl = d_pc_inc & 0xFF
            elif ctrl.sel_abl == 0x2:
                self.r_abl = d_alu
            elif ctrl.sel_abl == 0x3:
                self.r_abl = d_data
            elif ctrl.sel_abl == 0x4:
                self.r_abl = r_pcl
            elif ctrl.sel_abl == 0x5:
                self.r_abl = r_sp
            elif ctrl.sel_abl == 0x6:
                self.r_abl = 0xFA
            elif ctrl.sel_abl == 0x7:
                self.r_abl = 0xFB
            elif ctrl.sel_abl == 0x8:
                self.r_abl = 0xFC
            elif ctrl.sel_abl == 0x9:
                self.r_abl = 0xFD
            elif ctrl.sel_abl == 0xA:
                self.r_abl = 0xFE
            elif ctrl.sel_abl == 0xB:
                self.r_abl = 0xFF

        if not rst_n:
            self.r_pch = 0
        elif f_rdy:
            if ctrl.sel_pch == 1:
                self.r_pch = d_pc_inc >> 8 & 0xFF
            elif ctrl.sel_pch == 3:
                self.r_pch = d_data

        if not rst_n:
            self.r_pcl = 0
        elif f_rdy:
            if ctrl.sel_pcl == 1:
                self.r_pcl = d_pc_inc & 0xFF
            elif ctrl.sel_pcl == 2:
                self.r_pcl = d_alu
            elif ctrl.sel_pcl == 3:
                self.r_pcl = r_sp

        # for debug
        self.r_main = d_main
        self.r_sub = d_sub
        self.r_alu = d_alu
        self.r_alu_op = ctrl.sel_alu
        if self.p_debug:
            print(self)

        return {'o_rw':o_rw, 'o_address':o_address, 'o_data':o_data}

    def __repr__(self):
        hidden_keys = {'r_rst_old', 'r_nmi_old', 'r_nmi_latch', 'r_cout_old', 'p_debug'}
        return " ".join(
            f"{k[2:].upper()}:{v.name if isinstance(v, stage_e) else f'{v:02X}'}"
            for k, v in self.__dict__.items()
            if (k not in hidden_keys)
        )
    