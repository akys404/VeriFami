from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_05(i_decoder):
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage
    r_p = i_decoder.r_p
    r_ain = i_decoder.r_ain

    # ---------- Branch ----------
    #135 BVC-RELATIVE[=50h]
    if r_ir == 0x50:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #136 BVS-RELATIVE[=70h]
    elif r_ir == 0x70:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #137 BCC-RELATIVE[=90h]
    elif r_ir == 0x90:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #138 BCS-RELATIVE[=B0h]
    elif r_ir == 0xB0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #139 BEQ-RELATIVE[=F0h]
    elif r_ir == 0xF0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #140 BMI-RELATIVE[=30h]
    elif r_ir == 0x30:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #141 BNE-RELATIVE[=D0h]
    elif r_ir == 0xD0:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #142 BPL-RELATIVE[=10h]
    elif r_ir == 0x10:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    # ---------- Other ----------
    #143 BRK-IMPLIED[=00h]
    elif r_ir == 0x00:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)

    #144 JMP-ABSOLUTE[=4Ch]
    elif r_ir == 0x4C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #145 JMP-INDIRECT[=6Ch]
    elif r_ir == 0x6C:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #146 JSR-ABSOLUTE[=20h]
    elif r_ir == 0x20:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #147 PHA-IMPLIED[=48h]
    elif r_ir == 0x48:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #148 PHP-IMPLIED[=08h]
    elif r_ir == 0x08:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #149 PLA-IMPLIED[=68h]
    elif r_ir == 0x68:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #150 PLP-IMPLIED[=28h]
    elif r_ir == 0x28:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #151 RTI-IMPLIED[=40h]
    elif r_ir == 0x40:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    #152 RTS-IMPLIED[=60h]
    elif r_ir == 0x60:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T3:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T4:
            ctrl_signals = ctrl_t()
        elif r_stage == stage_e.T0:
            ctrl_signals = ctrl_t()

    # ---------- Default ----------
    else:
        ctrl_signals = ctrl_t()
        print('Undefined instruction')
    
    return ctrl_signals
