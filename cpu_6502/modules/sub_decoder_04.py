from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_04(i_decoder):
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage

    # ---------- MEM2MEM ----------
    #109 ASL-ABSOLUTE[=0Eh]
    if r_ir == 0x0E:
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

    #110 ASL-ZEROPAGE[=06h]
    elif r_ir == 0x06:
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

    #111 ASL-ACCUM[=0Ah]
    elif r_ir == 0x0A:
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

    #112 DEC-ABSOLUTE[=CEh]
    elif r_ir == 0xCE:
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

    #113 DEC-ZEROPAGE[=C6h]
    elif r_ir == 0xC6:
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

    #114 DEC-ZPG,X[=D6h]
    elif r_ir == 0xD6:
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

    #115 DEC-ABS,X[=DEh]
    elif r_ir == 0xDE:
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

    #116 INC-ABSOLUTE[=EEh]
    elif r_ir == 0xEE:
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

    #117 INC-ZEROPAGE[=E6h]
    elif r_ir == 0xE6:
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

    #118 INC-ZPG,X[=F6h]
    elif r_ir == 0xF6:
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

    #119 INC-ABS,X[=FEh]
    elif r_ir == 0xFE:
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

    #120 LSR-ABSOLUTE[=4Eh]
    elif r_ir == 0x4E:
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

    #121 LSR-ZEROPAGE[=46h]
    elif r_ir == 0x46:
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

    #122 LSR-ACCUM[=4Ah]
    elif r_ir == 0x4A:
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

    #123 LSR-ZPG,X[=56h]
    elif r_ir == 0x56:
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

    #124 LSR-ABS,X[=5Eh]
    elif r_ir == 0x5E:
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

    #125 ROL-ABSOLUTE[=2Eh]
    elif r_ir == 0x2E:
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

    #126 ROL-ZEROPAGE[=26h]
    elif r_ir == 0x26:
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

    #127 ROL-ACCUM[=2Ah]
    elif r_ir == 0x2A:
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

    #128 ROL-ZPG,X[=36h]
    elif r_ir == 0x36:
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

    #129 ROL-ABS,X[=3Eh]
    elif r_ir == 0x3E:
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

    #130 ROR-ABSOLUTE[=6Eh]
    elif r_ir == 0x6E:
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

    #131 ROR-ZEROPAGE[=66h]
    elif r_ir == 0x66:
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

    #132 ROR-ACCUM[=6Ah]
    elif r_ir == 0x6A:
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

    #133 ROR-ZPG,X[=76h]
    elif r_ir == 0x76:
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

    #134 ROR-ABS,X[=7Eh]
    elif r_ir == 0x7E:
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
