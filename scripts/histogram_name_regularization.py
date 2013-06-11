#! /usr/bin/env python

import sys, os
from ROOT import TFile

# File type 
type = os.path.basename(sys.argv[1]).split('.')[0]

# Open input file
input = TFile(sys.argv[1])
keys = input.GetListOfKeys()

# Open output file
output = TFile(sys.argv[2], 'RECREATE')

# Loop over all the histograms
for key in keys:

    hname = key.GetName()
    pname = hname.split('__')[1] 
    nname = ''

    # Clone and save the histogram 
    histogram = input.Get(hname).Clone()
        
    # Convertion for all hadronic files
    if type == 'high_mass_allhadronic_selection':
        if 'zp' in pname:
            mass = float(pname.split('w')[0].split('zp')[1])
            width = float(pname.split('w')[1])
            ratio = width/mass
            if ratio == 0.1:
                nname = hname.replace(pname, 'zp%0.fw10p' % mass)
            else:
                nname = hname.replace(pname, 'zp%0.fw1p' % mass)
        elif 'rskkg' in pname:
            nname = hname.replace('rskkg', 'rsg')

    # Convertion for high mass semileptonic
    elif type == 'high_mass_semileptonic_selection':
        if 'zp' in pname:
            if 'wide' in pname:
                nname = hname.replace('wide', 'w10p')
            else:
                nname = hname.replace(pname, '%sw1p' % pname)

    # Convertion for low mass semileptonic
    elif type == 'low_mass_semileptonic_selection':
        if 'zp' in pname:
            if 'wide' in pname:
                nname = hname.replace(pname, pname.replace('wide','') + 'w10p')
            else:
                nname = hname.replace(pname, '%sw1p' % pname)
        elif 'kkgluon' in pname:
            nname = hname.replace('kkgluon', 'rsg')

    # Convertion for low mass dilepton
    elif type == 'narrow_low_mass_dilepton_selection':
        if 'zp' in pname:
            nname = hname.replace(pname, '%sw1p' % pname)
        elif 'WJets' in pname:
            nname =  hname.replace(pname, 'wjets')
    elif type == 'wide_low_mass_dilepton_selection':
        if 'zp' in pname:
            nname = hname.replace(pname, '%sw10p' % pname)
        elif 'WJets' in pname:
            nname =  hname.replace(pname, 'wjets')
    
    else:
        raise NameError('Unknown input file type.')

    if nname != '':
        print '%s -> %s' % (hname, nname)
        histogram.SetName(nname)

    output.cd()
    histogram.Write()
