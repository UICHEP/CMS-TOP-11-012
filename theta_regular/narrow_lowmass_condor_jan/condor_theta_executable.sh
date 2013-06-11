#! /bin/bash

export SCRAM_ARCH=slc5_amd64_gcc462
source /uscmst1/prod/sw/cms/shrc prod

DIR=$PWD
cd /uscms_data/d1/baites/CMSSW/CMSSW_5_2_5/src/
eval `scramv1 runtime -sh`
cd $DIR

echo $DIR
ls

/uscms_data/d1/baites/theta/testing/utils/theta-auto.py analysis.py 

