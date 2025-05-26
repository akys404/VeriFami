from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_00(r_ir, r_stage):
    ctrl_signals = None

    # ---------- 0x00 ~ 0x0F ----------
    # BRK-IMPLIED
    if r_ir == 0x00:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=6, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=7, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_b=1, sel_main=8, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=7, sel_abl=0xA)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=0xB)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # ORA-(IND,X)
    elif r_ir == 0x01:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
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
    elif r_ir == 0x02:
        pass

    # illegal opcodes
    elif r_ir == 0x03:
        pass

    # illegal opcodes
    elif r_ir == 0x04:
        pass

    # ORA-ZEROPAGE
    elif r_ir == 0x05:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ASL-ZEROPAGE
    elif r_ir == 0x06:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=0, sel_alu=5)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x07:
        pass

    # PHP-IMPLIED
    elif r_ir == 0x08:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, sel_b=1, sel_main=8, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=4, sel_abl=4)

    # ORA-IMMEDIATE
    elif r_ir == 0x09:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # ASL-ACCUM
    elif r_ir == 0x0A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=5, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_ain=2, sel_bin=0, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x0B:
        pass

    # illegal opcodes
    elif r_ir == 0x0C:
        pass

    # ORA-ABSOLUTE
    elif r_ir == 0x0D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ASL-ABSOLUTE
    elif r_ir == 0x0E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=0, sel_alu=5)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x0F:
        pass

    # ---------- 0x10 ~ 0x1F ----------
    # BPL-RELATIVE
    elif r_ir == 0x10:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=5, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # ORA-(IND),Y
    elif r_ir == 0x11:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
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
    elif r_ir == 0x12:
        pass

    # illegal opcodes
    elif r_ir == 0x13:
        pass

    # illegal opcodes
    elif r_ir == 0x14:
        pass

    # ORA-ZPG,X
    elif r_ir == 0x15:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x16:
        pass

    # illegal opcodes
    elif r_ir == 0x17:
        pass

    # CLC-IMPLIED
    elif r_ir == 0x18:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0x01, sel_p=0, sel_abh=4, sel_abl=4)

    # ORA-ABS,Y
    elif r_ir == 0x19:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x1A:
        pass

    # illegal opcodes
    elif r_ir == 0x1B:
        pass

    # illegal opcodes
    elif r_ir == 0x1C:
        pass

    # ORA-ABS,X
    elif r_ir == 0x1D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=3, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x1E:
        pass

    # illegal opcodes
    elif r_ir == 0x1F:
        pass

    # ---------- 0x20 ~ 0x2F ----------
    # JSR-ABSOLUTE
    elif r_ir == 0x20:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=1, sel_sub=3, en_sp=1, sel_ain=0, sel_bin=2, sel_abh=6, sel_abl=5, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=6, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=7, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=4, sel_abl=4)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=5, sel_pch=3, sel_pcl=3)

    # AND-(IND,X)
    elif r_ir == 0x21:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
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
    elif r_ir == 0x22:
        pass

    # illegal opcodes
    elif r_ir == 0x23:
        pass

    # BIT-ZEROPAGE
    elif r_ir == 0x24:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x02, sel_p=2, sel_main=0, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0xC0, sel_p=3, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # AND-ZEROPAGE
    elif r_ir == 0x25:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROL-ZEROPAGE
    elif r_ir == 0x26:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_abh=5, sel_abl=3, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x27:
        pass

    # PLP-IMPLIED
    elif r_ir == 0x28:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=3, sel_ain=0, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_main=0, en_sp=1, sel_cin=1, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0xFF, sel_p=3, sel_abh=4, sel_abl=4)

    # AND-IMMEDIATE
    elif r_ir == 0x29:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)

    # ROL-ACCUM
    elif r_ir == 0x2A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x83, sel_p=2, sel_main=0, en_a=1, sel_cin=2, sel_alu=7, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_ain=2, sel_bin=0, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x2B:
        pass

    # BIT-ABSOLUTE
    elif r_ir == 0x2C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x02, sel_p=2, sel_main=0, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0xC0, sel_p=3, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # AND-ABSOLUTE
    elif r_ir == 0x2D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROL-ABSOLUTE
    elif r_ir == 0x2E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x2F:
        pass

    # ---------- 0x30 ~ 0x3F ----------
    # BMI-RELATIVE
    elif r_ir == 0x30:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=6, sel_main=1, sel_sub=2, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=4, sel_main=6, sel_ain=2, sel_bin=3, sel_cin=0, sel_alu=0, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=3, sel_alu=0, sel_abh=2)

    # AND-(IND),Y
    elif r_ir == 0x31:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
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
    elif r_ir == 0x32:
        pass

    # illegal opcodes
    elif r_ir == 0x33:
        pass

    # illegal opcodes
    elif r_ir == 0x34:
        pass

    # AND-ZPG,X
    elif r_ir == 0x35:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROL-ZPG,X
    elif r_ir == 0x36:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x37:
        pass

    # SEC-IMPLIED
    elif r_ir == 0x38:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, en_p=0x01, sel_p=1, sel_abh=4, sel_abl=4)

    # AND-ABS,Y
    elif r_ir == 0x39:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x3A:
        pass

    # illegal opcodes
    elif r_ir == 0x3B:
        pass

    # illegal opcodes
    elif r_ir == 0x3C:
        pass

    # AND-ABS,X
    elif r_ir == 0x3D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_a=1, sel_cin=0, sel_alu=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=3, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_main=4, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=4, sel_abl=4)

    # ROL-ABS,X
    elif r_ir == 0x3E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=1, sel_cin=1, sel_alu=0, sel_abh=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=1, sel_ain=2, sel_bin=0)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_rw=0, sel_st=1, en_p=0x83, sel_p=2, sel_main=0, sel_cin=2, sel_alu=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_abh=4, sel_abl=4)

    # illegal opcodes
    elif r_ir == 0x3F:
        pass

    # ---------- Default ----------
    if ctrl_signals is None:
        ctrl_signals = ctrl_t()

    return ctrl_signals
