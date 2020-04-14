#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM-Generator
#Function: Functions for debug information generation
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
from generator.debug_log import *
from generator.base_func import *
import re
def format_bit(bit):
    if isinstance(bit,int):
        bit=bit
    elif isinstance(bit,str):
        bit=del_content(bit)
        if bit.isdigit():
            bit=int(bit)
        elif re.match("0(x|X)[0-9a-fA-F]",bit):
            bit=int(bit,16)
        else:
            bit=str(bit)
    else:
        ERROR("format_bit: "+"Unknow Signal Bit Info "+str(bit))
        bit=str(bit)
    return bit

def format_list(list_to_form):
    for i in range(len(list_to_form)):
        list_to_form[i]=format_bit(list_to_form[i])
    return list_to_form


class SIGNAL(object):
    def __init__(self):
        self.name=""
        self.directon="" #0=input 1=output 2=inout
        self.msb=""
        self.lsb=""
        self.bits=[]
        self.status=[]


    def check_bit(self,bit,param_dict={}):
        if isinstance(bit,int) or (isinstance(bit,str) and bit.isdigit()) or (isinstance(bit,str) and re.match("0(x|X)[0-9a-fA-F]",bit)):
            return True
        if isinstance(bit,str)and(not bit.isdigit())and(not re.match("0(x|X)[0-9a-fA-F]",bit)):
            flag=0
            for key in list(param_dict.keys()):
                if key in bit:
                    flag=1
                    return True
            if flag==0:
                WARNING("check_bit: "+self.name+" Bit:"+bit)
                return False

    def check_sig(self,param_dict={}):
        if self.name=="":
            ERROR("check_sig: "+"Signal Name Illegal")
        if self.direction>2:
            ERROR("check_sig: "+"Signal Direction Illegal")
        msb_flag=self.check_bit(self.msb,param_dict)
        lsb_flag=self.check_bit(self.lsb,param_dict)
        return(msb_flag,lsb_flag)









    def display_sig(self):
        if self.direction==0:
            dir_str="input"
        elif self.direction==1:
            dir_str="output"
        elif self.direction==2:
            dir_str="inout"
        else:
            dir_str="xxx"
        bit_str=str(self.msb)+":"+str(self.lsb)
        print("Signal: "+str(self.name)+" "+dir_str+" "+bit_str)



class INTERFACE(object):
    def __init__(self):
        self.name_list=[]
        self.direction_list=[]
        self.msb_list=[]
        self.lsb_list=[]

        self.parameter={}
        self.clk_rst=[]
        self.port_list=[] #without clk and rst signal




    def update_param(self,bits,global_param_dict):
        for key in list(self.parameter.keys()):
            if key in bits:
                return
            else:
                continue
        for key in list(global_param_dict.keys()):
            if key in bits:
                self.parameter[key]=global_param_dict[key]
            else:
                continue
        return

    def check_update_list(self,glb_name_list=[],glb_direction_list=[],glb_msb_list=[],glb_lsb_list=[]):
        if len(self.name_list)==0:
            self.name_list=glb_name_list
            self.direction_list=glb_direction_list
            self.msb_list=glb_msb_list
            self.lsb_list=glb_lsb_list
        else:
            #update length
            update_direction=False
            update_msb=False
            update_lsb=False
            if len(self.name_list)!=len(self.direction_list):
                ERROR("check_update_list: "+"Name Num!= Direction Num "+str(self.name_list))
                self.direction_list=[]
                update_direction=True
                for i in range(len(self.name_list)):
                    self.direction_list.append(0)#default input
            if len(self.name_list)!=len(self.msb_list):
                ERROR("check_update_list: "+"Name Num!= MSB Num "+str(self.name_list))
                self.msb_list=[]
                update_msb=True
                for i in range(len(self.name_list)):
                    self.msb_list.append(0)#default 0
            if len(self.name_list)!=len(self.lsb_list):
                ERROR("check_update_list: "+"Name Num!= Direction Num "+str(self.name_list))
                self.lsb_list=[]
                update_lsb=True
                for i in range(len(self.name_list)):
                    self.lsb_list.append(0)#default 0
            #update value
            for i in range(len(glb_name_list)):
                if glb_name_list[i] in self.name_list:
                    if update_direction:
                        self.direction_list[self.name_list.index(glb_name_list[i])]=glb_direction_list[i]
                    elif self.direction_list[self.name_list.index(glb_name_list[i])]!=glb_direction_list[i]:
                        ERROR("check_update_list: "+"Direction Diff Config "+str(glb_name_list[i]))
                        self.direction_list[self.name_list.index(glb_name_list[i])]=glb_direction_list[i]
                    if update_msb:
                        self.msb_list[self.name_list.index(glb_name_list[i])]=glb_msb_list[i]
                    elif self.msb_list[self.name_list.index(glb_name_list[i])]!=glb_msb_list[i]:
                        ERROR("check_update_list: "+"MSB Diff Config "+str(glb_name_list[i]))
                        self.msb_list[self.name_list.index(glb_name_list[i])]=glb_msb_list[i]
                    if update_lsb:
                        self.lsb_list[self.name_list.index(glb_name_list[i])]=glb_lsb_list[i]
                    elif self.lsb_list[self.name_list.index(glb_name_list[i])]!=glb_lsb_list[i]:
                        ERROR("check_update_list: "+"LSB Diff Config "+str(glb_name_list[i]))
                        self.lsb_list[self.name_list.index(glb_name_list[i])]=glb_lsb_list[i]







    def format_inf(self,global_param_dict={},glb_name_list=[],glb_direction_list=[],glb_msb_list=[],glb_lsb_list=[]):
        self.check_update_list(glb_name_list,glb_direction_list,glb_msb_list,glb_lsb_list)
        for i in range(min(len(self.name_list),len(self.direction_list),len(self.msb_list),len(self.lsb_list))):
            sig=SIGNAL()
            sig.name=self.name_list[i]
            sig.direction=format_bit(self.direction_list[i])
            sig.msb=format_bit(self.msb_list[i])
            sig.lsb=format_bit(self.lsb_list[i])
            (msb_flag,lsb_flag)=sig.check_sig(self.parameter)
            if not msb_flag:
                self.update_param(sig.msb,global_param_dict)
            if not lsb_flag:
                self.update_param(sig.lsb,global_param_dict)
            if re.search(r'((clock)|(clk)|(rst)|(reset))',self.name_list[i].lower()):
                self.clk_rst.append(sig)
            else:
                self.port_list.append(sig)


    
    
    
    
    
    

    def render_param(self):
        param_rend_list=[]
        for k in list(self.parameter.keys()):
            if isinstance(self.parameter[k],int):
                param_rend_list.append(dict(type="int",key=str(k),value=self.parameter[k]))
            elif isinstance(self.parameter[k],str) and self.parameter[k].isdigit(): #10 dec-num
                param_rend_list.append(dict(type="int",key=str(k),value=int(self.parameter[k])))
            elif isinstance(self.parameter[k],str) and (re.match("0(x|X)[0-9a-fA-F]",self.parameter[k])): #16 hex-num
                param_rend_list.append(dict(type="int",key=str(k),value=int(self.parameter[k],16)))
            elif isinstance(self.parameter[k],str): #just string
                param_rend_list.append(dict(type="string",key=str(k),value="\""+str(self.parameter[k])+"\""))
            else:
                ERROR("render_param: "+"Parameter Illegal")
        return param_rend_list


    def render_signals(self,sig_list):
        render_sig_list=[]
        for port in sig_list:
            if port.msb==port.lsb:
                bit_str=""
            else:
                bit_str="["+str(port.msb)+":"+str(port.lsb)+"]"
            if port.direction==0:
                render_sig_list.append(dict(direction="input",name=port.name,bit_info=bit_str))
            elif port.direction==1:
                render_sig_list.append(dict(direction="output",name=port.name,bit_info=bit_str))
            elif port.direction==2:
                render_sig_list.append(dict(direction="inout",name=port.name,bit_info=bit_str))
            else:
                ERROR("render_param: "+"Clk or Rst Port Illegal")
        return render_sig_list

    def display_inf(self):
        print(self.name_list)
        print(self.direction_list)
        print(self.msb_list)
        print(self.lsb_list)
        print(self.parameter)
        for port in self.clk_rst+self.port_list:
            port.display_sig()
