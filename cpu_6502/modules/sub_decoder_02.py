from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_02(i_decoder):
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage
    r_cout_old = i_decoder.r_cout_old


    # ---------- REG2MEM ----------
    #22 STA-ABSOLUTE[=8Dh]
    if r_ir == 0x8D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #23 STA-ZEROPAGE[=85h]
    elif r_ir == 0x85:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_abh=1, sel_abl=8, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #24 STA-(IND,X)[=81h]
    elif r_ir == 0x81:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_sub=0, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=1, sel_abl=7)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=1, sel_abl=7)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #25 STA-(IND),Y[=91h]
    elif r_ir == 0x91:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=1, sel_abl=8, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_cin=1, sel_alu=0, sel_abh=1, sel_abl=7)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7)
        elif r_stage == stage_e.T5 and r_cout_old == False:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=0)
        elif r_stage == stage_e.T5 and r_cout_old == True:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=4)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #26 STA-ZPG,X[=95h]
    elif r_ir == 0x95:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=0, sel_alu=0, sel_abh=1, sel_abl=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #27 STA-ABS,X[=9Dh]
    elif r_ir == 0x9D:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7)
        elif r_stage == stage_e.T4 and r_cout_old == False:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=0)
        elif r_stage == stage_e.T4 and r_cout_old == True:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=4)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #28 STA-ABS,Y[=99h]
    elif r_ir == 0x99:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7)
        elif r_stage == stage_e.T4 and r_cout_old == False:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=0)
        elif r_stage == stage_e.T4 and r_cout_old == True:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=4, sel_cin=1, sel_alu=0, sel_abh=4)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #29 STX-ABSOLUTE[=8Eh]
    elif r_ir == 0x8E:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=2, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #30 STX-ZEROPAGE[=86h]
    elif r_ir == 0x86:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=2, sel_abh=1, sel_abl=8, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #31 STX-ZPG,Y[=96h]
    elif r_ir == 0x96:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=3, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=2, sel_cin=0, sel_alu=0, sel_abh=1, sel_abl=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #32 STY-ABSOLUTE[=8Ch]
    elif r_ir == 0x8C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=3, sel_cin=0, sel_alu=0, sel_abh=5, sel_abl=7, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #33 STY-ZEROPAGE[=84h]
    elif r_ir == 0x84:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=3, sel_abh=1, sel_abl=8, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    #34 STY-ZPG,X[=94h]
    elif r_ir == 0x94:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_main=2, sel_sub=1, sel_ain=2, sel_bin=2, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_st=1, sel_main=3, sel_cin=0, sel_alu=0, sel_abh=1, sel_abl=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(o_rw=0, sel_st=2, sel_abh=6, sel_abl=9)

    # ---------- Default ----------
    else:
        ctrl_signals = ctrl_t()
        print('Undefined instruction')
    
    return ctrl_signals
