from cpu_6502.modules.utils import stage_e, ctrl_t

def decoder(i_decoder):
    r_res = i_decoder.r_res
    r_nmi = i_decoder.r_nmi
    r_irq = i_decoder.r_irq
    r_ir = i_decoder.r_ir
    r_stage = i_decoder.r_stage
    r_p = i_decoder.r_p
    r_ain = i_decoder.r_ain

    # ---------- Exception ----------
    #01 RESET
    if r_res == True:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)
        elif r_stage == stage_e.T2:
            ctrl_signals = ctrl_t(sel_st=2, sel_main=2, sel_ain=2, sel_bin=0, sel_abh=6, sel_abl=9)

    #02 NMI
    elif r_nmi == True:
        ctrl_signals = ctrl_t()

    #03 IRQ
    elif r_irq == True:
        ctrl_signals = ctrl_t()

    # ---------- REG2REG ----------
    #04 CLC-IMPLIED[=18h]
    elif r_ir == 0x18:
        ctrl_signals = ctrl_t()

    #05 CLD-IMPLIED[=D8h]
    elif r_ir == 0xD8:
        ctrl_signals = ctrl_t()

    #06 CLI-IMPLIED[=58h]
    elif r_ir == 0x58:
        ctrl_signals = ctrl_t()

    #07 CLV-IMPLIED[=B8h]
    elif r_ir == 0xB8:
        ctrl_signals = ctrl_t()

    #08 DEX-IMPLIED[=CAh]
    elif r_ir == 0xCA:
        ctrl_signals = ctrl_t()

    #09 DEY-IMPLIED[=88h]
    elif r_ir == 0x88:
        ctrl_signals = ctrl_t()

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
        ctrl_signals = ctrl_t()

    #13 SEC-IMPLIED[=38h]
    elif r_ir == 0x38:
        ctrl_signals = ctrl_t()

    #14 SED-IMPLIED[=F8h]
    elif r_ir == 0xF8:
        ctrl_signals = ctrl_t()

    #15 SEI-IMPLIED[=78h]
    elif r_ir == 0x78:
        ctrl_signals = ctrl_t()

    #16 TAX-IMPLIED[=AAh]
    elif r_ir == 0xAA:
        ctrl_signals = ctrl_t()

    #17 TAY-IMPLIED[=ABh]
    elif r_ir == 0xAB:
        ctrl_signals = ctrl_t()

    #18 TSX-IMPLIED[=BAh]
    elif r_ir == 0xBA:
        ctrl_signals = ctrl_t()

    #19 TXA-IMPLIED[=8Ah]
    elif r_ir == 0x8A:
        ctrl_signals = ctrl_t()

    #20 TXS-IMPLIED[=9Ah]
    elif r_ir == 0x9A:
        ctrl_signals = ctrl_t()

    #21 TYA-IMPLIED[=9Bh]
    elif r_ir == 0x9B:
        ctrl_signals = ctrl_t()

    # ---------- REG2MEM ----------
    #22 STA-ABSOLUTE[=8Dh]
    elif r_ir == 0x8D:
        ctrl_signals = ctrl_t()

    #23 STA-ZEROPAGE[=85h]
    elif r_ir == 0x85:
        ctrl_signals = ctrl_t()

    #24 STA-(IND,X)[=81h]
    elif r_ir == 0x81:
        ctrl_signals = ctrl_t()

    #25 STA-(IND),Y[=91h]
    elif r_ir == 0x91:
        ctrl_signals = ctrl_t()

    #26 STA-ZPG,X[=95h]
    elif r_ir == 0x95:
        ctrl_signals = ctrl_t()

    #27 STA-ABS,X[=9Dh]
    elif r_ir == 0x9D:
        ctrl_signals = ctrl_t()

    #28 STA-ABS,Y[=99h]
    elif r_ir == 0x99:
        ctrl_signals = ctrl_t()

    #29 STX-ABSOLUTE[=8Eh]
    elif r_ir == 0x8E:
        ctrl_signals = ctrl_t()

    #30 STX-ZEROPAGE[=86h]
    elif r_ir == 0x86:
        ctrl_signals = ctrl_t()

    #31 STX-ZPG,Y[=96h]
    elif r_ir == 0x96:
        ctrl_signals = ctrl_t()

    #32 STY-ABSOLUTE[=8Ch]
    elif r_ir == 0x8C:
        ctrl_signals = ctrl_t()

    #33 STY-ZEROPAGE[=84h]
    elif r_ir == 0x84:
        ctrl_signals = ctrl_t()

    #34 STY-ZPG,X[=94h]
    elif r_ir == 0x94:
        ctrl_signals = ctrl_t()

    # ---------- MEM2REG ----------
    #35 ADC-IMMEDIATE[=69h]
    elif r_ir == 0x69:
        ctrl_signals = ctrl_t()

    #36 ADC-ABSOLUTE[=6Dh]
    elif r_ir == 0x6D:
        ctrl_signals = ctrl_t()

    #37 ADC-ZEROPAGE[=65h]
    elif r_ir == 0x65:
        ctrl_signals = ctrl_t()

    #38 ADC-(IND,X)[=61h]
    elif r_ir == 0x61:
        ctrl_signals = ctrl_t()

    #39 ADC-(IND),Y[=71h]
    elif r_ir == 0x71:
        ctrl_signals = ctrl_t()

    #40 ADC-ZPG,X[=75h]
    elif r_ir == 0x75:
        ctrl_signals = ctrl_t()

    #41 ADC-ABS,X[=7Dh]
    elif r_ir == 0x7D:
        ctrl_signals = ctrl_t()

    #42 ADC-ABS,Y[=79h]
    elif r_ir == 0x79:
        ctrl_signals = ctrl_t()

    #43 AND-IMMEDIATE[=29h]
    elif r_ir == 0x29:
        ctrl_signals = ctrl_t()

    #44 AND-ABSOLUTE[=2Dh]
    elif r_ir == 0x2D:
        ctrl_signals = ctrl_t()

    #45 AND-ZEROPAGE[=25h]
    elif r_ir == 0x25:
        ctrl_signals = ctrl_t()

    #46 AND-(IND,X)[=21h]
    elif r_ir == 0x21:
        ctrl_signals = ctrl_t()

    #47 AND-(IND),Y[=31h]
    elif r_ir == 0x31:
        ctrl_signals = ctrl_t()

    #48 AND-ZPG,X[=35h]
    elif r_ir == 0x35:
        ctrl_signals = ctrl_t()

    #49 AND-ABS,X[=3Dh]
    elif r_ir == 0x3D:
        ctrl_signals = ctrl_t()

    #50 AND-ABS,Y[=39h]
    elif r_ir == 0x39:
        ctrl_signals = ctrl_t()

    #51 BIT-ABSOLUTE[=2Ch]
    elif r_ir == 0x2C:
        ctrl_signals = ctrl_t()

    #52 BIT-ZEROPAGE[=24h]
    elif r_ir == 0x24:
        ctrl_signals = ctrl_t()

    #53 CMP-IMMEDIATE[=C9h]
    elif r_ir == 0xC9:
        ctrl_signals = ctrl_t()

    #54 CMP-ABSOLUTE[=CDh]
    elif r_ir == 0xCD:
        ctrl_signals = ctrl_t()

    #55 CMP-ZEROPAGE[=C5h]
    elif r_ir == 0xC5:
        ctrl_signals = ctrl_t()

    #56 CMP-(IND,X)[=C1h]
    elif r_ir == 0xC1:
        ctrl_signals = ctrl_t()

    #57 CMP-(IND),Y[=D1h]
    elif r_ir == 0xD1:
        ctrl_signals = ctrl_t()

    #58 CMP-ZPG,X[=D5h]
    elif r_ir == 0xD5:
        ctrl_signals = ctrl_t()

    #59 CMP-ABS,X[=DDh]
    elif r_ir == 0xDD:
        ctrl_signals = ctrl_t()

    #60 CMP-ABS,Y[=D9h]
    elif r_ir == 0xD9:
        ctrl_signals = ctrl_t()

    #61 CPX-IMMEDIATE[=E0h]
    elif r_ir == 0xE0:
        ctrl_signals = ctrl_t()

    #62 CPX-ABSOLUTE[=ECh]
    elif r_ir == 0xEC:
        ctrl_signals = ctrl_t()

    #63 CPX-ZEROPAGE[=E4h]
    elif r_ir == 0xE4:
        ctrl_signals = ctrl_t()

    #64 CPY-IMMEDIATE[=C0h]
    elif r_ir == 0xC0:
        ctrl_signals = ctrl_t()

    #65 CPY-ABSOLUTE[=CCh]
    elif r_ir == 0xCC:
        ctrl_signals = ctrl_t()

    #66 CPY-ZEROPAGE[=C4h]
    elif r_ir == 0xC4:
        ctrl_signals = ctrl_t()

    #67 EOR-IMMEDIATE[=49h]
    elif r_ir == 0x49:
        ctrl_signals = ctrl_t()

    #68 EOR-ABSOLUTE[=4Dh]
    elif r_ir == 0x4D:
        ctrl_signals = ctrl_t()

    #69 EOR-ZEROPAGE[=45h]
    elif r_ir == 0x45:
        ctrl_signals = ctrl_t()

    #70 EOR-(IND,X)[=41h]
    elif r_ir == 0x41:
        ctrl_signals = ctrl_t()

    #71 EOR-(IND),Y[=51h]
    elif r_ir == 0x51:
        ctrl_signals = ctrl_t()

    #72 EOR-ZPG,X[=55h]
    elif r_ir == 0x55:
        ctrl_signals = ctrl_t()

    #73 EOR-ABS,X[=5Dh]
    elif r_ir == 0x5D:
        ctrl_signals = ctrl_t()

    #74 EOR-ABS,Y[=59h]
    elif r_ir == 0x59:
        ctrl_signals = ctrl_t()

    #75 LDA-IMMEDIATE[=A9h]
    elif r_ir == 0xA9:
        ctrl_signals = ctrl_t()

    #76 LDA-ABSOLUTE[=ADh]
    elif r_ir == 0xAD:
        ctrl_signals = ctrl_t()

    #77 LDA-ZEROPAGE[=A5h]
    elif r_ir == 0xA5:
        ctrl_signals = ctrl_t()

    #78 LDA-(IND,X)[=A1h]
    elif r_ir == 0xA1:
        ctrl_signals = ctrl_t()

    #79 LDA-(IND),Y[=B1h]
    elif r_ir == 0xB1:
        ctrl_signals = ctrl_t()

    #80 LDA-ZPG,X[=B5h]
    elif r_ir == 0xB5:
        ctrl_signals = ctrl_t()

    #81 LDA-ABS,X[=BDh]
    elif r_ir == 0xBD:
        ctrl_signals = ctrl_t()

    #82 LDA-ABS,Y[=B9h]
    elif r_ir == 0xB9:
        ctrl_signals = ctrl_t()

    #83 LDX-IMMEDIATE[=A2h]
    elif r_ir == 0xA2:
        ctrl_signals = ctrl_t()

    #84 LDX-ABSOLUTE[=AEh]
    elif r_ir == 0xAE:
        ctrl_signals = ctrl_t()

    #85 LDX-ZEROPAGE[=A6h]
    elif r_ir == 0xA6:
        ctrl_signals = ctrl_t()

    #86 LDX-ABS,Y[=BEh]
    elif r_ir == 0xBE:
        ctrl_signals = ctrl_t()

    #87 LDX-ZPG,Y[=B6h]
    elif r_ir == 0xB6:
        ctrl_signals = ctrl_t()

    #88 LDY-IMMEDIATE[=A0h]
    elif r_ir == 0xA0:
        ctrl_signals = ctrl_t()

    #89 LDY-ABSOLUTE[=ACh]
    elif r_ir == 0xAC:
        ctrl_signals = ctrl_t()

    #90 LDY-ZEROPAGE[=A4h]
    elif r_ir == 0xA4:
        ctrl_signals = ctrl_t()

    #91 LDY-ZPG,X[=B4h]
    elif r_ir == 0xB4:
        ctrl_signals = ctrl_t()

    #92 LDY-ABS,X[=BCh]
    elif r_ir == 0xBC:
        ctrl_signals = ctrl_t()

    #93 ORA-IMMEDIATE[=09h]
    elif r_ir == 0x09:
        ctrl_signals = ctrl_t()

    #94 ORA-ABSOLUTE[=0Dh]
    elif r_ir == 0x0D:
        ctrl_signals = ctrl_t()

    #95 ORA-ZEROPAGE[=05h]
    elif r_ir == 0x05:
        ctrl_signals = ctrl_t()

    #96 ORA-(IND,X)[=01h]
    elif r_ir == 0x01:
        ctrl_signals = ctrl_t()

    #97 ORA-(IND),Y[=11h]
    elif r_ir == 0x11:
        ctrl_signals = ctrl_t()

    #98 ORA-ZPG,X[=15h]
    elif r_ir == 0x15:
        ctrl_signals = ctrl_t()

    #99 ORA-ABS,X[=1Dh]
    elif r_ir == 0x1D:
        ctrl_signals = ctrl_t()

    #100 ORA-ABS,Y[=19h]
    elif r_ir == 0x19:
        ctrl_signals = ctrl_t()

    #101 SBC-IMMEDIATE[=E9h]
    elif r_ir == 0xE9:
        ctrl_signals = ctrl_t()

    #102 SBC-ABSOLUTE[=EDh]
    elif r_ir == 0xED:
        ctrl_signals = ctrl_t()

    #103 SBC-ZEROPAGE[=E5h]
    elif r_ir == 0xE5:
        ctrl_signals = ctrl_t()

    #104 SBC-(IND,X)[=E1h]
    elif r_ir == 0xE1:
        ctrl_signals = ctrl_t()

    #105 SBC-(IND),Y[=F1h]
    elif r_ir == 0xF1:
        ctrl_signals = ctrl_t()

    #106 SBC-ZPG,X[=F5h]
    elif r_ir == 0xF5:
        ctrl_signals = ctrl_t()

    #107 SBC-ABS,X[=FDh]
    elif r_ir == 0xFD:
        ctrl_signals = ctrl_t()

    #108 SBC-ABS,Y[=F9h]
    elif r_ir == 0xF9:
        ctrl_signals = ctrl_t()

    # ---------- MEM2MEM ----------
    #109 ASL-ABSOLUTE[=0Eh]
    elif r_ir == 0x0E:
        ctrl_signals = ctrl_t()

    #110 ASL-ZEROPAGE[=06h]
    elif r_ir == 0x06:
        ctrl_signals = ctrl_t()

    #111 ASL-ACCUM[=0Ah]
    elif r_ir == 0x0A:
        ctrl_signals = ctrl_t()

    #112 DEC-ABSOLUTE[=CEh]
    elif r_ir == 0xCE:
        ctrl_signals = ctrl_t()

    #113 DEC-ZEROPAGE[=C6h]
    elif r_ir == 0xC6:
        ctrl_signals = ctrl_t()

    #114 DEC-ZPG,X[=D6h]
    elif r_ir == 0xD6:
        ctrl_signals = ctrl_t()

    #115 DEC-ABS,X[=DEh]
    elif r_ir == 0xDE:
        ctrl_signals = ctrl_t()

    #116 INC-ABSOLUTE[=EEh]
    elif r_ir == 0xEE:
        ctrl_signals = ctrl_t()

    #117 INC-ZEROPAGE[=E6h]
    elif r_ir == 0xE6:
        ctrl_signals = ctrl_t()

    #118 INC-ZPG,X[=F6h]
    elif r_ir == 0xF6:
        ctrl_signals = ctrl_t()

    #119 INC-ABS,X[=FEh]
    elif r_ir == 0xFE:
        ctrl_signals = ctrl_t()

    #120 LSR-ABSOLUTE[=4Eh]
    elif r_ir == 0x4E:
        ctrl_signals = ctrl_t()

    #121 LSR-ZEROPAGE[=46h]
    elif r_ir == 0x46:
        ctrl_signals = ctrl_t()

    #122 LSR-ACCUM[=4Ah]
    elif r_ir == 0x4A:
        ctrl_signals = ctrl_t()

    #123 LSR-ZPG,X[=56h]
    elif r_ir == 0x56:
        ctrl_signals = ctrl_t()

    #124 LSR-ABS,X[=5Eh]
    elif r_ir == 0x5E:
        ctrl_signals = ctrl_t()

    #125 ROL-ABSOLUTE[=2Eh]
    elif r_ir == 0x2E:
        ctrl_signals = ctrl_t()

    #126 ROL-ZEROPAGE[=26h]
    elif r_ir == 0x26:
        ctrl_signals = ctrl_t()

    #127 ROL-ACCUM[=2Ah]
    elif r_ir == 0x2A:
        ctrl_signals = ctrl_t()

    #128 ROL-ZPG,X[=36h]
    elif r_ir == 0x36:
        ctrl_signals = ctrl_t()

    #129 ROL-ABS,X[=3Eh]
    elif r_ir == 0x3E:
        ctrl_signals = ctrl_t()

    #130 ROR-ABSOLUTE[=6Eh]
    elif r_ir == 0x6E:
        ctrl_signals = ctrl_t()

    #131 ROR-ZEROPAGE[=66h]
    elif r_ir == 0x66:
        ctrl_signals = ctrl_t()

    #132 ROR-ACCUM[=6Ah]
    elif r_ir == 0x6A:
        ctrl_signals = ctrl_t()

    #133 ROR-ZPG,X[=76h]
    elif r_ir == 0x76:
        ctrl_signals = ctrl_t()

    #134 ROR-ABS,X[=7Eh]
    elif r_ir == 0x7E:
        ctrl_signals = ctrl_t()

    # ---------- Branch ----------
    #135 BVC-RELATIVE[=50h]
    elif r_ir == 0x50:
        ctrl_signals = ctrl_t()

    #136 BVS-RELATIVE[=70h]
    elif r_ir == 0x70:
        ctrl_signals = ctrl_t()

    #137 BCC-RELATIVE[=90h]
    elif r_ir == 0x90:
        ctrl_signals = ctrl_t()

    #138 BCS-RELATIVE[=B0h]
    elif r_ir == 0xB0:
        ctrl_signals = ctrl_t()

    #139 BEQ-RELATIVE[=F0h]
    elif r_ir == 0xF0:
        ctrl_signals = ctrl_t()

    #140 BMI-RELATIVE[=30h]
    elif r_ir == 0x30:
        ctrl_signals = ctrl_t()

    #141 BNE-RELATIVE[=D0h]
    elif r_ir == 0xD0:
        ctrl_signals = ctrl_t()

    #142 BPL-RELATIVE[=10h]
    elif r_ir == 0x10:
        ctrl_signals = ctrl_t()

    # ---------- Other ----------
    #143 BRK-IMPLIED[=00h]
    elif r_ir == 0x00:
        if r_stage == stage_e.T1:
            ctrl_signals = ctrl_t(en_ir=1, sel_abh=7, sel_abl=0xA, sel_pch=1, sel_pcl=1)

    #144 JMP-ABSOLUTE[=4Ch]
    elif r_ir == 0x4C:
        ctrl_signals = ctrl_t()

    #145 JMP-INDIRECT[=6Ch]
    elif r_ir == 0x6C:
        ctrl_signals = ctrl_t()

    #146 JSR-ABSOLUTE[=20h]
    elif r_ir == 0x20:
        ctrl_signals = ctrl_t()

    #147 PHA-IMPLIED[=48h]
    elif r_ir == 0x48:
        ctrl_signals = ctrl_t()

    #148 PHP-IMPLIED[=08h]
    elif r_ir == 0x08:
        ctrl_signals = ctrl_t()

    #149 PLA-IMPLIED[=68h]
    elif r_ir == 0x68:
        ctrl_signals = ctrl_t()

    #150 PLP-IMPLIED[=28h]
    elif r_ir == 0x28:
        ctrl_signals = ctrl_t()

    #151 RTI-IMPLIED[=40h]
    elif r_ir == 0x40:
        ctrl_signals = ctrl_t()

    #152 RTS-IMPLIED[=60h]
    elif r_ir == 0x60:
        ctrl_signals = ctrl_t()

    # ---------- Default ----------
    else:
        ctrl_signals = ctrl_t()
        print('Undefined instruction')
    
    return ctrl_signals
