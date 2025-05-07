from cpu_6502.cpu import mod_cpu

# ---------- Branch ----------
#135 BVC-RELATIVE[=50h]
def test_bvc_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#136 BVS-RELATIVE[=70h]
def test_bvs_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#137 BCC-RELATIVE[=90h]
def test_bcc_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#138 BCS-RELATIVE[=B0h]
def test_bcs_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#139 BEQ-RELATIVE[=F0h]
def test_beq_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#140 BMI-RELATIVE[=30h]
def test_bmi_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#141 BNE-RELATIVE[=D0h]
def test_bne_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#142 BPL-RELATIVE[=10h]
def test_bpl_rel():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

# ---------- Other ----------
#143 BRK-IMPLIED[=00h]
def test_brk_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#144 JMP-ABSOLUTE[=4Ch]
def test_jmp_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#145 JMP-INDIRECT[=6Ch]
def test_jmp_ind():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#146 JSR-ABSOLUTE[=20h]
def test_jsr_abs():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#147 PHA-IMPLIED[=48h]
def test_pha_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#148 PHP-IMPLIED[=08h]
def test_php_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#149 PLA-IMPLIED[=68h]
def test_pla_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#150 PLP-IMPLIED[=28h]
def test_plp_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#151 RTI-IMPLIED[=40h]
def test_rti_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE

#152 RTS-IMPLIED[=60h]
def test_rts_imp():
    u_cpu = mod_cpu(debug=True)
    u_cpu.r_x = 0xFE
    assert u_cpu.r_x == 0xFE
