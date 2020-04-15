#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM Auto Generator
#Function: Functions for debug information generation
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#NOTE:
#logging.basicConfig is global 
#logger=logging.getLogger() just a object not global

import sys
import logging
#setting the config about the log
def log_cfg(log_level=1,log_fil=""):#the level is small the debug is more
    #DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S" #the data format
    LOG_FORMAT="%(asctime)s\t%(levelname)s:%(message)s"  #the debug format
    #LOG_FORMAT="%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"    
    if log_level==0:#level setting 
        log_level=logging.DEBUG
    elif log_level==1:
        log_level=logging.INFO
    elif log_level==2:
        log_level=logging.WARNING
    elif log_level==3:
        log_level=logging.ERROR
    elif log_level==4:
        log_level=logging.CRITICAL
    else:#default
        log_level=logging.INFO#default is info
    if log_fil!="": #log into the file
        formater=logging.Formatter(LOG_FORMAT)
        logger=logging.getLogger()
        logger.setLevel(log_level)
        #standard out
        stream_handler=logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formater)
        #file out
        file_handler=logging.FileHandler(log_fil)
        file_handler.setFormatter(formater)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        #logging.basicConfig(filename=log_fil, level=log_level, format=LOG_FORMAT,datefmt=DATE_FORMAT)
        #only has log but no stdout
    else:#log into the std
        logging.basicConfig(level=log_level, format=LOG_FORMAT,datefmt=DATE_FORMAT)

#--------------------------------------------------------
#Decorator  demo
#--------------------------------------------------------
#def log(func):
#    def wrapper(*args, **kw):
#        print('call %s():' % func.__name__)
#        return func(*args, **kw)
#    return wrapper


#def log(text):
#    def decorator(func):
#        def wrapper(*args, **kw):
#            print('%s %s():' % (text, func.__name__))
#            return func(*args, **kw)
#        return wrapper
#    return decorator



#using the decorator for debug each function
def DEBUG(text=""):
    def decorator(func):
        def wrapper(*args, **kw):
            if text!="":
                logging.debug(str("     ")+func.__name__+str(": ")+str(text))
            else:
                logging.debug(str("     ")+func.__name__)
            #logging.log(logging.DEBUG,string)
            return func(*args, **kw)
        return wrapper
    return decorator

#def DEBUG(string):
#    logging.debug(str("     ")+str(string))
#    #logging.log(logging.DEBUG,string)
#    return



#version 1
def INFO(string):#the info log 
    logging.info(str("      ")+string)
    #logging.log(logging.INFO,string)
    return

def WARNING(string):#the warning log 
    logging.warning(str("   ")+string)
    #logging.log(logging.WARNING,string)
    return


def ERROR(string):#the error log 
    logging.error(str("     ")+string)
    #logging.log(logging.ERROR,string)
    return


def CRITICAL(string):#the critical log 
    logging.critical(str("  ")+string)
    #logging.log(logging.CRITICAL,string)
    return



#version 2
#def INFO(string):#the info log 
#    print(str("      ")+string)
#    return
#
#def WARNING(string):#the warning log 
#    print(str("   ")+string)
#    return
#
#
#def ERROR(string):#the error log 
#    print(str("     ")+string)
#    return
#
#
#def CRITICAL(string):#the critical log 
#    print(str("  ")+string)
#    return
