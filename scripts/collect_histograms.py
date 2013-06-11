#! /usr/bin/env python

import sys
from ROOT import TFile

# Try to crate a new file to merge the histograms
output = TFile(sys.argv[1], 'NEW')

# List of histograms
histograms = {}

# Loop over all the files
for file in sys.argv[2:]:

    input = TFile(file)
    keys = input.GetListOfKeys()

    # Loop over all the histograms
    for key in keys:

        # Only add histogram with different names
        hname = key.GetName()
        if hname in histograms:
            continue
        
        # Clone and save the histogram 
        histogram = input.Get(hname).Clone()
        output.cd()
        histogram.Write()

        # Save the histogram name 
        histograms[hname] = True

    input.Close()
