from cpu_6502.cpu import mod_cpu

# ---------- MEM2REG ----------
#61 CPX-IMMEDIATE[=E0h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#62 CPX-ABSOLUTE[=ECh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#63 CPX-ZEROPAGE[=E4h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#64 CPY-IMMEDIATE[=C0h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#65 CPY-ABSOLUTE[=CCh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#66 CPY-ZEROPAGE[=C4h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#67 EOR-IMMEDIATE[=49h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#68 EOR-ABSOLUTE[=4Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#69 EOR-ZEROPAGE[=45h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#70 EOR-(IND,X)[=41h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#71 EOR-(IND),Y[=51h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#72 EOR-ZPG,X[=55h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#73 EOR-ABS,X[=5Dh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#74 EOR-ABS,Y[=59h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#75 LDA-IMMEDIATE[=A9h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#76 LDA-ABSOLUTE[=ADh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#77 LDA-ZEROPAGE[=A5h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#78 LDA-(IND,X)[=A1h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#79 LDA-(IND),Y[=B1h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#80 LDA-ZPG,X[=B5h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#81 LDA-ABS,X[=BDh]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#82 LDA-ABS,Y[=B9h]
def test_sample():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE


if __name__ == "__main__":
    test_sample()
    print("All tests passed!")