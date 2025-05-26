from cpu_6502.modules.utils import stage_e, ctrl_t
from cpu_6502.modules.sub_decoder_00 import sub_decoder_00
from cpu_6502.modules.sub_decoder_01 import sub_decoder_01
from cpu_6502.modules.sub_decoder_10 import sub_decoder_10
from cpu_6502.modules.sub_decoder_11 import sub_decoder_11

def decoder(i_decoder):
    r_res = i_decoder.r_res
    r_nmi = i_decoder.r_nmi
    r_irq = i_decoder.r_irq
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage

    # ---------- Exception ----------
    # RESET
    if r_res == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2: 
            ctrl_signals = ctrl_t(sel_rw=1, sel_abh=7, sel_abl=8)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=9)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # NMI
    elif r_nmi == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2: 
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=6, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=7, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_b=0, sel_main=8, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=7, sel_abl=6)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, en_p=0x04, sel_p=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=7)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # IRQ
    elif r_irq == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(sel_rw=1, en_ir=1, sel_abh=1, sel_abl=1, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2: 
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=6, sel_sub=3, sel_ain=1, sel_bin=2, sel_abh=6, sel_abl=5)
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t(sel_rw=0, sel_main=7, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t(sel_rw=0, sel_b=0, sel_main=8, sel_sub=0, sel_ain=1, sel_bin=2, sel_cin=0, sel_alu=0, sel_abh=6, sel_abl=2)
        elif r_stage == stage_e.T5:
            ctrl_signals = ctrl_t(sel_rw=1, sel_main=0, en_sp=1, sel_cin=0, sel_alu=0, sel_abh=7, sel_abl=0xA)
        elif r_stage == stage_e.T6:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=1, en_p=0x04, sel_p=1, sel_sub=1, sel_ain=0, sel_bin=2, sel_abh=7, sel_abl=0xB)
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t(sel_rw=1, sel_st=2, sel_cin=0, sel_alu=0, sel_abh=3, sel_abl=2, sel_pch=3, sel_pcl=2)

    # 0x00 ~ 0x3F
    elif (r_ir >> 6) == 0b00:
        ctrl_signals = sub_decoder_00(r_ir, r_stage)

    # 0x40 ~ 0x7F
    elif (r_ir >> 6) == 0b01:
        ctrl_signals = sub_decoder_01(r_ir, r_stage)

    # 0x80 ~ 0xBF
    elif (r_ir >> 6) == 0b10:
        ctrl_signals = sub_decoder_10(r_ir, r_stage)

    # 0xC0 ~ 0xFF
    elif (r_ir >> 6) == 0b11:
        ctrl_signals = sub_decoder_11(r_ir, r_stage)
    
    return ctrl_signals
