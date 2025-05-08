from cpu_6502.modules.utils import ctrl_t
from cpu_6502.modules.sub_decoder_01 import sub_decoder_01
from cpu_6502.modules.sub_decoder_02 import sub_decoder_02
from cpu_6502.modules.sub_decoder_03 import sub_decoder_03
from cpu_6502.modules.sub_decoder_04 import sub_decoder_04
from cpu_6502.modules.sub_decoder_05 import sub_decoder_05

def decoder(i_decoder):
    r_res = i_decoder.r_res
    r_nmi = i_decoder.r_nmi
    r_irq = i_decoder.r_irq
    r_ir = i_decoder.r_ir

    # ---------- Exception ----------
    #01 RESET
    if r_res == True:
        ctrl_signals = sub_decoder_01(i_decoder)
    #02 NMI
    elif r_nmi == True:
        ctrl_signals = sub_decoder_01(i_decoder)
    #03 IRQ
    elif r_irq == True:
        ctrl_signals = sub_decoder_01(i_decoder)

    # ---------- REG2REG ----------
    #04 CLC-IMPLIED[=18h]
    elif r_ir == 0x18:
        ctrl_signals = sub_decoder_01(i_decoder)

    #05 CLD-IMPLIED[=D8h]
    elif r_ir == 0xD8:
        ctrl_signals = sub_decoder_01(i_decoder)

    #06 CLI-IMPLIED[=58h]
    elif r_ir == 0x58:
        ctrl_signals = sub_decoder_01(i_decoder)

    #07 CLV-IMPLIED[=B8h]
    elif r_ir == 0xB8:
        ctrl_signals = sub_decoder_01(i_decoder)

    #08 DEX-IMPLIED[=CAh]
    elif r_ir == 0xCA:
        ctrl_signals = sub_decoder_01(i_decoder)

    #09 DEY-IMPLIED[=88h]
    elif r_ir == 0x88:
        ctrl_signals = sub_decoder_01(i_decoder)

    #10 INX-IMPLIED[=E8h]
    elif r_ir == 0xE8:
        ctrl_signals = sub_decoder_01(i_decoder)

    #11 INY-IMPLIED[=C8h]
    elif r_ir == 0xC8:
        ctrl_signals = sub_decoder_01(i_decoder)

    #12 NOP-IMPLIED[=EAh]
    elif r_ir == 0xEA:
        ctrl_signals = sub_decoder_01(i_decoder)

    #13 SEC-IMPLIED[=38h]
    elif r_ir == 0x38:
        ctrl_signals = sub_decoder_01(i_decoder)

    #14 SED-IMPLIED[=F8h]
    elif r_ir == 0xF8:
        ctrl_signals = sub_decoder_01(i_decoder)

    #15 SEI-IMPLIED[=78h]
    elif r_ir == 0x78:
        ctrl_signals = sub_decoder_01(i_decoder)

    #16 TAX-IMPLIED[=AAh]
    elif r_ir == 0xAA:
        ctrl_signals = sub_decoder_01(i_decoder)

    #17 TAY-IMPLIED[=ABh]
    elif r_ir == 0xAB:
        ctrl_signals = sub_decoder_01(i_decoder)

    #18 TSX-IMPLIED[=BAh]
    elif r_ir == 0xBA:
        ctrl_signals = sub_decoder_01(i_decoder)

    #19 TXA-IMPLIED[=8Ah]
    elif r_ir == 0x8A:
        ctrl_signals = sub_decoder_01(i_decoder)

    #20 TXS-IMPLIED[=9Ah]
    elif r_ir == 0x9A:
        ctrl_signals = sub_decoder_01(i_decoder)

    #21 TYA-IMPLIED[=9Bh]
    elif r_ir == 0x9B:
        ctrl_signals = sub_decoder_01(i_decoder)

    # ---------- REG2MEM ----------
    #22 STA-ABSOLUTE[=8Dh]
    elif r_ir == 0x8D:
        ctrl_signals = sub_decoder_02(i_decoder)

    #23 STA-ZEROPAGE[=85h]
    elif r_ir == 0x85:
        ctrl_signals = sub_decoder_02(i_decoder)

    #24 STA-(IND,X)[=81h]
    elif r_ir == 0x81:
        ctrl_signals = sub_decoder_02(i_decoder)

    #25 STA-(IND),Y[=91h]
    elif r_ir == 0x91:
        ctrl_signals = sub_decoder_02(i_decoder)

    #26 STA-ZPG,X[=95h]
    elif r_ir == 0x95:
        ctrl_signals = sub_decoder_02(i_decoder)

    #27 STA-ABS,X[=9Dh]
    elif r_ir == 0x9D:
        ctrl_signals = sub_decoder_02(i_decoder)

    #28 STA-ABS,Y[=99h]
    elif r_ir == 0x99:
        ctrl_signals = sub_decoder_02(i_decoder)

    #29 STX-ABSOLUTE[=8Eh]
    elif r_ir == 0x8E:
        ctrl_signals = sub_decoder_02(i_decoder)

    #30 STX-ZEROPAGE[=86h]
    elif r_ir == 0x86:
        ctrl_signals = sub_decoder_02(i_decoder)

    #31 STX-ZPG,Y[=96h]
    elif r_ir == 0x96:
        ctrl_signals = sub_decoder_02(i_decoder)

    #32 STY-ABSOLUTE[=8Ch]
    elif r_ir == 0x8C:
        ctrl_signals = sub_decoder_02(i_decoder)

    #33 STY-ZEROPAGE[=84h]
    elif r_ir == 0x84:
        ctrl_signals = sub_decoder_02(i_decoder)

    #34 STY-ZPG,X[=94h]
    elif r_ir == 0x94:
        ctrl_signals = sub_decoder_02(i_decoder)

    # ---------- MEM2REG ----------
    #35 ADC-IMMEDIATE[=69h]
    elif r_ir == 0x69:
        ctrl_signals = sub_decoder_03(i_decoder)

    #36 ADC-ABSOLUTE[=6Dh]
    elif r_ir == 0x6D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #37 ADC-ZEROPAGE[=65h]
    elif r_ir == 0x65:
        ctrl_signals = sub_decoder_03(i_decoder)

    #38 ADC-(IND,X)[=61h]
    elif r_ir == 0x61:
        ctrl_signals = sub_decoder_03(i_decoder)

    #39 ADC-(IND),Y[=71h]
    elif r_ir == 0x71:
        ctrl_signals = sub_decoder_03(i_decoder)

    #40 ADC-ZPG,X[=75h]
    elif r_ir == 0x75:
        ctrl_signals = sub_decoder_03(i_decoder)

    #41 ADC-ABS,X[=7Dh]
    elif r_ir == 0x7D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #42 ADC-ABS,Y[=79h]
    elif r_ir == 0x79:
        ctrl_signals = sub_decoder_03(i_decoder)

    #43 AND-IMMEDIATE[=29h]
    elif r_ir == 0x29:
        ctrl_signals = sub_decoder_03(i_decoder)

    #44 AND-ABSOLUTE[=2Dh]
    elif r_ir == 0x2D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #45 AND-ZEROPAGE[=25h]
    elif r_ir == 0x25:
        ctrl_signals = sub_decoder_03(i_decoder)

    #46 AND-(IND,X)[=21h]
    elif r_ir == 0x21:
        ctrl_signals = sub_decoder_03(i_decoder)

    #47 AND-(IND),Y[=31h]
    elif r_ir == 0x31:
        ctrl_signals = sub_decoder_03(i_decoder)

    #48 AND-ZPG,X[=35h]
    elif r_ir == 0x35:
        ctrl_signals = sub_decoder_03(i_decoder)

    #49 AND-ABS,X[=3Dh]
    elif r_ir == 0x3D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #50 AND-ABS,Y[=39h]
    elif r_ir == 0x39:
        ctrl_signals = sub_decoder_03(i_decoder)

    #51 BIT-ABSOLUTE[=2Ch]
    elif r_ir == 0x2C:
        ctrl_signals = sub_decoder_03(i_decoder)

    #52 BIT-ZEROPAGE[=24h]
    elif r_ir == 0x24:
        ctrl_signals = sub_decoder_03(i_decoder)

    #53 CMP-IMMEDIATE[=C9h]
    elif r_ir == 0xC9:
        ctrl_signals = sub_decoder_03(i_decoder)

    #54 CMP-ABSOLUTE[=CDh]
    elif r_ir == 0xCD:
        ctrl_signals = sub_decoder_03(i_decoder)

    #55 CMP-ZEROPAGE[=C5h]
    elif r_ir == 0xC5:
        ctrl_signals = sub_decoder_03(i_decoder)

    #56 CMP-(IND,X)[=C1h]
    elif r_ir == 0xC1:
        ctrl_signals = sub_decoder_03(i_decoder)

    #57 CMP-(IND),Y[=D1h]
    elif r_ir == 0xD1:
        ctrl_signals = sub_decoder_03(i_decoder)

    #58 CMP-ZPG,X[=D5h]
    elif r_ir == 0xD5:
        ctrl_signals = sub_decoder_03(i_decoder)

    #59 CMP-ABS,X[=DDh]
    elif r_ir == 0xDD:
        ctrl_signals = sub_decoder_03(i_decoder)

    #60 CMP-ABS,Y[=D9h]
    elif r_ir == 0xD9:
        ctrl_signals = sub_decoder_03(i_decoder)

    #61 CPX-IMMEDIATE[=E0h]
    elif r_ir == 0xE0:
        ctrl_signals = sub_decoder_03(i_decoder)

    #62 CPX-ABSOLUTE[=ECh]
    elif r_ir == 0xEC:
        ctrl_signals = sub_decoder_03(i_decoder)

    #63 CPX-ZEROPAGE[=E4h]
    elif r_ir == 0xE4:
        ctrl_signals = sub_decoder_03(i_decoder)

    #64 CPY-IMMEDIATE[=C0h]
    elif r_ir == 0xC0:
        ctrl_signals = sub_decoder_03(i_decoder)

    #65 CPY-ABSOLUTE[=CCh]
    elif r_ir == 0xCC:
        ctrl_signals = sub_decoder_03(i_decoder)

    #66 CPY-ZEROPAGE[=C4h]
    elif r_ir == 0xC4:
        ctrl_signals = sub_decoder_03(i_decoder)

    #67 EOR-IMMEDIATE[=49h]
    elif r_ir == 0x49:
        ctrl_signals = sub_decoder_03(i_decoder)

    #68 EOR-ABSOLUTE[=4Dh]
    elif r_ir == 0x4D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #69 EOR-ZEROPAGE[=45h]
    elif r_ir == 0x45:
        ctrl_signals = sub_decoder_03(i_decoder)

    #70 EOR-(IND,X)[=41h]
    elif r_ir == 0x41:
        ctrl_signals = sub_decoder_03(i_decoder)

    #71 EOR-(IND),Y[=51h]
    elif r_ir == 0x51:
        ctrl_signals = sub_decoder_03(i_decoder)

    #72 EOR-ZPG,X[=55h]
    elif r_ir == 0x55:
        ctrl_signals = sub_decoder_03(i_decoder)

    #73 EOR-ABS,X[=5Dh]
    elif r_ir == 0x5D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #74 EOR-ABS,Y[=59h]
    elif r_ir == 0x59:
        ctrl_signals = sub_decoder_03(i_decoder)

    #75 LDA-IMMEDIATE[=A9h]
    elif r_ir == 0xA9:
        ctrl_signals = sub_decoder_03(i_decoder)

    #76 LDA-ABSOLUTE[=ADh]
    elif r_ir == 0xAD:
        ctrl_signals = sub_decoder_03(i_decoder)

    #77 LDA-ZEROPAGE[=A5h]
    elif r_ir == 0xA5:
        ctrl_signals = sub_decoder_03(i_decoder)

    #78 LDA-(IND,X)[=A1h]
    elif r_ir == 0xA1:
        ctrl_signals = sub_decoder_03(i_decoder)

    #79 LDA-(IND),Y[=B1h]
    elif r_ir == 0xB1:
        ctrl_signals = sub_decoder_03(i_decoder)

    #80 LDA-ZPG,X[=B5h]
    elif r_ir == 0xB5:
        ctrl_signals = sub_decoder_03(i_decoder)

    #81 LDA-ABS,X[=BDh]
    elif r_ir == 0xBD:
        ctrl_signals = sub_decoder_03(i_decoder)

    #82 LDA-ABS,Y[=B9h]
    elif r_ir == 0xB9:
        ctrl_signals = sub_decoder_03(i_decoder)

    #83 LDX-IMMEDIATE[=A2h]
    elif r_ir == 0xA2:
        ctrl_signals = sub_decoder_03(i_decoder)

    #84 LDX-ABSOLUTE[=AEh]
    elif r_ir == 0xAE:
        ctrl_signals = sub_decoder_03(i_decoder)

    #85 LDX-ZEROPAGE[=A6h]
    elif r_ir == 0xA6:
        ctrl_signals = sub_decoder_03(i_decoder)

    #86 LDX-ABS,Y[=BEh]
    elif r_ir == 0xBE:
        ctrl_signals = sub_decoder_03(i_decoder)

    #87 LDX-ZPG,Y[=B6h]
    elif r_ir == 0xB6:
        ctrl_signals = sub_decoder_03(i_decoder)

    #88 LDY-IMMEDIATE[=A0h]
    elif r_ir == 0xA0:
        ctrl_signals = sub_decoder_03(i_decoder)

    #89 LDY-ABSOLUTE[=ACh]
    elif r_ir == 0xAC:
        ctrl_signals = sub_decoder_03(i_decoder)

    #90 LDY-ZEROPAGE[=A4h]
    elif r_ir == 0xA4:
        ctrl_signals = sub_decoder_03(i_decoder)

    #91 LDY-ZPG,X[=B4h]
    elif r_ir == 0xB4:
        ctrl_signals = sub_decoder_03(i_decoder)

    #92 LDY-ABS,X[=BCh]
    elif r_ir == 0xBC:
        ctrl_signals = sub_decoder_03(i_decoder)

    #93 ORA-IMMEDIATE[=09h]
    elif r_ir == 0x09:
        ctrl_signals = sub_decoder_03(i_decoder)

    #94 ORA-ABSOLUTE[=0Dh]
    elif r_ir == 0x0D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #95 ORA-ZEROPAGE[=05h]
    elif r_ir == 0x05:
        ctrl_signals = sub_decoder_03(i_decoder)

    #96 ORA-(IND,X)[=01h]
    elif r_ir == 0x01:
        ctrl_signals = sub_decoder_03(i_decoder)

    #97 ORA-(IND),Y[=11h]
    elif r_ir == 0x11:
        ctrl_signals = sub_decoder_03(i_decoder)

    #98 ORA-ZPG,X[=15h]
    elif r_ir == 0x15:
        ctrl_signals = sub_decoder_03(i_decoder)

    #99 ORA-ABS,X[=1Dh]
    elif r_ir == 0x1D:
        ctrl_signals = sub_decoder_03(i_decoder)

    #100 ORA-ABS,Y[=19h]
    elif r_ir == 0x19:
        ctrl_signals = sub_decoder_03(i_decoder)

    #101 SBC-IMMEDIATE[=E9h]
    elif r_ir == 0xE9:
        ctrl_signals = sub_decoder_03(i_decoder)

    #102 SBC-ABSOLUTE[=EDh]
    elif r_ir == 0xED:
        ctrl_signals = sub_decoder_03(i_decoder)

    #103 SBC-ZEROPAGE[=E5h]
    elif r_ir == 0xE5:
        ctrl_signals = sub_decoder_03(i_decoder)

    #104 SBC-(IND,X)[=E1h]
    elif r_ir == 0xE1:
        ctrl_signals = sub_decoder_03(i_decoder)

    #105 SBC-(IND),Y[=F1h]
    elif r_ir == 0xF1:
        ctrl_signals = sub_decoder_03(i_decoder)

    #106 SBC-ZPG,X[=F5h]
    elif r_ir == 0xF5:
        ctrl_signals = sub_decoder_03(i_decoder)

    #107 SBC-ABS,X[=FDh]
    elif r_ir == 0xFD:
        ctrl_signals = sub_decoder_03(i_decoder)

    #108 SBC-ABS,Y[=F9h]
    elif r_ir == 0xF9:
        ctrl_signals = sub_decoder_03(i_decoder)

    # ---------- MEM2MEM ----------
    #109 ASL-ABSOLUTE[=0Eh]
    elif r_ir == 0x0E:
        ctrl_signals = sub_decoder_04(i_decoder)

    #110 ASL-ZEROPAGE[=06h]
    elif r_ir == 0x06:
        ctrl_signals = sub_decoder_04(i_decoder)

    #111 ASL-ACCUM[=0Ah]
    elif r_ir == 0x0A:
        ctrl_signals = sub_decoder_04(i_decoder)

    #112 DEC-ABSOLUTE[=CEh]
    elif r_ir == 0xCE:
        ctrl_signals = sub_decoder_04(i_decoder)

    #113 DEC-ZEROPAGE[=C6h]
    elif r_ir == 0xC6:
        ctrl_signals = sub_decoder_04(i_decoder)

    #114 DEC-ZPG,X[=D6h]
    elif r_ir == 0xD6:
        ctrl_signals = sub_decoder_04(i_decoder)

    #115 DEC-ABS,X[=DEh]
    elif r_ir == 0xDE:
        ctrl_signals = sub_decoder_04(i_decoder)

    #116 INC-ABSOLUTE[=EEh]
    elif r_ir == 0xEE:
        ctrl_signals = sub_decoder_04(i_decoder)

    #117 INC-ZEROPAGE[=E6h]
    elif r_ir == 0xE6:
        ctrl_signals = sub_decoder_04(i_decoder)

    #118 INC-ZPG,X[=F6h]
    elif r_ir == 0xF6:
        ctrl_signals = sub_decoder_04(i_decoder)

    #119 INC-ABS,X[=FEh]
    elif r_ir == 0xFE:
        ctrl_signals = sub_decoder_04(i_decoder)

    #120 LSR-ABSOLUTE[=4Eh]
    elif r_ir == 0x4E:
        ctrl_signals = sub_decoder_04(i_decoder)

    #121 LSR-ZEROPAGE[=46h]
    elif r_ir == 0x46:
        ctrl_signals = sub_decoder_04(i_decoder)

    #122 LSR-ACCUM[=4Ah]
    elif r_ir == 0x4A:
        ctrl_signals = sub_decoder_04(i_decoder)

    #123 LSR-ZPG,X[=56h]
    elif r_ir == 0x56:
        ctrl_signals = sub_decoder_04(i_decoder)

    #124 LSR-ABS,X[=5Eh]
    elif r_ir == 0x5E:
        ctrl_signals = sub_decoder_04(i_decoder)

    #125 ROL-ABSOLUTE[=2Eh]
    elif r_ir == 0x2E:
        ctrl_signals = sub_decoder_04(i_decoder)

    #126 ROL-ZEROPAGE[=26h]
    elif r_ir == 0x26:
        ctrl_signals = sub_decoder_04(i_decoder)

    #127 ROL-ACCUM[=2Ah]
    elif r_ir == 0x2A:
        ctrl_signals = sub_decoder_04(i_decoder)

    #128 ROL-ZPG,X[=36h]
    elif r_ir == 0x36:
        ctrl_signals = sub_decoder_04(i_decoder)

    #129 ROL-ABS,X[=3Eh]
    elif r_ir == 0x3E:
        ctrl_signals = sub_decoder_04(i_decoder)

    #130 ROR-ABSOLUTE[=6Eh]
    elif r_ir == 0x6E:
        ctrl_signals = sub_decoder_04(i_decoder)

    #131 ROR-ZEROPAGE[=66h]
    elif r_ir == 0x66:
        ctrl_signals = sub_decoder_04(i_decoder)

    #132 ROR-ACCUM[=6Ah]
    elif r_ir == 0x6A:
        ctrl_signals = sub_decoder_04(i_decoder)

    #133 ROR-ZPG,X[=76h]
    elif r_ir == 0x76:
        ctrl_signals = sub_decoder_04(i_decoder)

    #134 ROR-ABS,X[=7Eh]
    elif r_ir == 0x7E:
        ctrl_signals = sub_decoder_04(i_decoder)

    # ---------- Branch ----------
    #135 BVC-RELATIVE[=50h]
    elif r_ir == 0x50:
        ctrl_signals = sub_decoder_05(i_decoder)

    #136 BVS-RELATIVE[=70h]
    elif r_ir == 0x70:
        ctrl_signals = sub_decoder_05(i_decoder)

    #137 BCC-RELATIVE[=90h]
    elif r_ir == 0x90:
        ctrl_signals = sub_decoder_05(i_decoder)

    #138 BCS-RELATIVE[=B0h]
    elif r_ir == 0xB0:
        ctrl_signals = sub_decoder_05(i_decoder)

    #139 BEQ-RELATIVE[=F0h]
    elif r_ir == 0xF0:
        ctrl_signals = sub_decoder_05(i_decoder)

    #140 BMI-RELATIVE[=30h]
    elif r_ir == 0x30:
        ctrl_signals = sub_decoder_05(i_decoder)

    #141 BNE-RELATIVE[=D0h]
    elif r_ir == 0xD0:
        ctrl_signals = sub_decoder_05(i_decoder)

    #142 BPL-RELATIVE[=10h]
    elif r_ir == 0x10:
        ctrl_signals = sub_decoder_05(i_decoder)

    # ---------- Other ----------
    #143 BRK-IMPLIED[=00h]
    elif r_ir == 0x00:
        ctrl_signals = sub_decoder_05(i_decoder)

    #144 JMP-ABSOLUTE[=4Ch]
    elif r_ir == 0x4C:
        ctrl_signals = sub_decoder_05(i_decoder)

    #145 JMP-INDIRECT[=6Ch]
    elif r_ir == 0x6C:
        ctrl_signals = sub_decoder_05(i_decoder)

    #146 JSR-ABSOLUTE[=20h]
    elif r_ir == 0x20:
        ctrl_signals = sub_decoder_05(i_decoder)

    #147 PHA-IMPLIED[=48h]
    elif r_ir == 0x48:
        ctrl_signals = sub_decoder_05(i_decoder)

    #148 PHP-IMPLIED[=08h]
    elif r_ir == 0x08:
        ctrl_signals = sub_decoder_05(i_decoder)

    #149 PLA-IMPLIED[=68h]
    elif r_ir == 0x68:
        ctrl_signals = sub_decoder_05(i_decoder)

    #150 PLP-IMPLIED[=28h]
    elif r_ir == 0x28:
        ctrl_signals = sub_decoder_05(i_decoder)

    #151 RTI-IMPLIED[=40h]
    elif r_ir == 0x40:
        ctrl_signals = sub_decoder_05(i_decoder)

    #152 RTS-IMPLIED[=60h]
    elif r_ir == 0x60:
        ctrl_signals = sub_decoder_05(i_decoder)

    # ---------- Default ----------
    else:
        ctrl_signals = ctrl_t()
        print('Undefined instruction')
    
    return ctrl_signals
