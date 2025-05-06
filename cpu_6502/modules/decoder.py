from cpu_6502.modules.utils import stage_e, ctrl_t

def decoder(r_res, r_nmi, r_irq, r_ir, r_stage, r_p, r_ain):
    set_ctrl = {}
    # ---------- Exception ----------
    #01 RESET
    if r_res == True:
        if r_stage == stage_e.T1:
            set_ctrl = {'en_ir':1, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}
        elif r_stage == stage_e.T2:
            set_ctrl = {'sel_st':2, 'sel_main':2, 'sel_ain':2, 'sel_bin':0, 'sel_abh':6, 'sel_abl':9}

    #02 NMI
    elif r_nmi == True:
        pass

    #03 IRQ
    elif r_irq == True:
        pass

    # ---------- REG2REG ----------
    #04 CLC-IMPLIED[=18h]
    elif r_ir == 0x18:
        pass

    #05 CLD-IMPLIED[=D8h]
    elif r_ir == 0xD8:
        pass

    #06 CLI-IMPLIED[=58h]
    elif r_ir == 0x58:
        pass

    #07 CLV-IMPLIED[=B8h]
    elif r_ir == 0xB8:
        pass

    #08 DEX-IMPLIED[=CAh]
    elif r_ir == 0xCA:
        pass

    #09 DEY-IMPLIED[=88h]
    elif r_ir == 0x88:
        pass

    #10 INX-IMPLIED[=E8h]
    elif r_ir == 0xE8:
        if r_stage == stage_e.T1:
            set_ctrl = {'en_ir':1, 'en_p':0x82, 'sel_p':2, 'sel_main':0, 'en_x':1, 'sel_cin':1, 'sel_alu':0, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}
        elif r_stage == stage_e.T2:
            set_ctrl = {'sel_st':2, 'sel_main':2, 'sel_ain':2, 'sel_bin':0, 'sel_abh':6, 'sel_abl':9}

    #11 INY-IMPLIED[=C8h]
    elif r_ir == 0xC8:
        if r_stage == stage_e.T1:
            set_ctrl = {'en_ir':1, 'en_p':0x82, 'sel_p':2, 'sel_main':0, 'en_y':1, 'sel_cin':1, 'sel_alu':0, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}
        elif r_stage == stage_e.T2:
            set_ctrl = {'sel_st':2, 'sel_main':3, 'sel_ain':2, 'sel_bin':0, 'sel_abh':6, 'sel_abl':9}

    #12 NOP-IMPLIED[=EAh]
    elif r_ir == 0xEA:
        pass

    #13 SEC-IMPLIED[=38h]
    elif r_ir == 0x38:
        pass

    #14 SED-IMPLIED[=F8h]
    elif r_ir == 0xF8:
        pass

    #15 SEI-IMPLIED[=78h]
    elif r_ir == 0x78:
        pass

    #16 TAX-IMPLIED[=AAh]
    elif r_ir == 0xAA:
        pass

    #17 TAY-IMPLIED[=ABh]
    elif r_ir == 0xAB:
        pass

    #18 TSX-IMPLIED[=BAh]
    elif r_ir == 0xBA:
        pass

    #19 TXA-IMPLIED[=8Ah]
    elif r_ir == 0x8A:
        pass

    #20 TXS-IMPLIED[=9Ah]
    elif r_ir == 0x9A:
        pass

    #21 TYA-IMPLIED[=9Bh]
    elif r_ir == 0x9B:
        pass

    # ---------- REG2MEM ----------
    #22 STA-ABSOLUTE[=8Dh]
    elif r_ir == 0x8D:
        pass

    #23 STA-ZEROPAGE[=85h]
    elif r_ir == 0x85:
        pass

    #24 STA-(IND,X)[=81h]
    elif r_ir == 0x81:
        pass

    #25 STA-(IND),Y[=91h]
    elif r_ir == 0x91:
        pass

    #26 STA-ZPG,X[=95h]
    elif r_ir == 0x95:
        pass

    #27 STA-ABS,X[=9Dh]
    elif r_ir == 0x9D:
        pass

    #28 STA-ABS,Y[=99h]
    elif r_ir == 0x99:
        pass

    #29 STX-ABSOLUTE[=8Eh]
    elif r_ir == 0x8E:
        pass

    #30 STX-ZEROPAGE[=86h]
    elif r_ir == 0x86:
        pass

    #31 STX-ZPG,Y[=96h]
    elif r_ir == 0x96:
        pass

    #32 STY-ABSOLUTE[=8Ch]
    elif r_ir == 0x8C:
        pass

    #33 STY-ZEROPAGE[=84h]
    elif r_ir == 0x84:
        pass

    #34 STY-ZPG,X[=94h]
    elif r_ir == 0x94:
        pass

    # ---------- MEM2REG ----------
    #35 ADC-IMMEDIATE[=69h]
    elif r_ir == 0x69:
        pass

    #36 ADC-ABSOLUTE[=6Dh]
    elif r_ir == 0x6D:
        pass

    #37 ADC-ZEROPAGE[=65h]
    elif r_ir == 0x65:
        pass

    #38 ADC-(IND,X)[=61h]
    elif r_ir == 0x61:
        pass

    #39 ADC-(IND),Y[=71h]
    elif r_ir == 0x71:
        pass

    #40 ADC-ZPG,X[=75h]
    elif r_ir == 0x75:
        pass

    #41 ADC-ABS,X[=7Dh]
    elif r_ir == 0x7D:
        pass

    #42 ADC-ABS,Y[=79h]
    elif r_ir == 0x79:
        pass

    #43 AND-IMMEDIATE[=29h]
    elif r_ir == 0x29:
        pass

    #44 AND-ABSOLUTE[=2Dh]
    elif r_ir == 0x2D:
        pass

    #45 AND-ZEROPAGE[=25h]
    elif r_ir == 0x25:
        pass

    #46 AND-(IND,X)[=21h]
    elif r_ir == 0x21:
        pass

    #47 AND-(IND),Y[=31h]
    elif r_ir == 0x31:
        pass

    #48 AND-ZPG,X[=35h]
    elif r_ir == 0x35:
        pass

    #49 AND-ABS,X[=3Dh]
    elif r_ir == 0x3D:
        pass

    #50 AND-ABS,Y[=39h]
    elif r_ir == 0x39:
        pass

    #51 BIT-ABSOLUTE[=2Ch]
    elif r_ir == 0x2C:
        pass

    #52 BIT-ZEROPAGE[=24h]
    elif r_ir == 0x24:
        pass

    #53 CMP-IMMEDIATE[=C9h]
    elif r_ir == 0xC9:
        pass

    #54 CMP-ABSOLUTE[=CDh]
    elif r_ir == 0xCD:
        pass

    #55 CMP-ZEROPAGE[=C5h]
    elif r_ir == 0xC5:
        pass

    #56 CMP-(IND,X)[=C1h]
    elif r_ir == 0xC1:
        pass

    #57 CMP-(IND),Y[=D1h]
    elif r_ir == 0xD1:
        pass

    #58 CMP-ZPG,X[=D5h]
    elif r_ir == 0xD5:
        pass

    #59 CMP-ABS,X[=DDh]
    elif r_ir == 0xDD:
        pass

    #60 CMP-ABS,Y[=D9h]
    elif r_ir == 0xD9:
        pass

    #61 CPX-IMMEDIATE[=E0h]
    elif r_ir == 0xE0:
        pass

    #62 CPX-ABSOLUTE[=ECh]
    elif r_ir == 0xEC:
        pass

    #63 CPX-ZEROPAGE[=E4h]
    elif r_ir == 0xE4:
        pass

    #64 CPY-IMMEDIATE[=C0h]
    elif r_ir == 0xC0:
        pass

    #65 CPY-ABSOLUTE[=CCh]
    elif r_ir == 0xCC:
        pass

    #66 CPY-ZEROPAGE[=C4h]
    elif r_ir == 0xC4:
        pass

    #67 EOR-IMMEDIATE[=49h]
    elif r_ir == 0x49:
        pass

    #68 EOR-ABSOLUTE[=4Dh]
    elif r_ir == 0x4D:
        pass

    #69 EOR-ZEROPAGE[=45h]
    elif r_ir == 0x45:
        pass

    #70 EOR-(IND,X)[=41h]
    elif r_ir == 0x41:
        pass

    #71 EOR-(IND),Y[=51h]
    elif r_ir == 0x51:
        pass

    #72 EOR-ZPG,X[=55h]
    elif r_ir == 0x55:
        pass

    #73 EOR-ABS,X[=5Dh]
    elif r_ir == 0x5D:
        pass

    #74 EOR-ABS,Y[=59h]
    elif r_ir == 0x59:
        pass

    #75 LDA-IMMEDIATE[=A9h]
    elif r_ir == 0xA9:
        pass

    #76 LDA-ABSOLUTE[=ADh]
    elif r_ir == 0xAD:
        pass

    #77 LDA-ZEROPAGE[=A5h]
    elif r_ir == 0xA5:
        pass

    #78 LDA-(IND,X)[=A1h]
    elif r_ir == 0xA1:
        pass

    #79 LDA-(IND),Y[=B1h]
    elif r_ir == 0xB1:
        pass

    #80 LDA-ZPG,X[=B5h]
    elif r_ir == 0xB5:
        pass

    #81 LDA-ABS,X[=BDh]
    elif r_ir == 0xBD:
        pass

    #82 LDA-ABS,Y[=B9h]
    elif r_ir == 0xB9:
        pass

    #83 LDX-IMMEDIATE[=A2h]
    elif r_ir == 0xA2:
        pass

    #84 LDX-ABSOLUTE[=AEh]
    elif r_ir == 0xAE:
        pass

    #85 LDX-ZEROPAGE[=A6h]
    elif r_ir == 0xA6:
        pass

    #86 LDX-ABS,Y[=BEh]
    elif r_ir == 0xBE:
        pass

    #87 LDX-ZPG,Y[=B6h]
    elif r_ir == 0xB6:
        pass

    #88 LDY-IMMEDIATE[=A0h]
    elif r_ir == 0xA0:
        pass

    #89 LDY-ABSOLUTE[=ACh]
    elif r_ir == 0xAC:
        pass

    #90 LDY-ZEROPAGE[=A4h]
    elif r_ir == 0xA4:
        pass

    #91 LDY-ZPG,X[=B4h]
    elif r_ir == 0xB4:
        pass

    #92 LDY-ABS,X[=BCh]
    elif r_ir == 0xBC:
        pass

    #93 ORA-IMMEDIATE[=09h]
    elif r_ir == 0x09:
        pass

    #94 ORA-ABSOLUTE[=0Dh]
    elif r_ir == 0x0D:
        pass

    #95 ORA-ZEROPAGE[=05h]
    elif r_ir == 0x05:
        pass

    #96 ORA-(IND,X)[=01h]
    elif r_ir == 0x01:
        pass

    #97 ORA-(IND),Y[=11h]
    elif r_ir == 0x11:
        pass

    #98 ORA-ZPG,X[=15h]
    elif r_ir == 0x15:
        pass

    #99 ORA-ABS,X[=1Dh]
    elif r_ir == 0x1D:
        pass

    #100 ORA-ABS,Y[=19h]
    elif r_ir == 0x19:
        pass

    #101 SBC-IMMEDIATE[=E9h]
    elif r_ir == 0xE9:
        pass

    #102 SBC-ABSOLUTE[=EDh]
    elif r_ir == 0xED:
        pass

    #103 SBC-ZEROPAGE[=E5h]
    elif r_ir == 0xE5:
        pass

    #104 SBC-(IND,X)[=E1h]
    elif r_ir == 0xE1:
        pass

    #105 SBC-(IND),Y[=F1h]
    elif r_ir == 0xF1:
        pass

    #106 SBC-ZPG,X[=F5h]
    elif r_ir == 0xF5:
        pass

    #107 SBC-ABS,X[=FDh]
    elif r_ir == 0xFD:
        pass

    #108 SBC-ABS,Y[=F9h]
    elif r_ir == 0xF9:
        pass

    # ---------- MEM2MEM ----------
    #109 ASL-ABSOLUTE[=0Eh]
    elif r_ir == 0x0E:
        pass

    #110 ASL-ZEROPAGE[=06h]
    elif r_ir == 0x06:
        pass

    #111 ASL-ACCUM[=0Ah]
    elif r_ir == 0x0A:
        pass

    #112 DEC-ABSOLUTE[=CEh]
    elif r_ir == 0xCE:
        pass

    #113 DEC-ZEROPAGE[=C6h]
    elif r_ir == 0xC6:
        pass

    #114 DEC-ZPG,X[=D6h]
    elif r_ir == 0xD6:
        pass

    #115 DEC-ABS,X[=DEh]
    elif r_ir == 0xDE:
        pass

    #116 INC-ABSOLUTE[=EEh]
    elif r_ir == 0xEE:
        pass

    #117 INC-ZEROPAGE[=E6h]
    elif r_ir == 0xE6:
        pass

    #118 INC-ZPG,X[=F6h]
    elif r_ir == 0xF6:
        pass

    #119 INC-ABS,X[=FEh]
    elif r_ir == 0xFE:
        pass

    #120 LSR-ABSOLUTE[=4Eh]
    elif r_ir == 0x4E:
        pass

    #121 LSR-ZEROPAGE[=46h]
    elif r_ir == 0x46:
        pass

    #122 LSR-ACCUM[=4Ah]
    elif r_ir == 0x4A:
        pass

    #123 LSR-ZPG,X[=56h]
    elif r_ir == 0x56:
        pass

    #124 LSR-ABS,X[=5Eh]
    elif r_ir == 0x5E:
        pass

    #125 ROL-ABSOLUTE[=2Eh]
    elif r_ir == 0x2E:
        pass

    #126 ROL-ZEROPAGE[=26h]
    elif r_ir == 0x26:
        pass

    #127 ROL-ACCUM[=2Ah]
    elif r_ir == 0x2A:
        pass

    #128 ROL-ZPG,X[=36h]
    elif r_ir == 0x36:
        pass

    #129 ROL-ABS,X[=3Eh]
    elif r_ir == 0x3E:
        pass

    #130 ROR-ABSOLUTE[=6Eh]
    elif r_ir == 0x6E:
        pass

    #131 ROR-ZEROPAGE[=66h]
    elif r_ir == 0x66:
        pass

    #132 ROR-ACCUM[=6Ah]
    elif r_ir == 0x6A:
        pass

    #133 ROR-ZPG,X[=76h]
    elif r_ir == 0x76:
        pass

    #134 ROR-ABS,X[=7Eh]
    elif r_ir == 0x7E:
        pass

    # ---------- Branch ----------
    #135 BVC-RELATIVE[=50h]
    elif r_ir == 0x50:
        pass

    #136 BVS-RELATIVE[=70h]
    elif r_ir == 0x70:
        pass

    #137 BCC-RELATIVE[=90h]
    elif r_ir == 0x90:
        pass

    #138 BCS-RELATIVE[=B0h]
    elif r_ir == 0xB0:
        pass

    #139 BEQ-RELATIVE[=F0h]
    elif r_ir == 0xF0:
        pass

    #140 BMI-RELATIVE[=30h]
    elif r_ir == 0x30:
        pass

    #141 BNE-RELATIVE[=D0h]
    elif r_ir == 0xD0:
        pass

    #142 BPL-RELATIVE[=10h]
    elif r_ir == 0x10:
        pass

    # ---------- Other ----------
    #143 BRK-IMPLIED[=00h]
    elif r_ir == 0x00:
        if r_stage == stage_e.T1:
            set_ctrl = {'en_ir':1, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}

    #144 JMP-ABSOLUTE[=4Ch]
    elif r_ir == 0x4C:
        pass

    #145 JMP-INDIRECT[=6Ch]
    elif r_ir == 0x6C:
        pass

    #146 JSR-ABSOLUTE[=20h]
    elif r_ir == 0x20:
        pass

    #147 PHA-IMPLIED[=48h]
    elif r_ir == 0x48:
        pass

    #148 PHP-IMPLIED[=08h]
    elif r_ir == 0x08:
        pass

    #149 PLA-IMPLIED[=68h]
    elif r_ir == 0x68:
        pass

    #150 PLP-IMPLIED[=28h]
    elif r_ir == 0x28:
        pass

    #151 RTI-IMPLIED[=40h]
    elif r_ir == 0x40:
        pass

    #152 RTS-IMPLIED[=60h]
    elif r_ir == 0x60:
        pass

    # ---------- Default ----------
    else:
        print('Undefined instruction')
    
    ctrl_signals = ctrl_t()
    ctrl_signals.update(set_ctrl)

    return ctrl_signals
