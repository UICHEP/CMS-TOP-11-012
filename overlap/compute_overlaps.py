#! /usr/bin/env python

from compute_overlap import *

# Main function
if __name__ == "__main__":

    # Computing overlap in data
    comparator = Comparator('high_mass_semileptonic_selection/data.txt')

    comparator.compare('low_mass_semileptonic_selection/data.txt')
    print 'BLP vs TLP : data'
    print comparator
    print

    comparator.compare('low_mass_dilepton_selection/data.txt')
    print 'BLP vs TDL : data'
    print comparator
    print

    comparator.compare('high_mass_allhadronic_selection/data.txt')
    print 'BLP vs BAH : data'
    print comparator
    print
    del comparator
        
    comparator = Comparator('low_mass_semileptonic_selection/data.txt')
    
    comparator.compare('low_mass_dilepton_selection/data.txt')
    print 'TLP vs TDL : data'
    print comparator
    print

    comparator.compare('high_mass_allhadronic_selection/data.txt')
    print 'TLP vs BAH : data'
    print comparator
    print
    del comparator

    comparator = Comparator('low_mass_dilepton_selection/data.txt')
        
    comparator.compare('high_mass_allhadronic_selection/data.txt')
    print 'TDL vs BAH : data'
    print comparator
    print
    del comparator
    
    
    # Computing overlap in zp500
    comparator = Comparator('low_mass_semileptonic_selection/zp500w5.txt')
        
    comparator.compare('low_mass_dilepton_selection/zp500w5.txt')
    print 'TLP vs TDL : zp500w5'
    print comparator
    print
    del comparator

    # Computing overlap in zp500
    comparator = Comparator('low_mass_semileptonic_selection/zp750w7.txt')
    
    comparator.compare('low_mass_dilepton_selection/zp750w7.txt')
    print 'TLP vs TDL : zp750w7'
    print comparator
    print
    del comparator
        
    # Computing overlap in zp1000    
    comparator = Comparator('high_mass_semileptonic_selection/zp1000w10.txt')
    
    comparator.compare('low_mass_semileptonic_selection/zp1000w10.txt')
    print 'BLP vs TLP : zp1000w10'
    print comparator
    print
    
    comparator.compare('low_mass_dilepton_selection/zp1000w10.txt')
    print 'BLP vs TDL : zp1000w10'
    print comparator
    print
    del comparator

    comparator = Comparator('low_mass_semileptonic_selection/zp1000w10.txt')
    
    comparator.compare('low_mass_dilepton_selection/zp1000w10.txt')
    print 'TLP vs TDL : zp1000w10'
    print comparator
    print
    del comparator
        
    # Computing overlap in zp2000
    comparator = Comparator('high_mass_semileptonic_selection/zp2000w20.txt')
    
    comparator.compare('low_mass_semileptonic_selection/zp2000w20.txt')
    print 'BLP vs TLP : zp2000w20'
    print comparator
    print
    
    comparator.compare('low_mass_dilepton_selection/zp2000w20.txt')
    print 'BLP vs TDL : zp2000w20'
    print comparator
    print

    comparator.compare('high_mass_allhadronic_selection/zp2000w20.txt')
    print 'BLP vs BAH : zp2000w20'
    print comparator
    print
    
    del comparator

    comparator = Comparator('low_mass_semileptonic_selection/zp2000w20.txt')
    
    comparator.compare('low_mass_dilepton_selection/zp2000w20.txt')
    print 'TLP vs TDL : zp2000w20'
    print comparator
    print

    comparator.compare('high_mass_allhadronic_selection/zp2000w20.txt')
    print 'TLP vs BAH : zp2000w20'
    print comparator
    print
    
    del comparator

    comparator = Comparator('low_mass_dilepton_selection/zp2000w20.txt')
        
    comparator.compare('high_mass_allhadronic_selection/zp2000w20.txt')
    print 'TDP vs BAH : zp2000w20'
    print comparator
    print
    
    del comparator
    
    
    # Computing overlap in zp3000
    comparator = Comparator('high_mass_semileptonic_selection/zp3000w30.txt')
        
    comparator.compare('low_mass_dilepton_selection/zp3000w30.txt')
    print 'BLP vs TDL : zp3000w30'
    print comparator
    print
    del comparator
