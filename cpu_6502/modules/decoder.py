from cpu_6502.modules.utils import stage_e, ctrl_t

def decoder(r_ir, r_stage):
    set_ctrl = {}
    #xx for debug[=00h]
    if r_ir == 0x00:
        set_ctrl = {'en_ir':1, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}

    #10 INX-IMPLIED[=E8h]
    elif r_ir == 0xE8:
        if r_stage == stage_e.T1:
            set_ctrl = {'en_ir':1, 'en_p':0x82, 'sel_p':2, 'sel_main':0, 'en_x':1, 'sel_cin':1, 'sel_alu':0, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}
        elif r_stage == stage_e.T2:
            set_ctrl = {'sel_st':2, 'sel_main':2, 'sel_ain':2, 'sel_bin':0, 'sel_abh':6, 'sel_abl':9}

    #11 INY-IMPLIED[=C8h]
    elif r_ir == 0xC8:
        if r_stage == stage_e.T1:
            set_ctrl = {'en_ir':1, 'en_p':0x82, 'sel_p':2, 'sel_main':0, 'en_y':1, 'sel_cin':1, 'sel_alu':0, 'sel_abh':7, 'sel_abl':0xA, 'sel_pch':1, 'sel_pcl':1}
        elif r_stage == stage_e.T2:
            set_ctrl = {'sel_st':2, 'sel_main':3, 'sel_ain':2, 'sel_bin':0, 'sel_abh':6, 'sel_abl':9}

    ctrl_signals = ctrl_t()
    ctrl_signals.update(set_ctrl)

    return ctrl_signals
