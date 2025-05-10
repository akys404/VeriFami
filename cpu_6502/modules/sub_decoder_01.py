from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_01(r_ir, r_stage):
    ctrl_signals = None

    # ---------- 0x40 ~ 0x4F ----------
    # RTI-IMPLIED
    if r_ir == 0x40:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=3, sel_ain=0, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, en_p=0xFF, sel_p=3, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=0, sel_sub=1, en_sp=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # EOR-(IND,X)
    elif r_ir == 0x41:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x42:
        pass

    # illegal opcodes
    elif r_ir == 0x43:
        pass

    # illegal opcodes
    elif r_ir == 0x44:
        pass

    # EOR-ZEROPAGE
    elif r_ir == 0x45:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # LSR-ZEROPAGE
    elif r_ir == 0x46:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=0, sel_alu=6)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x47:
        pass

    # PHA-IMPLIED
    elif r_ir == 0x48:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=4, sel_abl=4)

    # EOR-IMMEDIATE
    elif r_ir == 0x49:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # LSR-ACCUM
    elif r_ir == 0x4A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=6, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_ain=2, sel_bin=0, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x4B:
        pass

    # JMP-ABSOLUTE
    elif r_ir == 0x4C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # EOR-ABSOLUTE
    elif r_ir == 0x4D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # LSR-ABSOLUTE
    elif r_ir == 0x4E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=0, sel_alu=6)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x4F:
        pass

    # ---------- 0x50 ~ 0x5F ----------
    # BVC-RELATIVE
    elif r_ir == 0x50:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=7, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # EOR-(IND),Y
    elif r_ir == 0x51:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x52:
        pass

    # illegal opcodes
    elif r_ir == 0x53:
        pass

    # illegal opcodes
    elif r_ir == 0x54:
        pass

    # EOR-ZPG,X
    elif r_ir == 0x55:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # LSR-ZPG,X
    elif r_ir == 0x56:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=0, sel_alu=6)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x57:
        pass

    # CLI-IMPLIED
    elif r_ir == 0x58:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x04, sel_p=0, sel_abh=4, sel_abl=4)

    # EOR-ABS,Y
    elif r_ir == 0x59:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x5A:
        pass

    # illegal opcodes
    elif r_ir == 0x5B:
        pass

    # illegal opcodes
    elif r_ir == 0x5C:
        pass

    # EOR-ABS,X
    elif r_ir == 0x5D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=4, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # LSR-ABS,X
    elif r_ir == 0x5E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=0, sel_alu=6)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x5F:
        pass

    # ---------- 0x60 ~ 0x6F ----------
    # RTS-IMPLIED
    elif r_ir == 0x60:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=3, sel_ain=0, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=0, sel_sub=1, en_sp=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # ADC-(IND,X)
    elif r_ir == 0x61:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x62:
        pass

    # illegal opcodes
    elif r_ir == 0x63:
        pass

    # illegal opcodes
    elif r_ir == 0x64:
        pass

    # ADC-ZEROPAGE
    elif r_ir == 0x65:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROR-ZEROPAGE
    elif r_ir == 0x66:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=8)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x67:
        pass

    # PLA-IMPLIED
    elif r_ir == 0x68:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=3, sel_ain=0, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=0, en_sp=1, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # ADC-IMMEDIATE
    elif r_ir == 0x69:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # ROR-ACCUM
    elif r_ir == 0x6A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=8, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_ain=2, sel_bin=0, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x6B:
        pass

    # JMP-INDIRECT
    elif r_ir == 0x6C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # ADC-ABSOLUTE
    elif r_ir == 0x6D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROR-ABSOLUTE
    elif r_ir == 0x6E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=8)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x6F:
        pass

    # ---------- 0x70 ~ 0x7F ----------
    # BVS-RELATIVE
    elif r_ir == 0x70:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=8, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # ADC-(IND),Y
    elif r_ir == 0x71:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x72:
        pass

    # illegal opcodes
    elif r_ir == 0x73:
        pass

    # illegal opcodes
    elif r_ir == 0x74:
        pass

    # ADC-ZPG,X
    elif r_ir == 0x75:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROR-ZPG,X
    elif r_ir == 0x76:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=8)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x77:
        pass

    # SEI-IMPLIED
    elif r_ir == 0x78:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x04, sel_p=1, sel_abh=4, sel_abl=4)

    # ADC-ABS,Y
    elif r_ir == 0x79:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x7A:
        pass

    # illegal opcodes
    elif r_ir == 0x7B:
        pass

    # illegal opcodes
    elif r_ir == 0x7C:
        pass

    # ADC-ABS,X
    elif r_ir == 0x7D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0xC3, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROR-ABS,X
    elif r_ir == 0x7E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=8)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x7F:
        pass

    # ---------- Default ----------
    if ctrl_signals is None:
        ctrl_signals = ctrl_t()

    return ctrl_signals
