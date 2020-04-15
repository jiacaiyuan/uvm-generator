#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM Auto Generator
#Function: Functions for json-config process
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****

import chardet
import json
import traceback
from generator.debug_log import *
from generator.base_func import *
from generator.interface import *
from generator.agent import *

class JSONCFG_PARSE(object):
    def __init__(self,fil_name=""):
        self.fil_name=fil_name #the json file name 
        self.contents=""  #the content of the json file
        self.top_module=""#the top module rtl file 
        self.top_name="" # the top module name 
        self.agent_list=[] #the agent list 
        

    #check the json file top level is a dict or a list
    def check_dict(self,contents):
        if isinstance(contents,dict):
            return True
        else:
            return False

    #check and process the list 
    def check_list(self,contents):
        if isinstance(contents,list):
            return del_content(contents)
        elif isinstance(contents,str) or isinstance(contents,int):
            tmp=[]
            tmp.append(del_content(str(contents)))
            return tmp
        else:
            return []

    #check and process the bool type 
    def check_bool(self,contents):
        if contents==True:
            return True
        elif contents==False:
            return False
        elif isinstance(contents,str):
            contents=del_content(contents)
            if contents.lower() =="true":
                return True
            elif contents.lower() =="false":
                return False
            elif contents.lower() =="": #the blank means false
                return False
            else:
                return True#has the key is true
        else:
            return True


    #check and process the identifier
    def check_identifier(self,contents):
        if not isinstance(contents,str):
            return ""
        elif re.match("^[A-Za-z0-9_$-]*$",str(contents)) and re.match("^[A-Za-z_-]*$",str(contents)[0]):
            return str(contents)
        else:
            ERROR("check_identifier: "+"String Illegal "+str(contents))

    #read the json config file
    @DEBUG()
    def json_parse_ini(self,fil_name=""):
        if fil_name != "":
            self.fil_name=fil_name
        with open(self.fil_name, 'rb') as f:
            f_encoding = chardet.detect(f.read())["encoding"]
        with open(self.fil_name, encoding=f_encoding) as j_file:
            try:
                self.contents =json.load(j_file)
            except Exception:
                ERROR("read_json: "+"Json File Format Illegal "+str(self.fil_name))
                traceback.print_exc()#print which/where json file wrong
        if not self.check_dict(self.contents):#check the top
            CRITICAL("read_json: "+"Json File Must Be Dict "+str(self.fil_name))
            self.contents=""
        f.close()
        return self.contents

    #parse the module part 
    @DEBUG()
    def parse_module(self):
        if "TOP_MODULE" in list(self.contents.keys()):
            self.top_module=get_abs_dir(del_content(str(self.contents["TOP_MODULE"])))# if no "TOP_MODULE" is fine 
            if not path_exists(self.top_module):#check and find the module rtl file 
                ERROR("parse_module: "+str(self.top_module)+" Can't Find File "+str(self.contents["TOP_MODULE"]))
                self.top_module=""
        if "NAME" in list(self.contents.keys()):#find the module name 
            self.top_name=del_content(str(self.contents["NAME"]))# if no "NAME" is fine it can auto find or set auto
        return

    #parse the ral info 
    @DEBUG()
    def parse_ral(self,agt,ral_dict={}):
        if "AUTO_PREDICT" in list(ral_dict.keys()):
            agt.ral.auto_predict=self.check_bool(ral_dict["AUTO_PREDICT"]) #get predict set; if no has default value 
        if "NAME" in list(ral_dict.keys()):#if no  get from system-rdl 
            agt.ral.ral_name=self.check_identifier(ral_dict["NAME"])
        if "SystemRDL" in list(ral_dict.keys()):#get systemRDL file 
            agt.ral.ral_file=get_abs_dir(del_content(str(ral_dict["SystemRDL"])))
            if not path_exists(agt.ral.ral_file):# check file exists
                ERROR("parse_ral: "+str(agt.ral.ral_file)+" Can't Find")
                agt.ral.ral_file=""
        return

    #parse the interface info
    @DEBUG()
    def parse_interface(self,agt,inf_dict={}):
        if ("PARAMETER" in list(inf_dict.keys())):
            if isinstance(inf_dict["PARAMETER"],dict):
                agt.interface.parameter=inf_dict["PARAMETER"]#get parameter info in each agent 
            else:
                ERROR("parse_interface: "+"Parameter Must Be a Dict")
        if("PORTS" in list(inf_dict.keys())):#get port info in each agent 
            if isinstance(inf_dict["PORTS"],dict):
                if "NAME" in list(inf_dict["PORTS"].keys()):
                    agt.interface.name_list=self.check_list(inf_dict["PORTS"]["NAME"])
                if "DIRECTION" in list(inf_dict["PORTS"].keys()):
                    agt.interface.direction_list=format_list(self.check_list(inf_dict["PORTS"]["DIRECTION"]))
                if "MSB" in list(inf_dict["PORTS"].keys()):
                    agt.interface.msb_list=format_list(self.check_list(inf_dict["PORTS"]["MSB"]))
                if "LSB" in list(inf_dict["PORTS"].keys()):
                    agt.interface.lsb_list=format_list(self.check_list(inf_dict["PORTS"]["LSB"]))
            else:
                ERROR("parse_interface: "+"PORTS Must Be a Dict")
        return 

    #parse the agent  info
    @DEBUG()
    def parse_agents(self):
        INFO("parse_agents: "+"Analysis The JSON Config File About Agents")
        if "AGENTS" in list(self.contents.keys()):#get agent 
            agent_contents=self.contents["AGENTS"]
            if self.check_dict(agent_contents):
                for key in list(agent_contents.keys()):
                    if self.check_dict(agent_contents[key]):
                        agt=AGENT()
                        agt.name=key
                        if "ACTIVE" in list(agent_contents[key].keys()):#default True
                            agt.is_active=self.check_bool(agent_contents[key]["ACTIVE"])
                        if "RESPONSE" in list(agent_contents[key].keys()):#default False
                            agt.response=self.check_bool(agent_contents[key]["RESPONSE"])
                        if "RAL" in list(agent_contents[key].keys()):
                            if self.check_dict(agent_contents[key]["RAL"]):
                                self.parse_ral(agt,agent_contents[key]["RAL"])#parse ral
                            else:
                                ERROR("parse_agents: "+"RAL Must Be a Dict")
                        if "INTERFACE" in list(agent_contents[key].keys()):
                            if self.check_dict(agent_contents[key]["INTERFACE"]):
                                self.parse_interface(agt,agent_contents[key]["INTERFACE"])#parse interface 
                            else:
                                ERROR("parse_agents: "+"INTERFACE Must Be a Dict")
                        self.agent_list.append(agt)
                    else:
                        ERROR("parse_agents: "+"Each Agent Must Be a Dict")
            else:
                ERROR("parse_agents: "+"AGENTS Must Be a Dict")

    #parse the config file info
    @DEBUG()
    def parse(self,fil_name=""):
        INFO("parse: "+"Analysis Json Config File")
        self.json_parse_ini(fil_name)
        self.parse_module()
        self.parse_agents()
        

    def display_cfg(self):
        print(self.top_module)
        print(self.top_name)
        for agt in self.agent_list:
            agt.display_agt()
        return 
