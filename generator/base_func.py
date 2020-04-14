#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  Design Platform for RTL development
#Function: some base function in the design platform
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
import os
import sys

#delete the char in a string default=" "
def del_content(content,to_del=" "):
    if isinstance(content,list):
        while to_del in content:
            content.remove(to_del)
        return content
    elif isinstance(content,str):
        while to_del in content:
            content=content.replace(to_del,"")
        return content
    else:
        return content 

#check file exist or path exist
def path_exists(dir=""):
    if os.path.exists(dir):
        return True
    else:
        return False


#get the abs directory
def get_abs_dir(dir=""):
    dir=del_content(dir," ")
    abs_dir=os.path.abspath(dir)+os.path.sep
    #abs_dir=os.path.dirname(os.path.abspath(dir)+os.path.sep)
    if abs_dir[-1]=="/":
        abs_dir=abs_dir[0:-1]
    if path_exists(abs_dir):
        return abs_dir
    else:
        return ""

