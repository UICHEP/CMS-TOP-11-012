#! /bin/bash

./histogram_name_regularization.py ../theta/high_mass_allhadronic_selection.root high_mass_allhadronic_selection.root
./histogram_name_regularization.py ../theta/high_mass_semileptonic_selection.root high_mass_semileptonic_selection.root
./histogram_name_regularization.py ../theta/low_mass_semileptonic_selection.root low_mass_semileptonic_selection.root
./histogram_name_regularization.py ../theta/narrow_low_mass_dilepton_selection.root narrow_low_mass_dilepton_selection.root 
./histogram_name_regularization.py ../theta/wide_low_mass_dilepton_selection.root wide_low_mass_dilepton_selection.root 

