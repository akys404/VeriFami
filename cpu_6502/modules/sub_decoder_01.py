from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_01(i_decoder):
    r_res = i_decoder.r_res
    r_nmi = i_decoder.r_nmi
    r_irq = i_decoder.r_irq
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage

    # ---------- Exception ----------
    #01 RESET
    if r_res == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_abh=3, sel_abl=3)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=3, sel_abl=4)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_st=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7, sel_pch=2, sel_pcl=2)

    #02 NMI
    elif r_nmi == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=6, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=2, sel_abl=0xB)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=0, sel_main=7, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=2, sel_abl=7)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=0, sel_b=0, sel_main=8, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=2, sel_abl=7)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=0, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=1)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_st=1, en_p=0x04, sel_p=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=3, sel_abl=2)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_st=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7, sel_pch=2, sel_pcl=2)

    #03 IRQ
    elif r_irq == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=6, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=2, sel_abl=0xB)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(o_rw=0, sel_main=7, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=2, sel_abl=7)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(o_rw=0, sel_b=0, sel_main=8, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=2, sel_abl=7)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(o_rw=0, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=5)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_st=1, en_p=0x04, sel_p=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=3, sel_abl=6)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_st=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7, sel_pch=2, sel_pcl=2)

    # ---------- REG2REG ----------
    #04 CLC-IMPLIED[=18h]
    elif r_ir == 0x18:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x01, sel_p=0, sel_abh=6, sel_abl=9)

    #05 CLD-IMPLIED[=D8h]
    elif r_ir == 0xD8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x08, sel_p=0, sel_abh=6, sel_abl=9)

    #06 CLI-IMPLIED[=58h]
    elif r_ir == 0x58:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x04, sel_p=0, sel_abh=6, sel_abl=9)

    #07 CLV-IMPLIED[=B8h]
    elif r_ir == 0xB8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x40, sel_p=0, sel_abh=6, sel_abl=9)

    #08 DEX-IMPLIED[=CAh]
    elif r_ir == 0xCA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_x=1, sel_cin=0, sel_alu=0, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, sel_main=2, sel_ain=2, sel_bin=1, sel_abh=6, sel_abl=9)

    #09 DEY-IMPLIED[=88h]
    elif r_ir == 0x88:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_y=1, sel_cin=0, sel_alu=0, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, sel_main=3, sel_ain=2, sel_bin=1, sel_abh=6, sel_abl=9)

    #10 INX-IMPLIED[=E8h]
    elif r_ir == 0xE8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_x=1, sel_cin=1, sel_alu=0, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, sel_main=2, sel_ain=2, sel_bin=0, sel_abh=6, sel_abl=9)

    #11 INY-IMPLIED[=C8h]
    elif r_ir == 0xC8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, en_p=0x82, sel_p=2, sel_main=0, en_y=1, sel_cin=1, sel_alu=0, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, sel_main=3, sel_ain=2, sel_bin=0, sel_abh=6, sel_abl=9)

    #12 NOP-IMPLIED[=EAh]
    elif r_ir == 0xEA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, sel_abh=6, sel_abl=9)

    #13 SEC-IMPLIED[=38h]
    elif r_ir == 0x38:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x01, sel_p=1, sel_abh=6, sel_abl=9)

    #14 SED-IMPLIED[=F8h]
    elif r_ir == 0xF8:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x04, sel_p=1, sel_abh=6, sel_abl=9)

    #15 SEI-IMPLIED[=78h]
    elif r_ir == 0x78:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x04, sel_p=1, sel_abh=6, sel_abl=9)

    #16 TAX-IMPLIED[=AAh]
    elif r_ir == 0xAA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x82, sel_p=2, sel_main=4, en_x=1, sel_abh=6, sel_abl=9)

    #17 TAY-IMPLIED[=ABh]
    elif r_ir == 0xAB:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x82, sel_p=2, sel_main=4, en_y=1, sel_abh=6, sel_abl=9)

    #18 TSX-IMPLIED[=BAh]
    elif r_ir == 0xBA:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x82, sel_p=2, sel_main=5, en_x=1, sel_abh=6, sel_abl=9)

    #19 TXA-IMPLIED[=8Ah]
    elif r_ir == 0x8A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x82, sel_p=2, sel_main=2, en_a=1, sel_abh=6, sel_abl=9)

    #20 TXS-IMPLIED[=9Ah]
    elif r_ir == 0x9A:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x82, sel_p=2, sel_main=2, en_sp=1, sel_abh=6, sel_abl=9)

    #21 TYA-IMPLIED[=9Bh]
    elif r_ir == 0x9B:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, en_p=0x82, sel_p=2, sel_main=2, en_a=1, sel_abh=6, sel_abl=9)

    # ---------- Default ----------
    else:
        ctrl_signals = ctrl_t()
        print('Undefined instruction')
    
    return ctrl_signals
