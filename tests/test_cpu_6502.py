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
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#03 IRQ
def test_irq():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

# ---------- REG2REG ----------
#04 CLC-IMPLIED[=18h]
def test_clc_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#05 CLD-IMPLIED[=D8h]
def test_cld_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#06 CLI-IMPLIED[=58h]
def test_cli_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#07 CLV-IMPLIED[=B8h]
def test_clv_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#08 DEX-IMPLIED[=CAh]
def test_dex_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#09 DEY-IMPLIED[=88h]
def test_dey_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#10 INX-IMPLIED[=E8h]
def test_inx_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#11 INY-IMPLIED[=C8h]
def test_iny_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#12 NOP-IMPLIED[=EAh]
def test_nop_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#13 SEC-IMPLIED[=38h]
def test_sec_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#14 SED-IMPLIED[=F8h]
def test_sed_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#15 SEI-IMPLIED[=78h]
def test_sei_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#16 TAX-IMPLIED[=AAh]
def test_tax_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#17 TAY-IMPLIED[=ABh]
def test_tay_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#18 TSX-IMPLIED[=BAh]
def test_tsx_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#19 TXA-IMPLIED[=8Ah]
def test_txa_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#20 TXS-IMPLIED[=9Ah]
def test_txs_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#21 TYA-IMPLIED[=9Bh]
def test_tya_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE
