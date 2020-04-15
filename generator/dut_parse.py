#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM Auto Generator
#Function: parse top module RTL file and get info about interface 
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
import os 
import re
import sys
from generator.debug_log import *
from generator.interface import *
## Regex Function Get & Delete
format_get = lambda format,string : re.compile(format).findall(string)
format_delete = lambda format,string : re.compile(format).sub('',string)
## This Function Convert List to Dictionary
list2dict=lambda keys,vals : [ dict(zip(keys,item)) for item in vals]

class DUT_PARSE(object):
    def __init__(self,file_name=""):
        self.file_name=file_name
        self.contents="" #the rtl file contents
        self.module_name="" #the top module name 
        self.parameter={} # the module parameters
        self.port_list=[] #top module port name 
        self.direction_list=[]#top module port direction 
        self.msb_list=[]#top module port msb Note:may has parameter
        self.lsb_list=[]#top module port lsb Note:may has parameter

    #process the contents to delete the comments
    @DEBUG()
    def pre_process(self,file_name=""):
        if file_name!="":
            self.file_name=file_name
        elif self.file_name=="":
            return self.contents
        self.contents=open(self.file_name,'r').read()
        #delete all the comments
        self.contents=format_delete('(/{2,}.*?\n)|(?:/\*(\n|.)*?\*/)',self.contents)
        return self.contents

    #get all the parameters in the file 
    @DEBUG()
    def get_parameters(self,local=False):
        param_info=format_get('((?:parameter)|(?:localparam))\s*(\w*)\s*=\s*(.*?)\s*[;,)]',self.contents)
        parameter_dict_list=list2dict(['Type','Name','Value'],param_info)
        for param in parameter_dict_list:
            if param["Type"]=="parameter":#default only get parameter
                self.parameter[param["Name"]]=param["Value"]
            elif param["Type"]=="localparam" and local==True:#get parameter and localparam
                self.parameter[param["Name"]]=param["Value"]
        return self.parameter

    #get top module name and check 
    @DEBUG()
    def get_module(self,module_name=""):
        if module_name!="":
            self.module_name=module_name#get the setting module name 
        if self.contents=="": #no file set 
            return
        elif self.module_name=="": #no set module name  default set the module name = file name 
            (filepath,filename_we)=os.path.split(self.file_name)
            (self.module_name,ext) = os.path.splitext(filename_we)
        #the module name after "module" and before "#" or "("
        module_list=format_get('module\s*(\S*)\s*[#|\(]',self.contents)# get all module names in the file
        if (module_name not in module_list) and len(module_list)>0:# find the top module 
            ERROR("get_module: "+"Can't Find Module "+module_name+" in "+str(module_list)+" Set "+module_list[0])
            self.module_name=module_list[0] #no top module find ; set the first module in the file as top module
        else:
            return self.module_name

    #get top module port information
    @DEBUG()
    def get_ports(self):
        if self.contents=="":
            return
        mod_cmp=re.compile(r'''(module(\s+))(%s)''' %(self.module_name),re.VERBOSE)
        endmod_cmp=re.compile(r'''(endmodule(\s+))''',re.VERBOSE)
        begin=re.search(mod_cmp, self.contents).start() #the str "module" start
        #line_num=[m.start() for m in re.finditer(mod_cmp,file_content)] #get the line num
        end=re.search(endmod_cmp, self.contents).end() #the str "endmodule" end
        module_content=self.contents[begin:end] #find the contents only about top module 
        module_content=format_delete('(?:function)(?:.|\n)*(?:endfunction)',module_content)# delete function->endfunction  to avoid unvaild port
        module_content=format_delete('(?:task)(?:.|\n)*(?:endtask)',module_content)# delete task->endtask  to avoid unvaild port
        port_info = format_get('((?:input)|(?:output)|(?:inout))(?:\s+(?:(?:reg)|(?:wire)|(?:logic)))?\s+((?:signed)|(?:unsigned))?\s*(?:\[\s*(\S*)\s*:\s*(\S*)\s*\])?\s*(\w*)(?:\n|.)*?[;,)]',module_content)
        port_dict_list=list2dict(['IO_Type','SIGNED','MSB','LSB','Name'],port_info)# get top module port info
        for port_info in port_dict_list:
            self.port_list.append(port_info["Name"]) #get name 
            if port_info["IO_Type"]=="input": #get direction
                self.direction_list.append(format_bit(0)) #0=input 1=output 2=inout
            elif port_info["IO_Type"]=="output":#get direction
                self.direction_list.append(format_bit(1)) #0=input 1=output 2=inout
            else: #port_info["IO_Type"]=="inout":#0=input 1=output 2=inout #get direction
                self.direction_list.append(format_bit(2))
            if port_info["MSB"]=="":#get msb
                self.msb_list.append(format_bit(0))
            else:
                self.msb_list.append(format_bit(str(port_info["MSB"])))
            if port_info["LSB"]=="":#get lsb
                self.lsb_list.append(format_bit(0))
            else:
                self.lsb_list.append(format_bit(str(port_info["LSB"])))

    #parse the file module info
    @DEBUG()
    def parse(self,file_name="",module_name="",local=False):
        INFO("parse: "+"Get Information From RTL File")
        self.pre_process(file_name)
        self.get_parameters()
        self.get_module(module_name)
        self.get_ports()
        return

    def display_dut(self):
        print(self.file_name)
        print(self.contents)
        print(self.module_name)
        print(self.parameter)
        print(self.port_list)
        print(self.direction_list)
        print(self.msb_list)
        print(self.lsb_list)

