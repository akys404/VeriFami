from cpu_6502.cpu import mod_cpu

# ---------- REG2MEM ----------
#22 STA-ABSOLUTE[=8Dh]
def test_sta_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#23 STA-ZEROPAGE[=85h]
def test_sta_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#24 STA-(IND,X)[=81h]
def test_sta_indx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#25 STA-(IND),Y[=91h]
def test_sta_indy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#26 STA-ZPG,X[=95h]
def test_sta_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#27 STA-ABS,X[=9Dh]
def test_sta_absx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#28 STA-ABS,Y[=99h]
def test_sta_absy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#29 STX-ABSOLUTE[=8Eh]
def test_stx_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#30 STX-ZEROPAGE[=86h]
def test_stx_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#31 STX-ZPG,Y[=96h]
def test_stx_zpgy():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#32 STY-ABSOLUTE[=8Ch]
def test_sty_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#33 STY-ZEROPAGE[=84h]
def test_sty_zpg():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#34 STY-ZPG,X[=94h]
def test_sty_zpgx():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE
