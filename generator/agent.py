#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM Auto Generator
#Function: Functions for agent information get and process
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****

from generator.debug_log import *
from generator.interface import *
from generator.rdl import *

#the agent-sqr has RAL 
class REGISTER(object):
    def __init__(self):
        self.ral_file="" #ral_file and ral_name must has one
        self.ral_name="" #class name in uvm
        self.auto_predict=True#when ral==True,default auto_predict #False:explicit pedict
        self.rdl=RDL()
    
    #render the reg info to transfer to jinja2
    @DEBUG()
    def render_reg(self):
        INFO("render_reg: "+"Process "+self.ral_name+" Register Model Info")
        if self.ral_file!="" and self.ral_name!="":
            return dict(auto_predict=self.auto_predict,name=self.ral_name)
        else:
            return {}
    
    #get the System-RDL and parse the file get info
    @DEBUG()
    def format_reg(self):
        if self.ral_file!="":
            if isinstance(self.ral_file,str):
                tmp=[]
                tmp.append(self.ral_file)
                self.ral_file=tmp
            self.rdl.read_rdl(self.ral_file)# process the rdl file 
            self.ral_name=self.rdl.listener.ip_name #update the ral name same as file info
        return 


    def display_reg(self):
        print("RAL_FILE: "+str(self.ral_file))
        print("RAL_NAME: "+str(self.ral_name))
        print("PREDICT: "+str(self.auto_predict))


class AGENT(object):
    def __init__(self):
        self.name=""
        self.interface=INTERFACE() #the agent side interface 
        self.is_active=True #default has drv+sqr+monitor #False: just monitor
        self.response=False #default don't has response in driver
        self.ral=REGISTER() #default don't has uvm_reg_block in the agent #True:has
    
    #render the agent info to transfer to jinja2
    @DEBUG()
    def render_agent(self):
        INFO("render_agent: "+"Process "+self.name+" Agent Info")
        if self.name=="":
            return {}
        else:
            return dict(name=self.name,ral=self.ral.render_reg(),is_active=self.is_active,response=self.response,
                        clk_rst=self.interface.render_signals(self.interface.clk_rst),
                        port_list=self.interface.render_signals(self.interface.port_list),
                        param_list=self.interface.render_param())

    def display_agt(self):
        print("-------------------------------")
        print("AGENT NAME: "+str(self.name))
        self.interface.display_inf()
        print("AGENT ACTIVE: "+str(self.is_active))
        print("AGENT RESPONSE: "+str(self.response))
        self.ral.display_reg()
        return 
