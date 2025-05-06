from cpu_6502.cpu import mod_cpu

# ---------- Exception ----------
#01 RESET
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#02 NMI
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#03 IRQ
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

# ---------- REG2REG ----------
#04 CLC-IMPLIED[=18h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#05 CLD-IMPLIED[=D8h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#06 CLI-IMPLIED[=58h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#07 CLV-IMPLIED[=B8h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#08 DEX-IMPLIED[=CAh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#09 DEY-IMPLIED[=88h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#10 INX-IMPLIED[=E8h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#11 INY-IMPLIED[=C8h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#12 NOP-IMPLIED[=EAh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#13 SEC-IMPLIED[=38h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#14 SED-IMPLIED[=F8h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#15 SEI-IMPLIED[=78h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#16 TAX-IMPLIED[=AAh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#17 TAY-IMPLIED[=ABh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#18 TSX-IMPLIED[=BAh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#19 TXA-IMPLIED[=8Ah]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#20 TXS-IMPLIED[=9Ah]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#21 TYA-IMPLIED[=9Bh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE


if __name__ == "__main__":
    test_sample()
    print("All tests passed!")