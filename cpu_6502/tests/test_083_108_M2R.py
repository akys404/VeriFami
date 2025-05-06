from cpu_6502.cpu import mod_cpu

# ---------- MEM2REG ----------
#83 LDX-IMMEDIATE[=A2h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#84 LDX-ABSOLUTE[=AEh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#85 LDX-ZEROPAGE[=A6h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#86 LDX-ABS,Y[=BEh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#87 LDX-ZPG,Y[=B6h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#88 LDY-IMMEDIATE[=A0h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#89 LDY-ABSOLUTE[=ACh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#90 LDY-ZEROPAGE[=A4h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#91 LDY-ZPG,X[=B4h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#92 LDY-ABS,X[=BCh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#93 ORA-IMMEDIATE[=09h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#94 ORA-ABSOLUTE[=0Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#95 ORA-ZEROPAGE[=05h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#96 ORA-(IND,X)[=01h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#97 ORA-(IND),Y[=11h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#98 ORA-ZPG,X[=15h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#99 ORA-ABS,X[=1Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#100 ORA-ABS,Y[=19h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#101 SBC-IMMEDIATE[=E9h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#102 SBC-ABSOLUTE[=EDh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#103 SBC-ZEROPAGE[=E5h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#104 SBC-(IND,X)[=E1h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#105 SBC-(IND),Y[=F1h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#106 SBC-ZPG,X[=F5h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#107 SBC-ABS,X[=FDh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#108 SBC-ABS,Y[=F9h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE


if __name__ == "__main__":
    test_sample()
    print("All tests passed!")