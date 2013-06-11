#! /usr/bin/env python

# Python modules
import exceptions, math
from optparse import OptionParser


class Comparator:
    """ Compare the overlap between to set of events """
    
    def __init__(self, reference):
        """ Initialize the comparator by passing a reference file """  

        # Use run:lumi:id to identify the event
        self.__use_run_lumi_id = False
        # Map containing a counter per events        
        self.__event_counters = {}
        # Basic counters
        self.__reference_counter = 0
        self.__target_counter = 0
        self.__overlap_counter = 0
        
        # read the reference events
        file = open(reference)
        for line in file:
            eventinfo = map(lambda x: x.lstrip().rstrip(), line.split(':'))
            key = ''
            if len(eventinfo) >= 3:
                if int(eventinfo[2]) < 0: eventinfo[2] = str(abs(int(eventinfo[2])) + 2147483648)
                key = ':'.join(eventinfo[:3])
                self.__use_run_lumi_id = True
            elif len(eventinfo) == 2:
                if int(eventinfo[1]) < 0: eventinfo[1] = str(abs(int(eventinfo[1])) + 2147483648)
                key = ':'.join(eventinfo)
                self.__use_run_lumi_id = False
            else:
                raise exceptions.StandardError(
                    'Error in the reference file format.'
                )
            if key in self.__event_counters:
                print 'Warning: repeted entry %s in the reference file, skipping event.' % key
                continue
            self.__event_counters[key] = 1
            self.__reference_counter = self.__reference_counter + 1


    def __str__(self):
        """ Output string with basic statistices """
        string = 'Number of refence events : %d\n' % self.__reference_counter
        string = string + 'Number of target events  : %d\n' % self.__target_counter
        string = string + 'Number of overlap events : %d\n' % self.__overlap_counter
        string = string + 'Overlap/Reference ratio  : %f\n' % (
            float(self.__overlap_counter)/self.__reference_counter
        )
        string = string + 'Overlap/Target ratio     : %f\n' % (
            float(self.__overlap_counter)/self.__target_counter
        )
        string = string + 'Correlation              : %f' % (
            float(self.__overlap_counter)/math.sqrt(self.__reference_counter* self.__target_counter)
        )
        return string


    def compare(self, target):
        """ Compare the a target file againg the reference """
        # reset counters
        self.__target_counter = 0
        self.__overlap_counter = 0
        
        # read the reference events
        target_events = {}
        file = open(target)
        for line in file:
            eventinfo = map(lambda x: x.lstrip().rstrip(), line.split(':'))
            key = ''
            if self.__use_run_lumi_id and len(eventinfo) >= 3:
                if int(eventinfo[2]) < 0: eventinfo[2] = str(abs(int(eventinfo[2])) + 2147483648)
                key = ':'.join(eventinfo[:3])
            elif not self.__use_run_lumi_id and len(eventinfo) >= 3:
                if  int(eventinfo[2]) < 0: eventinfo[2] = str(abs(int(eventinfo[2])) + 2147483648)
                key = ':'.join([eventinfo[0],eventinfo[2]])
            elif not self.__use_run_lumi_id and len(eventinfo) == 2:
                if  int(eventinfo[1]) < 0: eventinfo[1] = str(abs(int(eventinfo[2])) + 2147483648)           
                key = ':'.join(eventinfo)
            else:
                raise exceptions.StandardError(
                    'Error in the target file format.'
                )
            if key in target_events:
                print 'Warning: repeted entry %s in the target file, skipping event.' % key
                continue
            if key in self.__event_counters:
                self.__event_counters[key] = self.__event_counters[key] + 1
                self.__overlap_counter = self.__overlap_counter + 1
                #print line.lstrip().rstrip()
            # else:
                # self.__event_counters[key] = 1
            self.__target_counter = self.__target_counter + 1
            target_events[key] = True
            

# Main function
if __name__ == "__main__":

    # Parsing options
    parser = OptionParser(usage = "usage: %prog [options]")

    parser.add_option(
        "--reference",
        action = "store",
        help = "File with reference events"
    )

    parser.add_option(
        "--target",
        action = "store",
        help = "File with events to be compare"
    )
 
    options, args = parser.parse_args()

    comparator = Comparator(options.reference)
    comparator.compare(options.target)
    print comparator
    

