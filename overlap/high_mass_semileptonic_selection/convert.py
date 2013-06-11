#! /usr/bin/env python

import sys

outname = sys.argv[1].split('.')[0]+'_convenrt.'+sys.argv[1].split('.')[1]

input = open(sys.argv[1])
output = open(outname, 'w')
for line in input:
    eventinfo = map(lambda x: x.lstrip().rstrip(), line.split(':'))  
    output.write(':'.join([eventinfo[0],eventinfo[2]])+'\n')
