from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_10(r_ir, r_stage):
    ctrl_signals = None

    # ---------- 0x80 ~ 0x8F ----------
    # illegal opcodes
    if r_ir == 0x80:
        pass

    # STA-(IND,X)
    elif r_ir == 0x81:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x82:
        pass

    # illegal opcodes
    elif r_ir == 0x83:
        pass

    # STY-ZEROPAGE
    elif r_ir == 0x84:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=3, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # STA-ZEROPAGE
    elif r_ir == 0x85:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # STX-ZEROPAGE
    elif r_ir == 0x86:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x87:
        pass

    # DEY-IMPLIED
    elif r_ir == 0x88:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_y=1, sel_cin=0, sel_alu=0, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_main=3, sel_ain=2, sel_bin=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x89:
        pass

    # TXA-IMPLIED
    elif r_ir == 0x8A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=2, en_a=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x8B:
        pass

    # STY-ABSOLUTE
    elif r_ir == 0x8C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=3, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # STA-ABSOLUTE
    elif r_ir == 0x8D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # STX-ABSOLUTE
    elif r_ir == 0x8E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x8F:
        pass

    # ---------- 0x90 ~ 0x9F ----------
    # BCC-RELATIVE
    elif r_ir == 0x90:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=9, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # STA-(IND),Y
    elif r_ir == 0x91:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x92:
        pass

    # illegal opcodes
    elif r_ir == 0x93:
        pass

    # STY-ZPG,X
    elif r_ir == 0x94:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=3, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # STA-ZPG,X
    elif r_ir == 0x95:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # STX-ZPG,Y
    elif r_ir == 0x96:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x97:
        pass

    # illegal opcodes
    elif r_ir == 0x98:
        pass

    # STA-ABS,Y
    elif r_ir == 0x99:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # TXS-IMPLIED
    elif r_ir == 0x9A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=2, en_sp=1, sel_abh=4, sel_abl=4)

    # TYA-IMPLIED
    elif r_ir == 0x9B:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=3, en_a=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x9C:
        pass

    # STA-ABS,X
    elif r_ir == 0x9D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x9E:
        pass

    # illegal opcodes
    elif r_ir == 0x9F:
        pass

    # ---------- 0xA0 ~ 0xAF ----------
    # LDY-IMMEDIATE
    elif r_ir == 0xA0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, en_p=0x82, sel_p=2, sel_main=1, en_y=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # LDA-(IND,X)
    elif r_ir == 0xA1:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # LDX-IMMEDIATE
    elif r_ir == 0xA2:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_x=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # illegal opcodes
    elif r_ir == 0xA3:
        pass

    # LDY-ZEROPAGE
    elif r_ir == 0xA4:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_y=1, sel_abh=4, sel_abl=4)

    # LDA-ZEROPAGE
    elif r_ir == 0xA5:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # LDX-ZEROPAGE
    elif r_ir == 0xA6:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_x=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xA7:
        pass

    # illegal opcodes
    elif r_ir == 0xA8:
        pass

    # LDA-IMMEDIATE
    elif r_ir == 0xA9:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # TAX-IMPLIED
    elif r_ir == 0xAA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=4, en_x=1, sel_abh=4, sel_abl=4)

    # TAY-IMPLIED
    elif r_ir == 0xAB:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=4, en_y=1, sel_abh=4, sel_abl=4)

    # LDY-ABSOLUTE
    elif r_ir == 0xAC:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_y=1, sel_abh=4, sel_abl=4)

    # LDA-ABSOLUTE
    elif r_ir == 0xAD:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # LDX-ABSOLUTE
    elif r_ir == 0xAE:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_x=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xAF:
        pass

    # ---------- 0xB0 ~ 0xBF ----------
    # BCS-RELATIVE
    elif r_ir == 0xB0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=0xA, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # LDA-(IND),Y
    elif r_ir == 0xB1:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xB2:
        pass

    # illegal opcodes
    elif r_ir == 0xB3:
        pass

    # LDY-ZPG,X
    elif r_ir == 0xB4:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_y=1, sel_abh=4, sel_abl=4)

    # LDA-ZPG,X
    elif r_ir == 0xB5:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # LDX-ZPG,Y
    elif r_ir == 0xB6:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_x=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xB7:
        pass

    # CLV-IMPLIED
    elif r_ir == 0xB8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x40, sel_p=0, sel_abh=4, sel_abl=4)

    # LDA-ABS,Y
    elif r_ir == 0xB9:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # TSX-IMPLIED
    elif r_ir == 0xBA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=5, en_x=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xBB:
        pass

    # LDY-ABS,X
    elif r_ir == 0xBC:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_y=1, sel_abh=4, sel_abl=4)

    # LDA-ABS,X
    elif r_ir == 0xBD:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_a=1, sel_abh=4, sel_abl=4)

    # LDX-ABS,Y
    elif r_ir == 0xBE:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(o_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(o_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=1, sel_st=2, en_p=0x82, sel_p=2, sel_main=1, en_x=1, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0xBF:
        pass

    # ---------- Default ----------
    if ctrl_signals is None:
        ctrl_signals = ctrl_t()

    return ctrl_signals
