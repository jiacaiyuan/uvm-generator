import chardet
import json
import traceback
from generator.debug_log import *
from generator.agent import *
from generator.interface import *
from generator.base_func import *
class JSONCFG_PARSE(object):
    def __init__(self,fil_name=""):
        self.fil_name=fil_name #the json file name 
        self.contents=""  #the content of the json file
        self.top_module=""
        self.top_name=""
        self.agent_list=[]
        

    #check the json file top level is a dict or a list
    @DEBUG()
    def check_dict(self,contents):
        if isinstance(contents,dict):
            return True
        else:
            return False

    def check_list(self,contents):
        if isinstance(contents,list):
            return del_content(contents)
        elif isinstance(contents,str) or isinstance(contents,int):
            tmp=[]
            tmp.append(del_content(str(contents)))
            return tmp
        else:
            return []

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



    def check_identifier(self,contents):
        if not isinstance(contents,str):
            return ""
        elif re.match("^[A-Za-z0-9_$-]*$",str(contents)) and re.match("^[A-Za-z_-]*$",str(contents)[0]):
            return str(contents)
        else:
            ERROR("check_identifier: "+"String Illegal "+str(contents))

    #read the json file
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

    def parse_module(self):
        if "TOP_MODULE" in list(self.contents.keys()):
            self.top_module=get_abs_dir(del_content(str(self.contents["TOP_MODULE"])))
            if not path_exists(self.top_module):
                ERROR("parse_module: "+str(self.top_module)+" Can't Find File "+str(self.contents["TOP_MODULE"]))
                self.top_module=""
        if "NAME" in list(self.contents.keys()):
            self.top_name=del_content(str(self.contents["NAME"]))
        return

    def parse_ral(self,agt,ral_dict={}):
        if "AUTO_PREDICT" in list(ral_dict.keys()):
            agt.ral.auto_predict=self.check_bool(ral_dict["AUTO_PREDICT"])
        if "NAME" in list(ral_dict.keys()):
            agt.ral.ral_name=self.check_identifier(ral_dict["NAME"])
        if "SystemRDL" in list(ral_dict.keys()):
            agt.ral.ral_file=get_abs_dir(del_content(str(ral_dict["SystemRDL"])))
            if not path_exists(agt.ral.ral_file):
                ERROR("parse_ral: "+str(agt.ral.ral_file)+" Can't Find")
                agt.ral.ral_file=""
        return

    def parse_interface(self,agt,inf_dict={}):
        if ("PARAMETER" in list(inf_dict.keys())):
            if isinstance(inf_dict["PARAMETER"],dict):
                agt.interface.parameter=inf_dict["PARAMETER"]
            else:
                ERROR("parse_interface: "+"Parameter Must Be a Dict")
        if("PORTS" in list(inf_dict.keys())):
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



    def parse_agents(self):
        if "AGENTS" in list(self.contents.keys()):
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
                                self.parse_ral(agt,agent_contents[key]["RAL"])
                            else:
                                ERROR("parse_agents: "+"---------------------------3")
                        if "INTERFACE" in list(agent_contents[key].keys()):
                            if self.check_dict(agent_contents[key]["INTERFACE"]):
                                self.parse_interface(agt,agent_contents[key]["INTERFACE"])
                            else:
                                ERROR("parse_agents: "+"---------------------------4")
                        self.agent_list.append(agt)
                    else:
                        ERROR("parse_agents: "+"---------------------------2")
            else:
                ERROR("parse_agents: "+"---------------------------1")

    def parse(self,fil_name=""):
        self.json_parse_ini(fil_name)
        self.parse_module()
        self.parse_agents()
        

    def display_cfg(self):
        print(self.top_module)
        print(self.top_name)
        for agt in self.agent_list:
            agt.display_agt()
        return 
