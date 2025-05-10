from cpu_6502.cpu import mod_cpu

# ---------- Exception ----------
#01 RESET
def test_res():
    u_cpu = mod_cpu(debug=False)
    u_cpu.step(0x00, rst_n=0)
    u_cpu.step(0x00, rst_n=0)
    u_cpu.step(0x00, rst_n=1)
    u_cpu.step(0x00, rst_n=1)
    output = u_cpu.step(0x0A, rst_n=1)
    assert output['o_address'] == 0xFFFC
    output = u_cpu.step(0x0B, rst_n=1)
    assert output['o_address'] == 0xFFFD
    output = u_cpu.step(0x00, rst_n=1)
    assert output['o_address'] == 0x0B0A

#02 NMI
def test_nmi():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#03 IRQ
def test_irq():
    u_cpu = mod_cpu(debug=False)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE
