from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_11(r_ir, r_stage):
    ctrl_signals = None

    # ---------- 0xC0 ~ 0xCF ----------
    # CPY-IMMEDIATE
    if r_ir == 0xC0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=1, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # CMP-(IND,X)
    elif r_ir == 0xC1:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xC2:
        pass

    # illegal opcodes
    elif r_ir == 0xC3:
        pass

    # CPY-ZEROPAGE
    elif r_ir == 0xC4:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=1, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # CMP-ZEROPAGE
    elif r_ir == 0xC5:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # DEC-ZEROPAGE
    elif r_ir == 0xC6:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=1, sel_bin=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=0, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xC7:
        pass

    # INY-IMPLIED
    elif r_ir == 0xC8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_y=1, sel_cin=1, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=3, sel_ain=2, sel_bin=0, sel_abh=4, sel_abl=4)

    # CMP-IMMEDIATE
    elif r_ir == 0xC9:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # DEX-IMPLIED
    elif r_ir == 0xCA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_x=1, sel_cin=0, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=2, sel_ain=2, sel_bin=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xCB:
        pass

    # CPY-ABSOLUTE
    elif r_ir == 0xCC:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=1, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # CMP-ABSOLUTE
    elif r_ir == 0xCD:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # DEC-ABSOLUTE
    elif r_ir == 0xCE:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=1, sel_bin=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=0, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xCF:
        pass

    # ---------- 0xD0 ~ 0xDF ----------
    # BNE-RELATIVE
    elif r_ir == 0xD0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=0xB, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # CMP-(IND),Y
    elif r_ir == 0xD1:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xD2:
        pass

    # illegal opcodes
    elif r_ir == 0xD3:
        pass

    # illegal opcodes
    elif r_ir == 0xD4:
        pass

    # CMP-ZPG,X
    elif r_ir == 0xD5:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # DEC-ZPG,X
    elif r_ir == 0xD6:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=1, sel_bin=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=0, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xD7:
        pass

    # CLD-IMPLIED
    elif r_ir == 0xD8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0x08, sel_p=0, sel_abh=4, sel_abl=4)

    # CMP-ABS,Y
    elif r_ir == 0xD9:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xDA:
        pass

    # illegal opcodes
    elif r_ir == 0xDB:
        pass

    # illegal opcodes
    elif r_ir == 0xDC:
        pass

    # CMP-ABS,X
    elif r_ir == 0xDD:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # DEC-ABS,X
    elif r_ir == 0xDE:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=1, sel_bin=2)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=0, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xDF:
        pass

    # ---------- 0xE0 ~ 0xEF ----------
    # CPX-IMMEDIATE
    elif r_ir == 0xE0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=1, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # SBC-(IND,X)
    elif r_ir == 0xE1:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xE2:
        pass

    # illegal opcodes
    elif r_ir == 0xE3:
        pass

    # CPX-ZEROPAGE
    elif r_ir == 0xE4:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=1, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # SBC-ZEROPAGE
    elif r_ir == 0xE5:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # INC-ZEROPAGE
    elif r_ir == 0xE6:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=0, sel_bin=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=1, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xE7:
        pass

    # INX-IMPLIED
    elif r_ir == 0xE8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_x=1, sel_cin=1, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=2, sel_ain=2, sel_bin=0, sel_abh=4, sel_abl=4)

    # SBC-IMMEDIATE
    elif r_ir == 0xE9:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # NOP-IMPLIED
    elif r_ir == 0xEA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xEB:
        pass

    # CPX-ABSOLUTE
    elif r_ir == 0xEC:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=1, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # SBC-ABSOLUTE
    elif r_ir == 0xED:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # INC-ABSOLUTE
    elif r_ir == 0xEE:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=0, sel_bin=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=1, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xEF:
        pass

    # ---------- 0xF0 ~ 0xFF ----------
    # BEQ-RELATIVE
    elif r_ir == 0xF0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=0xC, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # SBC-(IND),Y
    elif r_ir == 0xF1:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xF2:
        pass

    # illegal opcodes
    elif r_ir == 0xF3:
        pass

    # illegal opcodes
    elif r_ir == 0xF4:
        pass

    # SBC-ZPG,X
    elif r_ir == 0xF5:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # INC-ZPG,X
    elif r_ir == 0xF6:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=0, sel_bin=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=1, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xF7:
        pass

    # SED-IMPLIED
    elif r_ir == 0xF8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0x08, sel_p=1, sel_abh=4, sel_abl=4)

    # SBC-ABS,Y
    elif r_ir == 0xF9:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xFA:
        pass

    # illegal opcodes
    elif r_ir == 0xFB:
        pass

    # illegal opcodes
    elif r_ir == 0xFC:
        pass

    # SBC-ABS,X
    elif r_ir == 0xFD:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # INC-ABS,X
    elif r_ir == 0xFE:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_sub=1, sel_ain=0, sel_bin=2)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x82, sel_p=2, sel_main=0, sel_cin=1, sel_alu=0)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xFF:
        pass

    # ---------- Default ----------
    if ctrl_signals is None:
        ctrl_signals = ctrl_t()

    return ctrl_signals
