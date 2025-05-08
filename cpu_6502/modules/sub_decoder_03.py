from cpu_6502.modules.utils import stage_e, ctrl_t

def sub_decoder_03(i_decoder):
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage

    # ---------- MEM2REG ----------
    #35 ADC-IMMEDIATE[=69h]
    if r_ir == 0x69:
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

    #36 ADC-ABSOLUTE[=6Dh]
    elif r_ir == 0x6D:
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

    #37 ADC-ZEROPAGE[=65h]
    elif r_ir == 0x65:
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

    #38 ADC-(IND,X)[=61h]
    elif r_ir == 0x61:
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

    #39 ADC-(IND),Y[=71h]
    elif r_ir == 0x71:
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

    #40 ADC-ZPG,X[=75h]
    elif r_ir == 0x75:
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

    #41 ADC-ABS,X[=7Dh]
    elif r_ir == 0x7D:
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

    #42 ADC-ABS,Y[=79h]
    elif r_ir == 0x79:
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

    #43 AND-IMMEDIATE[=29h]
    elif r_ir == 0x29:
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

    #44 AND-ABSOLUTE[=2Dh]
    elif r_ir == 0x2D:
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

    #45 AND-ZEROPAGE[=25h]
    elif r_ir == 0x25:
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

    #46 AND-(IND,X)[=21h]
    elif r_ir == 0x21:
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

    #47 AND-(IND),Y[=31h]
    elif r_ir == 0x31:
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

    #48 AND-ZPG,X[=35h]
    elif r_ir == 0x35:
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

    #49 AND-ABS,X[=3Dh]
    elif r_ir == 0x3D:
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

    #50 AND-ABS,Y[=39h]
    elif r_ir == 0x39:
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

    #51 BIT-ABSOLUTE[=2Ch]
    elif r_ir == 0x2C:
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

    #52 BIT-ZEROPAGE[=24h]
    elif r_ir == 0x24:
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

    #53 CMP-IMMEDIATE[=C9h]
    elif r_ir == 0xC9:
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

    #54 CMP-ABSOLUTE[=CDh]
    elif r_ir == 0xCD:
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

    #55 CMP-ZEROPAGE[=C5h]
    elif r_ir == 0xC5:
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

    #56 CMP-(IND,X)[=C1h]
    elif r_ir == 0xC1:
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

    #57 CMP-(IND),Y[=D1h]
    elif r_ir == 0xD1:
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

    #58 CMP-ZPG,X[=D5h]
    elif r_ir == 0xD5:
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

    #59 CMP-ABS,X[=DDh]
    elif r_ir == 0xDD:
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

    #60 CMP-ABS,Y[=D9h]
    elif r_ir == 0xD9:
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

    #61 CPX-IMMEDIATE[=E0h]
    elif r_ir == 0xE0:
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

    #62 CPX-ABSOLUTE[=ECh]
    elif r_ir == 0xEC:
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

    #63 CPX-ZEROPAGE[=E4h]
    elif r_ir == 0xE4:
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

    #64 CPY-IMMEDIATE[=C0h]
    elif r_ir == 0xC0:
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

    #65 CPY-ABSOLUTE[=CCh]
    elif r_ir == 0xCC:
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

    #66 CPY-ZEROPAGE[=C4h]
    elif r_ir == 0xC4:
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

    #67 EOR-IMMEDIATE[=49h]
    elif r_ir == 0x49:
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

    #68 EOR-ABSOLUTE[=4Dh]
    elif r_ir == 0x4D:
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

    #69 EOR-ZEROPAGE[=45h]
    elif r_ir == 0x45:
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

    #70 EOR-(IND,X)[=41h]
    elif r_ir == 0x41:
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

    #71 EOR-(IND),Y[=51h]
    elif r_ir == 0x51:
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

    #72 EOR-ZPG,X[=55h]
    elif r_ir == 0x55:
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

    #73 EOR-ABS,X[=5Dh]
    elif r_ir == 0x5D:
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

    #74 EOR-ABS,Y[=59h]
    elif r_ir == 0x59:
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

    #75 LDA-IMMEDIATE[=A9h]
    elif r_ir == 0xA9:
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

    #76 LDA-ABSOLUTE[=ADh]
    elif r_ir == 0xAD:
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

    #77 LDA-ZEROPAGE[=A5h]
    elif r_ir == 0xA5:
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

    #78 LDA-(IND,X)[=A1h]
    elif r_ir == 0xA1:
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

    #79 LDA-(IND),Y[=B1h]
    elif r_ir == 0xB1:
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

    #80 LDA-ZPG,X[=B5h]
    elif r_ir == 0xB5:
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

    #81 LDA-ABS,X[=BDh]
    elif r_ir == 0xBD:
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

    #82 LDA-ABS,Y[=B9h]
    elif r_ir == 0xB9:
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

    #83 LDX-IMMEDIATE[=A2h]
    elif r_ir == 0xA2:
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

    #84 LDX-ABSOLUTE[=AEh]
    elif r_ir == 0xAE:
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

    #85 LDX-ZEROPAGE[=A6h]
    elif r_ir == 0xA6:
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

    #86 LDX-ABS,Y[=BEh]
    elif r_ir == 0xBE:
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

    #87 LDX-ZPG,Y[=B6h]
    elif r_ir == 0xB6:
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

    #88 LDY-IMMEDIATE[=A0h]
    elif r_ir == 0xA0:
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

    #89 LDY-ABSOLUTE[=ACh]
    elif r_ir == 0xAC:
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

    #90 LDY-ZEROPAGE[=A4h]
    elif r_ir == 0xA4:
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

    #91 LDY-ZPG,X[=B4h]
    elif r_ir == 0xB4:
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

    #92 LDY-ABS,X[=BCh]
    elif r_ir == 0xBC:
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

    #93 ORA-IMMEDIATE[=09h]
    elif r_ir == 0x09:
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

    #94 ORA-ABSOLUTE[=0Dh]
    elif r_ir == 0x0D:
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

    #95 ORA-ZEROPAGE[=05h]
    elif r_ir == 0x05:
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

    #96 ORA-(IND,X)[=01h]
    elif r_ir == 0x01:
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

    #97 ORA-(IND),Y[=11h]
    elif r_ir == 0x11:
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

    #98 ORA-ZPG,X[=15h]
    elif r_ir == 0x15:
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

    #99 ORA-ABS,X[=1Dh]
    elif r_ir == 0x1D:
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

    #100 ORA-ABS,Y[=19h]
    elif r_ir == 0x19:
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

    #101 SBC-IMMEDIATE[=E9h]
    elif r_ir == 0xE9:
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

    #102 SBC-ABSOLUTE[=EDh]
    elif r_ir == 0xED:
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

    #103 SBC-ZEROPAGE[=E5h]
    elif r_ir == 0xE5:
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

    #104 SBC-(IND,X)[=E1h]
    elif r_ir == 0xE1:
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

    #105 SBC-(IND),Y[=F1h]
    elif r_ir == 0xF1:
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

    #106 SBC-ZPG,X[=F5h]
    elif r_ir == 0xF5:
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

    #107 SBC-ABS,X[=FDh]
    elif r_ir == 0xFD:
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

    #108 SBC-ABS,Y[=F9h]
    elif r_ir == 0xF9:
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
