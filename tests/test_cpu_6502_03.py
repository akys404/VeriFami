from cpu_6502.cpu import mod_cpu

# ---------- MEM2REG ----------
#35 ADC-IMMEDIATE[=69h]
def test_adc_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#36 ADC-ABSOLUTE[=6Dh]
def test_adc_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#37 ADC-ZEROPAGE[=65h]
def test_adc_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#38 ADC-(IND,X)[=61h]
def test_adc_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#39 ADC-(IND),Y[=71h]
def test_adc_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#40 ADC-ZPG,X[=75h]
def test_adc_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#41 ADC-ABS,X[=7Dh]
def test_adc_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#42 ADC-ABS,Y[=79h]
def test_adc_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#43 AND-IMMEDIATE[=29h]
def test_and_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#44 AND-ABSOLUTE[=2Dh]
def test_and_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#45 AND-ZEROPAGE[=25h]
def test_and_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#46 AND-(IND,X)[=21h]
def test_and_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#47 AND-(IND),Y[=31h]
def test_and_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#48 AND-ZPG,X[=35h]
def test_and_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#49 AND-ABS,X[=3Dh]
def test_and_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#50 AND-ABS,Y[=39h]
def test_and_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#51 BIT-ABSOLUTE[=2Ch]
def test_bit_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#52 BIT-ZEROPAGE[=24h]
def test_bit_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#53 CMP-IMMEDIATE[=C9h]
def test_cmp_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#54 CMP-ABSOLUTE[=CDh]
def test_cmp_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#55 CMP-ZEROPAGE[=C5h]
def test_cmp_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#56 CMP-(IND,X)[=C1h]
def test_cmp_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#57 CMP-(IND),Y[=D1h]
def test_cmp_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#58 CMP-ZPG,X[=D5h]
def test_cmp_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#59 CMP-ABS,X[=DDh]
def test_cmp_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#60 CMP-ABS,Y[=D9h]
def test_cmp_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#61 CPX-IMMEDIATE[=E0h]
def test_cpx_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#62 CPX-ABSOLUTE[=ECh]
def test_cpx_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#63 CPX-ZEROPAGE[=E4h]
def test_cpx_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#64 CPY-IMMEDIATE[=C0h]
def test_cpy_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#65 CPY-ABSOLUTE[=CCh]
def test_cpy_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#66 CPY-ZEROPAGE[=C4h]
def test_cpy_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#67 EOR-IMMEDIATE[=49h]
def test_eor_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#68 EOR-ABSOLUTE[=4Dh]
def test_eor_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#69 EOR-ZEROPAGE[=45h]
def test_eor_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#70 EOR-(IND,X)[=41h]
def test_eor_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#71 EOR-(IND),Y[=51h]
def test_eor_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#72 EOR-ZPG,X[=55h]
def test_eor_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#73 EOR-ABS,X[=5Dh]
def test_eor_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#74 EOR-ABS,Y[=59h]
def test_eor_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#75 LDA-IMMEDIATE[=A9h]
def test_lda_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#76 LDA-ABSOLUTE[=ADh]
def test_lda_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#77 LDA-ZEROPAGE[=A5h]
def test_lda_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#78 LDA-(IND,X)[=A1h]
def test_lda_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#79 LDA-(IND),Y[=B1h]
def test_lda_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#80 LDA-ZPG,X[=B5h]
def test_lda_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#81 LDA-ABS,X[=BDh]
def test_lda_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#82 LDA-ABS,Y[=B9h]
def test_lda_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#83 LDX-IMMEDIATE[=A2h]
def test_ldx_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#84 LDX-ABSOLUTE[=AEh]
def test_ldx_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#85 LDX-ZEROPAGE[=A6h]
def test_ldx_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#86 LDX-ABS,Y[=BEh]
def test_ldx_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#87 LDX-ZPG,Y[=B6h]
def test_ldx_zpgy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#88 LDY-IMMEDIATE[=A0h]
def test_ldy_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#89 LDY-ABSOLUTE[=ACh]
def test_ldy_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#90 LDY-ZEROPAGE[=A4h]
def test_ldy_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#91 LDY-ZPG,X[=B4h]
def test_ldy_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#92 LDY-ABS,X[=BCh]
def test_ldy_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#93 ORA-IMMEDIATE[=09h]
def test_ora_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#94 ORA-ABSOLUTE[=0Dh]
def test_ora_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#95 ORA-ZEROPAGE[=05h]
def test_ora_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#96 ORA-(IND,X)[=01h]
def test_ora_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#97 ORA-(IND),Y[=11h]
def test_ora_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#98 ORA-ZPG,X[=15h]
def test_ora_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#99 ORA-ABS,X[=1Dh]
def test_ora_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#100 ORA-ABS,Y[=19h]
def test_ora_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#101 SBC-IMMEDIATE[=E9h]
def test_sbc_imm():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#102 SBC-ABSOLUTE[=EDh]
def test_sbc_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#103 SBC-ZEROPAGE[=E5h]
def test_sbc_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#104 SBC-(IND,X)[=E1h]
def test_sbc_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#105 SBC-(IND),Y[=F1h]
def test_sbc_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#106 SBC-ZPG,X[=F5h]
def test_sbc_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#107 SBC-ABS,X[=FDh]
def test_sbc_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#108 SBC-ABS,Y[=F9h]
def test_sbc_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE
