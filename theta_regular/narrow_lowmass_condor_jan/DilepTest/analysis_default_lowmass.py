# -*- coding: utf-8 -*-
import scipy.interpolate

def histogram_filter(hname):
    if 'rskkg' not in hname and 'zp' not in hname: return True
    zp_blacklist = ('zp1000w100', 'zp1500w150', 'zp2000w200', 'zp3000w300',
                    'zp1000wide', 'zp1500wide', 'zp2000wide', 'zp3000wide',
                    'zpwide1000', 'zpwide1500', 'zpwide2000', 'zpwide3000',
                    'rskkg', 'zp1250', 'kkgluon', )
    for zpw in zp_blacklist:
        if ('__' + zpw) in hname : return False
    return True
 
def histogram_filter_semilep(hname):
    if 'zp' not in hname and 'kkgluon' not in hname : return True
    zp_blackList = (
        'wide', 'kkgluon'
        )
    for zpw in zp_blackList :
        if zpw in hname : return False
    snames = hname.split('__')
    iname = ''
    for sname in snames :
        if 'zp' in sname :
            iname = sname
            break
    m = utils.extract_number(sname)
    return m = 1000
    #return m == 500 or m == 750 or m == 1000

"""
    zp_whitelist = ('zp1000', 'zp1500', 'zp2000', 'zp3000')
    for zpw in zp_whitelist:
        if ('__' + zpw) in hname: return True
    return False
"""

def external_to_internal(hname):
    m = {'zp1000w10': 'zp1000', 'zp1500w15':'zp1500', 'zp2000w20':'zp2000', 'zp3000w30':'zp3000', # allhad
         'zp500':'zp500', 'zp750':'zp750', 'zp1000':'zp1000', 'zp1250':'zp1250', 'zp1500':'zp1500', 'zp2000':'zp2000', 'zp3000':'zp3000'  # everything else
         }
    for old_pname in m:
        if ('__' + old_pname) in hname: hname = hname.replace('__' + old_pname, '__' + m[old_pname])
    return hname


def build_zp_model():
    fileshadhigh  = ['high_mass_allhadronic_selection.root' ]
    filessemihigh = ['high_mass_semileptonic_selection.root' ]
    filessemilow  = ['low_mass_semileptonic_selection.root' ]
    filesdilow    = ['narrow_low_mass_dilepton_selection.root']


    #### Semileptonic, low mass ####
    modelsemilow = build_model_from_rootfile(filessemilow, histogram_filter_semilep, external_to_internal)
    modelsemilow.fill_histogram_zerobins()
    #modelsemilow.set_signal_processes(['zp*', 'kkgluon*'])
    modelsemilow.set_signal_processes('zp*')
    observables = ["mu_3jets_1btag_mttbar",
                   "ele_3jets_1btag_mttbar",
                   "mu_4jets_0btag_mttbar",
                   "mu_4jets_1btag_mttbar",
                   "mu_4jets_2btag_mttbar",
                   "ele_4jets_0btag_mttbar",
                   "ele_4jets_1btag_mttbar",
                   "ele_4jets_2btag_mttbar"]
    
    for p in modelsemilow.processes:
        if p=='qcd' : continue
        modelsemilow.add_lognormal_uncertainty('lumi', math.log(1.022), p)
        for observable in observables:
            if "mu" in observable:
                modelsemilow.add_lognormal_uncertainty('mu_eff', math.log(1.03), p, observable)
            elif "ele" in observable:
                modelsemilow.add_lognormal_uncertainty('ele_eff', math.log(1.03), p, observable)
            if "3jets" in observable:
                modelsemilow.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'wlight', observable)
                modelsemilow.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'wb', observable)
                modelsemilow.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'wc', observable)
                modelsemilow.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'zlight', observable)
                modelsemilow.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'zb', observable)
                modelsemilow.add_lognormal_uncertainty('v3j_rate', math.log(1.5), 'zc', observable)
            elif "4jets" in observable:
                modelsemilow.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wlight', observable)
                modelsemilow.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wb', observable)
                modelsemilow.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'wc', observable)
                modelsemilow.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'zlight', observable)
                modelsemilow.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'zb', observable)
                modelsemilow.add_lognormal_uncertainty('vj_rate', math.log(1.5), 'zc', observable)

    modelsemilow.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    
    modelsemilow.add_lognormal_uncertainty('vb_rate', math.log(2.), 'wb')
    modelsemilow.add_lognormal_uncertainty('vb_rate', math.log(2.), 'zb')
    modelsemilow.add_lognormal_uncertainty('vc_rate', math.log(2.), 'wc')
    modelsemilow.add_lognormal_uncertainty('vc_rate', math.log(2.), 'zc')

    modelsemilow.add_lognormal_uncertainty('zl_rate', math.log(1.3), 'zlight')
    modelsemilow.add_lognormal_uncertainty('zl_rate', math.log(1.3), 'zb')
    modelsemilow.add_lognormal_uncertainty('zl_rate', math.log(1.3), 'zc')
    
    modelsemilow.add_lognormal_uncertainty('st_rate', math.log(1.30), 'singletop')
    
    modelsemilow.add_lognormal_uncertainty('eleqcd3j1t_rate', math.log(1.43), 'qcd', "ele_3jets_1btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('eleqcd4j0t_rate', math.log(1.63), 'qcd', "ele_4jets_0btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('eleqcd4j1t_rate', math.log(1.48), 'qcd', "ele_4jets_1btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('eleqcd4j2t_rate', math.log(1.62), 'qcd', "ele_4jets_2btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('muqcd3j1t_rate', math.log(1.61), 'qcd', "mu_3jets_1btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('muqcd4j0t_rate', math.log(1.52), 'qcd', "mu_4jets_0btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('muqcd4j1t_rate', math.log(1.73), 'qcd', "mu_4jets_1btag_mttbar")
    modelsemilow.add_lognormal_uncertainty('muqcd4j2t_rate', math.log(1.68), 'qcd', "mu_4jets_2btag_mttbar")


    #### Dileptonic, low mass ####
    modeldilow = build_model_from_rootfile(filesdilow, histogram_filter_semilep, external_to_internal)
    modeldilow.fill_histogram_zerobins()
    modeldilow.set_signal_processes('zp*')
    modeldilow.add_lognormal_uncertainty('ttbar_rate', 0.15, 'ttbar')
    modeldilow.add_lognormal_uncertainty('VV_xsec', 0.038, 'VV')
    modeldilow.add_lognormal_uncertainty('vj_rate', 0.05, 'WJets', 'ee')
    modeldilow.add_lognormal_uncertainty('vj_rate', 0.05, 'WJets', 'emu')
    modeldilow.add_lognormal_uncertainty('st_rate', 0.077, 'singletop')
    modeldilow.add_lognormal_uncertainty('DY_norm', 0.30, 'DY', 'ee')
    modeldilow.add_lognormal_uncertainty('DY_norm', 0.30, 'DY', 'mumu')
    modeldilow.add_lognormal_uncertainty('DY_norm', 0.30, 'DY', 'emu')
    modeldilow.add_lognormal_uncertainty('QCD_norm', 0.130, 'qcd', 'ee')
    modeldilow.add_lognormal_uncertainty('QCD_norm', 0.182, 'qcd', 'mumu')
    modeldilow.add_lognormal_uncertainty('QCD_norm', 0.097, 'qcd', 'emu')	
    # the qcd modeldilow is from data, so do not apply a lumi uncertainty on that:
    for p in modeldilow.processes:
        if p == 'qcd' or p == 'WJets': continue
        modeldilow.add_lognormal_uncertainty('btagsf', 0.10, p)
		
    for p2 in modeldilow.processes:
        if p2 == 'qcd' or p2 == 'DY' or p2 == 'WJets': continue
        modeldilow.add_lognormal_uncertainty('lumi', 0.022, p2)
        modeldilow.add_lognormal_uncertainty('eid', 0.02, p2, 'ee')
        modeldilow.add_lognormal_uncertainty('eid', 0.02, p2, 'emu')
        modeldilow.add_lognormal_uncertainty('muid', 0.02, p2, 'mumu')
        modeldilow.add_lognormal_uncertainty('muid', 0.02, p2, 'emu')
	modeldilow.add_lognormal_uncertainty('btagsf', 0.10, 'WJets', 'ee')
	modeldilow.add_lognormal_uncertainty('btagsf', 0.10, 'WJets', 'emu')
	modeldilow.add_lognormal_uncertainty('lumi', 0.022, 'WJets', 'ee')
	modeldilow.add_lognormal_uncertainty('lumi', 0.022, 'WJets', 'emu')
	modeldilow.add_lognormal_uncertainty('eid', 0.02, 'WJets', 'ee')
	modeldilow.add_lognormal_uncertainty('eid', 0.02, 'WJets', 'emu')
	modeldilow.add_lognormal_uncertainty('muid', 0.02, 'WJets', 'emu')	
    # Specifying all uncertainties manually can be error-prone. You can also execute
    # a automatically generated file using python's execfile here
    # which contains these statements, or read in a text file, etc. Remember: this is a
    # python script, so use this power!
    modeldilow.add_lognormal_uncertainty('scale_vjets', 1.00, 'WJets')
    modeldilow.add_lognormal_uncertainty('matching_vjets', 1.00, 'WJets')

    
    #model = modelhadhigh
    model = modelsemilow
    #model = modeldilow
    #model.combine(modelhadhigh, False)
    #model.combine(modelsemihigh, False)
    #model.combine(modelsemilow, False)
    model.combine(modeldilow, False)

    return model

# either:
# * call with step = 0 first, run all config files through theta, then call with step = 1 OR
# * call directly with step=1, will run all locally ...
def limits_zp(model, step = 1):
   if step==0:
       #bayesian_limits(model, run_theta=False)
       cls_limits(model, ts = 'lhclike', run_theta=False, write_debuglog = False)
       #cls_limits(model, ts = 'lr', run_theta=False)
       return
   #plot_exp, plot_obs = bayesian_limits(model)
   plot_exp, plot_obs = cls_limits(model, ts = 'lhclike', write_debuglog = False)
   #plot_exp, plot_obs = cls_limits(model, ts = 'lr')
   plot_exp.write_txt('exp_limit.txt')
   plot_obs.write_txt('obs_limit.txt')
   plot_obs.legend = 'observed limit (95% C.L.)'
   plot_exp.legend = 'expected limit (95% C.L.)'
   plot_exp.color = '#aaaaaa'
   plot_obs.yerrors = None
   dp1 = plotutil.plotdata()
   dp1.x = [1000]
   dp1.y = [0]
   dp1.color = plot_exp.bands[1][2]
   dp1.legend = 'central $1\\sigma$ expected limit'
   dp2 = plotutil.plotdata()
   dp2.x = [1000]
   dp2.y = [0]
   dp2.color = plot_exp.bands[0][2]
   dp2.legend = 'central $2\\sigma$ expected limit'
   zp12 = plotutil.plotdata()
   zp12.x, zp12.y = get_zp(1.2)
   zp12.legend = 'Topcolor $\\rm Z^{\\prime}$, 1.2% width, Harris et al.'
   zp12.color = '#ff00ff'
   zp12.fmt = '--'
   zp3 = plotutil.plotdata()
   zp3.x, zp3.y = get_zp(3.0)
   zp3.legend = 'Topcolor $\\rm Z^{\\prime}$, 3.0% width, Harris et al.'
   zp3.color = '#0000ff'
   zp3.fmt = '--'
   kkg = plotutil.plotdata()
   kkg.x, kkg.y = get_kkg()
   kkg.legend = 'KK Gluon, Agashe et al.'
   kkg.color = '#aaaa00'
   kkg.fmt = '--'
   kkg.as_function=True
   zp12.as_function=True
   zp3.as_function=True
   #plot.bands = None
   #plot_nd.legend = 'median expected limit'
   #plot_nd.color = '#aaaaaa'
   #zp3.write_txt('zp3.txt')
   #zp3_xsec = scipy.interpolate.interp1d(zp3.x[:], map(lambda x: math.log(x), zp3.y))
   #limit_obs = scipy.interpolate.interp1d(plot.x[:], map(lambda x: math.log(x), plot.y))
   #for x in range(750, 1500, 1.0):
   #    if zp3_xsec(x) > limit_obs(x): print x, "EXCLUDED"
   #    else: print x

   plots = [plot_exp, plot_obs, dp1, dp2, zp3, zp12, kkg]
   #plots = [plot_exp, dp1, dp2, zp3, zp12]
   plotutil.plot(plots, "$M_{\\rm Z^{\\prime}}$ [GeV/$c^{2}$]",
    "limit on $\sigma(\\rm pp\\rightarrow Z^{\\prime} \\rightarrow t\\bar{t})$ [pb]",
    "limits.pdf", title_ul = '$L = 4.6$ fb$^{-1}$', xmin=1000, ymin=0.0, ymax=15.0,
    title_ur = 'all-hadronic, $\\sqrt{s} = 7$ TeV')
   plotutil.plot(plots, "$M_{\\rm Z^{\\prime}}$ [GeV/$c^{2}$]",
    "limit on $\sigma(\\rm pp\\rightarrow Z^{\\prime} \\rightarrow t\\bar{t})$ [pb]",
    "limits-log.pdf", title_ul = '$L = 4.6$ fb$^{-1}$', logy = True, xmin=1000, ymin=0.02, ymax=5.0,
    title_ur = 'all-hadronic, $\\sqrt{s} = 7$ TeV')


#debug_cls_plots('cls_limits-zp1900--bfb8402e28.db', 'lr__nll_diff')

#cwd = os.getcwd()
#os.chdir('../zp2011/')
#execfile("theory-xsecs.py")
#execfile("analysis.py")
#model_semilep = build_final_model(histogram_filter_semilep)
#os.chdir(cwd)

model = build_zp_model()
#model.combine(model_semilep)

for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

#cls_limits(model, 'all', ts = 'lhclike')

#model_summary(model)

# Option A:
#limits_zp(model, 1)

ks_test = ks_test(model, n = 500)
print "KS test result", ks_test

bayes_mc = bayesian_quantiles(model, input = 'toys:0', n = 50, mcmc_iterations = 100000)
print bayes_mc
# 
# bayes = bayesian_quantiles(model, input = 'data', n = 3, mcmc_iterations = 1000000)
# print bayes


# coeff = ml_fit_coefficients(model)
# print coeff

# fitres1 = ml_fit(model)
# print fitres1
# 
# fitres = ml_fit2(model)
# print fitres





# Option B:
# i. generate config files only, do not run theta locally:

#limits_zp(model, 0)

# ii. generate results from the db files in the analysis/cache directory:
#limits_zp(model, 1)


# (end option B)

#model_summary(model)
#report.write_html('./mttbar_zp_lowmass')

