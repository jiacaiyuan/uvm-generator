#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM-Generator
#Function: Functions for debug information generation
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
from generator.debug_log import *
from generator.interface import *
from generator.rdl import *
class REGISTER(object):
    def __init__(self):
        self.ral_file="" #ral_file and ral_name must has one
        self.ral_name="" #class name in uvm
        self.auto_predict=True#when ral==True,default auto_predict #False:explicit pedict
        self.rdl=RDL()
    
    def render_reg(self):
        if self.ral_name!="": #maybe change to self.ral_name!="" and self.ral_file!=""
            return dict(auto_predict=self.auto_predict,name=self.ral_name)
        else:
            return {}
    
    def format_reg(self):
        if self.ral_file!="":
            if isinstance(self.ral_file,str):
                tmp=[]
                tmp.append(self.ral_file)
                self.ral_file=tmp
            self.rdl.read_rdl(self.ral_file)
            self.ral_name=self.rdl.listener.ip_name
        return 


    def display_reg(self):
        print("RAL_FILE: "+str(self.ral_file))
        print("RAL_NAME: "+str(self.ral_name))
        print("PREDICT: "+str(self.auto_predict))


class AGENT(object):
    def __init__(self):
        self.name=""
        self.interface=INTERFACE()
        self.is_active=True #default has drv+sqr+monitor #False: just monitor
        self.response=False #default don't has response in driver
        self.ral=REGISTER() #default don't has uvm_reg_block in the agent #True:has
    
    def render_agent(self):
        if self.name=="":
            return {}
        else:
            return dict(name=self.name,ral=self.ral.render_reg(),is_active=self.is_active,response=self.response,
                        clk_rst=self.interface.render_signals(self.interface.clk_rst),
                        port_list=self.interface.render_signals(self.interface.port_list),
                        param_list=self.interface.render_param())#add later

    def display_agt(self):
        print("-------------------------------")
        print("AGENT NAME: "+str(self.name))
        self.interface.display_inf()
        print("AGENT ACTIVE: "+str(self.is_active))
        print("AGENT RESPONSE: "+str(self.response))
        self.ral.display_reg()
        return 
