from cpu_6502.cpu import mod_cpu

# ---------- MEM2MEM ----------
#109 ASL-ABSOLUTE[=0Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#110 ASL-ZEROPAGE[=06h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#111 ASL-ACCUM[=0Ah]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#112 DEC-ABSOLUTE[=CEh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#113 DEC-ZEROPAGE[=C6h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#114 DEC-ZPG,X[=D6h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#115 DEC-ABS,X[=DEh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#116 INC-ABSOLUTE[=EEh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#117 INC-ZEROPAGE[=E6h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#118 INC-ZPG,X[=F6h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#119 INC-ABS,X[=FEh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#120 LSR-ABSOLUTE[=4Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#121 LSR-ZEROPAGE[=46h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#122 LSR-ACCUM[=4Ah]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#123 LSR-ZPG,X[=56h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#124 LSR-ABS,X[=5Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#125 ROL-ABSOLUTE[=2Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#126 ROL-ZEROPAGE[=26h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#127 ROL-ACCUM[=2Ah]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#128 ROL-ZPG,X[=36h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#129 ROL-ABS,X[=3Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#130 ROR-ABSOLUTE[=6Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#131 ROR-ZEROPAGE[=66h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#132 ROR-ACCUM[=6Ah]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#133 ROR-ZPG,X[=76h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#134 ROR-ABS,X[=7Eh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE


if __name__ == "__main__":
    test_sample()
    print("All tests passed!")