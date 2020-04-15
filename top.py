#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  Design Platform for RTL development
#Function: Get the Parameter and run the Design Platform
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
import os
import argparse
from generator.base_func import *
from generator.debug_log import *
from generator.integration import *
#config the args
parser = argparse.ArgumentParser(prog="PROG",usage="%(prog)s [options]",description="Desgin Platfom Input Config")
#the debug config 
parser.add_argument("-d","--debug",type=int,choices=[0,1,2,3,4],default=1,help="Platform Debug Level") #debug level
parser.add_argument("-l","--log",type=str,default="",help="Platform Debug Log") #debug log file name 
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
    integrate=INTEGRATION()
    integrate.cfg_file=args.input
    integrate.out_dir=args.output
    integrate.run_flow()
