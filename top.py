#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM Auto Generator
#Function: Top Run the Generator
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
import os
import argparse
from generator.base_func import *
from generator.debug_log import *
from generator.integration import *
#config the args
parser = argparse.ArgumentParser(prog="PROG",usage="%(prog)s [options]",description="UVM Generator Config")
#the debug config 
parser.add_argument("-d","--debug",type=int,choices=[0,1,2,3,4],default=1,help="Debug Level Set") #debug level
parser.add_argument("-l","--log",type=str,default="",help="Debug Log File") #debug log file name 
parser.add_argument("-i","--input",type=str,default="",help="Verify Progect Config File") #the instance config file 
parser.add_argument("-o","--output",type=str,default="./build",help="UVM Progect Output Directory")  #project output directory


#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#***** ***** ***** ***** run the flow ***** ***** ***** ***** ****
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
args=parser.parse_args()
#config the log 
log_cfg(log_level=args.debug,log_fil=args.log)
if not path_exists(args.input):
    CRITICAL("NO Config File Input")
    exit()
else:
    INFO("Running the Flow")
    integrate=INTEGRATION()
    integrate.cfg_file=args.input
    integrate.out_dir=args.output
    integrate.run_flow()
