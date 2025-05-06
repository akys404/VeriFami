from cpu_6502.cpu import mod_cpu

# ---------- MEM2REG ----------
#35 ADC-IMMEDIATE[=69h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#36 ADC-ABSOLUTE[=6Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#37 ADC-ZEROPAGE[=65h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#38 ADC-(IND,X)[=61h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#39 ADC-(IND),Y[=71h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#40 ADC-ZPG,X[=75h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#41 ADC-ABS,X[=7Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#42 ADC-ABS,Y[=79h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#43 AND-IMMEDIATE[=29h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#44 AND-ABSOLUTE[=2Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#45 AND-ZEROPAGE[=25h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#46 AND-(IND,X)[=21h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#47 AND-(IND),Y[=31h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#48 AND-ZPG,X[=35h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#49 AND-ABS,X[=3Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#50 AND-ABS,Y[=39h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#51 BIT-ABSOLUTE[=2Ch]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#52 BIT-ZEROPAGE[=24h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#53 CMP-IMMEDIATE[=C9h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#54 CMP-ABSOLUTE[=CDh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#55 CMP-ZEROPAGE[=C5h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#56 CMP-(IND,X)[=C1h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#57 CMP-(IND),Y[=D1h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#58 CMP-ZPG,X[=D5h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#59 CMP-ABS,X[=DDh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE


if __name__ == "__main__":
    test_sample()
    print("All tests passed!")