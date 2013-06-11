
### Filter definitions ###

def narrow_high_mass(hname):
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'rsg' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # reject wide reonances
    if 'w10p' in pname:
        return False
    # Accept only a few mass points (no interpolation)
    mass = pname.split('w')[0].split('zp')[1]
    mass_blacklist = ['1000','1500','2000','3000']
    return mass in mass_blacklist


def wide_high_mass(hname):
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'rsg' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # reject wide reonances
    if 'w1p' in pname:
        return False
    # Accept only a few mass points (no interpolation)
    mass = pname.split('w')[0].split('zp')[1]
    mass_blacklist = ['1000','1500','2000','3000']
    return mass in mass_blacklist


def rsg_high_mass(hname):
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'zp' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # Accept only a few mass points (no interpolation)
    mass = pname.split('rsg')[1]
    mass_blacklist = ['1000','1500','2000','3000']
    return mass in mass_blacklist

def narrow_low_mass(hname):
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'rsg' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # reject wide reonances
    if 'w10p' in pname:
        return False
    # Accept only a few mass points (no interpolation)
    mass = pname.split('w')[0].split('zp')[1]
    mass_blacklist = ['500']
    return mass in mass_blacklist

def wide_low_mass(hname):
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'rsg' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # reject wide reonances
    if 'w1p' in pname:
        return False
    # Accept only a few mass points (no interpolation)
    mass = pname.split('w')[0].split('zp')[1]
    mass_blacklist = ['500','1000']
    return mass in mass_blacklist

def rsg_low_mass(hname):
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'zp' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # Accept only a few mass points (no interpolation)
    mass = pname.split('rsg')[1]
    mass_blacklist = ['500','750','1000']
    return mass in mass_blacklist


#### Model building ####

def build_hadhigh_model(files, filter, signal, mcstat):
    """ All hadronic high mass model """    
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
        if p=='qcd': continue
        model.add_lognormal_uncertainty('lumi', 0.022, p)
        model.add_lognormal_uncertainty('subjet_scalefactor', math.log(1.06), p)
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.50), 'ttbar')
    return model


def build_semihigh_model(files, filter, signal, mcstat):
    """ Semileptonic high mass model"""
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.022), p)
    
    # common to e and mu channels
    model.add_lognormal_uncertainty('zl_rate', math.log(2.0), 'zjets')
    model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wlight')
    model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wb')
    model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wc')
    model.add_lognormal_uncertainty('vb_rate', math.log(1.87), 'wb')
    model.add_lognormal_uncertainty('vc_rate', math.log(1.87), 'wc')
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    model.add_lognormal_uncertainty('st_rate', math.log(1.5), 'singletop')
    
    # mu channels 
    for obs in ('mu_0btag_mttbar', 'mu_1btag_mttbar'):
        for proc in ('wc', 'wb', 'wlight'):
            model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.76), math.log(0.62), proc, obs)
            model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.08), math.log(0.92), proc, obs)
        for proc in model.processes:
            model.add_lognormal_uncertainty('mu_eff', math.log(1.05), proc, obs)
    
    # e channels 
    for obs in ('el_0btag_mttbar', 'el_1btag_mttbar'):
        for proc in ('wc', 'wb', 'wlight'):
            model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.87), math.log(0.57), proc, obs)
            model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.05), math.log(0.95), proc, obs)
        for proc in model.processes:
            model.add_lognormal_uncertainty('ele_eff', math.log(1.05), proc, obs)
    return model


def build_semilow_model(files, filter, signal, mcstat):
    """ Semileptonic low mass model """
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    
    observables = ["mu_3jets_1btag_mttbar",
                   "ele_3jets_1btag_mttbar",
                   "mu_4jets_0btag_mttbar",
                   "mu_4jets_1btag_mttbar",
                   "mu_4jets_2btag_mttbar",
                   "ele_4jets_0btag_mttbar",
                   "ele_4jets_1btag_mttbar",
                   "ele_4jets_2btag_mttbar"]
    
    for p in model.processes:
        if p=='qcd' : continue
        model.add_lognormal_uncertainty('lumi', math.log(1.022), p)
        for observable in observables:
            if "mu" in observable:
                model.add_lognormal_uncertainty('mu_eff', math.log(1.03), p, observable)
            elif "ele" in observable:
                model.add_lognormal_uncertainty('ele_eff', math.log(1.03), p, observable)
            if "3jets" in observable:
                model.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'wlight', observable)
                model.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'wb', observable)
                model.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'wc', observable)
                model.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'zlight', observable)
                model.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'zb', observable)
                model.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'zc', observable)
            elif "4jets" in observable:
                model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wlight', observable)
                model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wb', observable)
                model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wc', observable)
                model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'zlight', observable)
                model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'zb', observable)
                model.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'zc', observable)
    
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    
    model.add_lognormal_uncertainty('vb_rate', math.log(1.87), 'wb')
    model.add_lognormal_uncertainty('vb_rate', math.log(1.87), 'zb')
    model.add_lognormal_uncertainty('vc_rate', math.log(1.87), 'wc')
    model.add_lognormal_uncertainty('vc_rate', math.log(1.87), 'zc')
    
    model.add_lognormal_uncertainty('zl_rate', math.log(1.3), 'zlight')
    model.add_lognormal_uncertainty('zl_rate', math.log(1.3), 'zb')
    model.add_lognormal_uncertainty('zl_rate', math.log(1.3), 'zc')
    
    model.add_lognormal_uncertainty('st_rate', math.log(1.3), 'singletop')
    
    model.add_lognormal_uncertainty('eleqcd3j1t_rate', math.log(1.43), 'qcd', "ele_3jets_1btag_mttbar")
    model.add_lognormal_uncertainty('eleqcd4j0t_rate', math.log(1.63), 'qcd', "ele_4jets_0btag_mttbar")
    model.add_lognormal_uncertainty('eleqcd4j1t_rate', math.log(1.48), 'qcd', "ele_4jets_1btag_mttbar")
    model.add_lognormal_uncertainty('eleqcd4j2t_rate', math.log(1.62), 'qcd', "ele_4jets_2btag_mttbar")
    model.add_lognormal_uncertainty('muqcd3j1t_rate', math.log(1.61), 'qcd', "mu_3jets_1btag_mttbar")
    model.add_lognormal_uncertainty('muqcd4j0t_rate', math.log(1.52), 'qcd', "mu_4jets_0btag_mttbar")
    model.add_lognormal_uncertainty('muqcd4j1t_rate', math.log(1.73), 'qcd', "mu_4jets_1btag_mttbar")
    model.add_lognormal_uncertainty('muqcd4j2t_rate', math.log(1.68), 'qcd', "mu_4jets_2btag_mttbar")
    return model


def build_dilow_model(files, filter, signal, mcstat):
    """ Dilepton low mass model """
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    model.add_lognormal_uncertainty('ttbar_rate', 0.15, 'ttbar')
    model.add_lognormal_uncertainty('VV_xsec', 0.038, 'VV')
    model.add_lognormal_uncertainty('vj_rate', 0.05, 'wjets', 'ee')
    model.add_lognormal_uncertainty('vj_rate', 0.05, 'wjets', 'emu')
    model.add_lognormal_uncertainty('st_rate', 0.077, 'singletop')
    model.add_lognormal_uncertainty('DY_norm', 0.3, 'DY', 'ee')
    model.add_lognormal_uncertainty('DY_norm', 0.3, 'DY', 'mumu')
    model.add_lognormal_uncertainty('DY_norm', 0.3, 'DY', 'emu')
    model.add_lognormal_uncertainty('QCD_norm', 0.130, 'qcd', 'ee')
    model.add_lognormal_uncertainty('QCD_norm', 0.182, 'qcd', 'mumu')
    model.add_lognormal_uncertainty('QCD_norm', 0.097, 'qcd', 'emu')	
    # the qcd model is from data, so do not apply a lumi uncertainty on that:
    for p in model.processes:
        if p == 'qcd' or p == 'wjets': continue
        model.add_lognormal_uncertainty('btagsf', 0.10, p)
        
    for p2 in model.processes:
        if p2 == 'qcd' or p2 == 'DY' or p2 == 'wjets': continue
        model.add_lognormal_uncertainty('lumi', 0.022, p2)
        model.add_lognormal_uncertainty('eid', 0.02, p2, 'ee')
        model.add_lognormal_uncertainty('eid', 0.02, p2, 'emu')
        model.add_lognormal_uncertainty('muid', 0.02, p2, 'mumu')
        model.add_lognormal_uncertainty('muid', 0.02, p2, 'emu')
        model.add_lognormal_uncertainty('btagsf', 0.1, 'wjets', 'ee')
        model.add_lognormal_uncertainty('btagsf', 0.1, 'wjets', 'emu')
        model.add_lognormal_uncertainty('lumi', 0.022, 'wjets', 'ee')
        model.add_lognormal_uncertainty('lumi', 0.022, 'wjets', 'emu')
        model.add_lognormal_uncertainty('eid', 0.02, 'wjets', 'ee')
        model.add_lognormal_uncertainty('eid', 0.02, 'wjets', 'emu')
        model.add_lognormal_uncertainty('muid', 0.02, 'wjets', 'emu')	
        
    # Specifying all uncertainties manually can be error-prone. You can also execute
    # a automatically generated file using python's execfile here
    # which contains these statements, or read in a text file, etc. Remember: this is a
    # python script, so use this power!
    model.add_lognormal_uncertainty('scale_vjets', 1.0, 'wjets')
    model.add_lognormal_uncertainty('matching_vjets', 1.0, 'wjets')
    return model


import exceptions


def build_model(type, mcstat = True):

    model = None

    if type == 'narrow_lowmass':

        modelsemilow = build_semilow_model(
            ['low_mass_semileptonic_selection.root'],
            narrow_low_mass,
            'zp*',
            mcstat
        )
        modeldilow = build_dilow_model(
            ['narrow_low_mass_dilepton_selection.root'],
            narrow_low_mass,
            'zp*',
            mcstat
        )
        model = modelsemilow
        model.combine(modeldilow, False)
    
    elif type == 'narrow_highmass':

        modelallhigh = build_hadhigh_model(
            ['high_mass_allhadronic_selection.root'],
            narrow_high_mass,
            'zp*',
            mcstat
        )
        modelsemihigh = build_semihigh_model(
            ['high_mass_semileptonic_selection.root'],
            narrow_high_mass,
            'zp*',
            mcstat
        )
        modeldilow = build_dilow_model(
            ['narrow_low_mass_dilepton_selection.root'],
            narrow_high_mass,
            'zp*',
            mcstat
        )
        model = modelallhigh
        model.combine(modelsemihigh, False)
        model.combine(modeldilow, False)

    elif type == 'wide_lowmass':

        modelsemilow = build_semilow_model(
            ['low_mass_semileptonic_selection.root'],
            wide_low_mass,
            'zp*',
            mcstat
        )
        modeldilow = build_dilow_model(
            ['wide_low_mass_dilepton_selection.root'],
            wide_low_mass,
            'zp*',
            mcstat
        )
        model = modelsemilow
        model.combine(modeldilow, False)
    
    elif type == 'wide_highmass':

        modelallhigh = build_hadhigh_model(
            ['high_mass_allhadronic_selection.root'],
            wide_high_mass,
            'zp*',
            mcstat
        )
        modelsemihigh = build_semihigh_model(
            ['high_mass_semileptonic_selection.root'],
            wide_high_mass,
            'zp*',
            mcstat
        )
        modeldilow = build_dilow_model(
            ['wide_low_mass_dilepton_selection.root'],
            wide_high_mass,
            'zp*',
            mcstat
        )
        model = modelallhigh
        model.combine(modelsemihigh, False)
        model.combine(modeldilow, False)

    elif type == 'rsg_highmass':

        modelallhigh = build_hadhigh_model(
            ['high_mass_allhadronic_selection.root'],
            rsg_high_mass,
            'rsg*',
            mcstat
        )
        modelsemihigh = build_semihigh_model(
            ['high_mass_semileptonic_selection.root'],
            rsg_high_mass,
            'rsg*',
            mcstat
        )
        model = modelallhigh
        model.combine(modelsemihigh, False)

    else:

        raise exceptions.ValueError('Type %s is undefined' % type)

    for p in model.distribution.get_parameters():
        d = model.distribution.get_distribution(p)
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

    return model


# Code introduced by theta_driver

# Building the statistical model
args = {'type': 'narrow_lowmass'}

model = build_model(**args)

args = {}

results = bayesian_limits(model, run_theta = True, **args)
exp, obs = results

for i in range(len(exp.x)):
    print '%.2f: [%.6f, %.6f, %.6f, %.6f, %.6f, %.6f]\n' % (
                exp.x[i], exp.y[i],
                exp.bands[1][1][i] - exp.y[i], exp.bands[1][0][i] - exp.y[i],
                exp.bands[0][1][i] - exp.y[i], exp.bands[0][0][i] - exp.y[i],
                obs.y[i]
            )


