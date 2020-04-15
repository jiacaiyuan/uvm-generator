#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  UVM Auto Generator
#Function: Functions for integration
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****

import re
import shutil
from copy import deepcopy
from generator.base_func import *
from generator.debug_log import *
from generator.jsoncfg_parse import *
from generator.dut_parse import *
from generator.interface import *
from jinja2 import Environment,FileSystemLoader

class INTEGRATION(object):
    def __init__(self):
        self.jscfg=JSONCFG_PARSE()
        self.dut_parse=DUT_PARSE()
        self.cfg_file=""
        self.dut_name=""
        self.out_dir=""
        self.agent_list=[]
        self.render_agent_list=[]
        self.pkg_str=""
        self.template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"../template/")
        self.env=Environment(loader = FileSystemLoader(self.template_path))
        self.agt_template_list=["_agent_cfg.svh","_sequencer.svh","_driver.svh","_monitor.svh","_agent.svh"]
        self.reg_adp_template="_reg_adapter.svh"
        self.env_template_list=["_env_cfg.svh","_virtual_sequencer.svh","_env.svh"]
        self.sequence_template_list=["_transaction.svh","_sequence_base.svh"]
        self.sequence_cfg_template="_sequence_cfg.svh"
        self.testcase_template="_base_test.svh"
        self.inf_template="_interface.svh"
        self.harness_template="_harness.svh"
        #self.agt_template_list=["_interface.svh","_transaction.svh","_driver.svh",
        #"_monitor.svh","_sequencer.svh","_agent_cfg.svh","_agent.svh","_reg_adapter.svh",
        #"_sequence_base.svh"]
        #self.global_template_list=["_sequence_cfg.svh","_virtual_sequencer.svh",
        #"_env_cfg.svh","_env.svh",
        #"_base_test.svh","_harness.svh"]
        
        #order: rtl,sequence,agent,reg,env,testcase,sim

    #parse the config file and dut file 
    @DEBUG()
    def parse(self,cfg_file):
        INFO("parse: "+"All Available Info")
        if cfg_file!="":
            self.cfg_file=cfg_file
        self.cfg_file=get_abs_dir(del_content(str(self.cfg_file)))
        if not path_exists(self.cfg_file):
            CRITICAL("parse: "+"Can't Find Config File")
            INFO("parse: "+"Default Flow")
            agt=AGENT()
            agt.name="AUTO_AGENT"
            self.agent_list.append(agt)
            self.render_agent_list.append(agt.render_agent())
            return
        self.jscfg.parse(self.cfg_file)
        self.dut_parse.parse(self.jscfg.top_module,self.jscfg.top_name)
        if self.dut_parse.module_name!="":
            self.dut_name=self.dut_parse.module_name
        else:
            self.dut_name="AUTO_DUT"#set auto name 
        self.agent_list=self.jscfg.agent_list
        if len(self.agent_list)==0:#no agent config 
            agt=AGENT()
            agt.name="AUTO_AGENT"
            self.agent_list.append(agt)
        for i in range(len(self.agent_list)):#format the info 
            self.agent_list[i].interface.format_inf(self.dut_parse.parameter,self.dut_parse.port_list,
                                             self.dut_parse.direction_list,self.dut_parse.msb_list,
                                             self.dut_parse.lsb_list)
            self.agent_list[i].ral.format_reg()
        for agt in self.agent_list:#render
            self.render_agent_list.append(agt.render_agent())
        return



    #change and build work directory
    @DEBUG()
    def chg_out_dir(self):
        if not path_exists(self.out_dir):
            os.makedirs(self.out_dir)#generate dirs
        self.out_dir=get_abs_dir(self.out_dir)#get the abs directory
        os.chdir(self.out_dir)#change into the project dir 
        if not path_exists(str(self.dut_name)+"_verify"):
            os.mkdir(str(self.dut_name)+"_verify")
        os.chdir(str(self.dut_name)+"_verify")
        self.out_dir=get_abs_dir("./")
        return self.out_dir



    #generate the project directory
    @DEBUG()
    def build_dir(self):
        INFO("build_ip_dir: "+"Build Project Directory")
        os.chdir(self.out_dir)#change into the project dir 
        for agt in self.agent_list:
            if not path_exists(agt.name+str("_agent")):
                os.mkdir(agt.name+str("_agent"))
            if (agt.ral.ral_file!="") and (agt.ral.ral_file!=[]) and (not path_exists("reg_model")):
                os.mkdir("reg_model")
        if not path_exists("env"):
            os.mkdir("env")
        if not path_exists("sim"):
            os.mkdir("sim")
        if not path_exists("sequence"):
            os.mkdir("sequence")
        if not path_exists("testcase"):
            os.mkdir("testcase")
        if not path_exists("rtl"):
            os.mkdir("rtl")
        return

    #rander the template base 
    def render_integrate_base(self,tmp,agent=AGENT()):
        if agent.ral.ral_name!="":
            UVM_RAL=True
        else:
            UVM_RAL=False
        template=self.env.get_template(tmp)
        content=template.render(
        MODULE=self.dut_name,
        MASTER_SLAVE_BUS=agent.name,
        param_list=agent.interface.render_param(),
        clk_rst=agent.interface.render_signals(agent.interface.clk_rst),
        port_list=agent.interface.render_signals(agent.interface.port_list),
        response=agent.response,
        UVM_RAL=UVM_RAL,
        agt_list=self.render_agent_list,
        ral=agent.ral.render_reg()
        )
        return content

    #fill the rtl and interface file 
    @DEBUG()
    def fill_rtl(self):
        os.chdir(self.out_dir)
        os.chdir("rtl")
        if self.dut_parse.file_name!="":
            shutil.copy( self.dut_parse.file_name,"./")#copy rtl file 
        for agent in self.agent_list:#gen the interface.sv
            content=self.render_integrate_base(self.inf_template,agent)
            with open("./"+str(agent.name)+str(self.inf_template).split(".")[0]+str(".sv"),"w") as fp:
                fp.write(content)
        os.chdir(self.out_dir)
        return

    
    #fill the sequence sequence_cfg and transaction 
    @DEBUG()
    def fill_sequence(self):
        os.chdir(self.out_dir)
        os.chdir("sequence")
        content=self.render_integrate_base(self.sequence_cfg_template)
        with open("./"+str(self.dut_name)+str(self.sequence_cfg_template).split(".")[0]+str(".sv"),"w") as fp:
            fp.write(content)
        self.pkg_str=self.pkg_str+str("`include \""+str(self.dut_name)+str(self.sequence_cfg_template).split(".")[0]+str(".sv")+"\"\n")
        for agent in self.agent_list:
            for t in self.sequence_template_list:
                content=self.render_integrate_base(t,agent)
                with open("./"+str(agent.name)+str(t).split(".")[0]+str(".sv"),"w") as fp:
                    fp.write(content)
                self.pkg_str=self.pkg_str+str("`include \""+str(agent.name)+str(t).split(".")[0]+str(".sv")+"\"\n")
        os.chdir(self.out_dir)
        return




    #fill the agent sv file 
    @DEBUG()
    def fill_agents(self):
        for agent in self.agent_list:
            os.chdir(self.out_dir)
            os.chdir(agent.name+str("_agent"))
            for t in self.agt_template_list:
                content=self.render_integrate_base(t,agent)
                with open("./"+str(agent.name)+str(t).split(".")[0]+str(".sv"),"w") as fp:
                    fp.write(content)
                self.pkg_str=self.pkg_str+str("`include \""+str(agent.name)+str(t).split(".")[0]+str(".sv")+"\"\n")
        os.chdir(self.out_dir)
        return

    #fill the env sv file 
    @DEBUG()
    def fill_env(self):
        os.chdir(self.out_dir)
        os.chdir("env")
        for t in self.env_template_list:
            content=self.render_integrate_base(t)
            with open("./"+str(self.dut_name)+str(t).split(".")[0]+str(".sv"),"w") as fp:
                fp.write(content)
            if t=="_env_cfg.svh":
                self.pkg_str=str("`include \""+str(self.dut_name)+str(t).split(".")[0]+str(".sv")+"\"\n")+self.pkg_str
            else:
                self.pkg_str=self.pkg_str+str("`include \""+str(self.dut_name)+str(t).split(".")[0]+str(".sv")+"\"\n")
        os.chdir(self.out_dir)
        return

    #fill the testcase sv file 
    @DEBUG()
    def fill_testcase(self):
        os.chdir(self.out_dir)
        os.chdir("testcase")
        content=self.render_integrate_base(self.testcase_template)
        with open("./"+str(self.dut_name)+str(self.testcase_template).split(".")[0]+str(".sv"),"w") as fp:
            fp.write(content)
        self.pkg_str=self.pkg_str+str("`include \""+str(self.dut_name)+str(self.testcase_template).split(".")[0]+str(".sv")+"\"\n")
        os.chdir(self.out_dir)
        return
    

    #fill the reg model base
    def fill_reg_base(self,agent):
        content=self.render_integrate_base(self.reg_adp_template,agent)
        agent.ral.rdl.gen_uvmral("./",str(agent.ral.ral_name)+"_uvm.sv")#generate the uvm-ral
        self.pkg_str=self.pkg_str+str("`include \""+str(agent.ral.ral_name)+"_uvm.sv"+"\"\n")
        agent.ral.rdl.gen_ipxact("./IPXACT",str(agent.ral.ral_name)+".xml")#generate the register-ipxact 
        return content

    #fill the reg model 
    @DEBUG()
    def fill_reg(self):
        os.chdir(self.out_dir)
        uvm_list=[]
        for agent in self.agent_list:
            if agent.ral.ral_name!="":
                uvm_list.append(True)
            else:
                uvm_list.append(False)
        for i in range(len(uvm_list)):
            if uvm_list[i]==True:
                os.chdir(self.out_dir)
                os.chdir("reg_model")
                if not path_exists(self.agent_list[i].ral.ral_name):
                    os.mkdir(self.agent_list[i].ral.ral_name)
                os.chdir(self.agent_list[i].ral.ral_name)
                content=self.fill_reg_base(self.agent_list[i])
                with open("./"+str(self.agent_list[i].name)+str(self.reg_adp_template).split(".")[0]+str(".sv"),"w") as fp:
                    fp.write(content)
                self.pkg_str=self.pkg_str+str("`include \""+str(self.agent_list[i].name)+str(self.reg_adp_template).split(".")[0]+str(".sv")+"\"\n")
                os.chdir(self.out_dir)
            else:
                continue

    #generate the pkg file 
    @DEBUG()
    def gen_pkg(self):
        os.chdir(self.out_dir)
        os.chdir("sim")
        file=open(self.dut_name+"_pkg"+str(".sv"),"w")
        file.write(self.pkg_str)
        file.close()
        os.chdir(self.out_dir)
        return 

    #generate the tb harness file 
    @DEBUG()
    def gen_harness(self):
        os.chdir(self.out_dir)
        os.chdir("sim")
        global_param_list=[]
        global_all_port_list=[]
        global_clk_rst=[]
        global_port_list=[]
        param_dut=deepcopy(self.dut_parse.parameter)
        port_name_dut=deepcopy(self.dut_parse.port_list)
        port_dir_dut=deepcopy(self.dut_parse.direction_list)
        port_msb_dut=deepcopy(self.dut_parse.msb_list)
        port_lsb_dut=deepcopy(self.dut_parse.lsb_list)
        for agt in self.agent_list:
            param_dut.update(agt.interface.parameter)
            port_name_dut=port_name_dut+deepcopy(agt.interface.name_list)
            port_dir_dut=port_dir_dut+deepcopy(agt.interface.direction_list)
            port_msb_dut=port_msb_dut+deepcopy(agt.interface.msb_list)
            port_lsb_dut=port_lsb_dut+deepcopy(agt.interface.lsb_list)
        for key in list(param_dut.keys()):
            global_param_list.append(dict(key=key,value=param_dut[key]))
        for i in range(min(len(port_name_dut),len(port_dir_dut),len(port_msb_dut),len(port_lsb_dut))):
            global_all_port_list.append((port_name_dut[i],port_dir_dut[i],port_msb_dut[i],port_lsb_dut[i]))
        for port in list(set(global_all_port_list)):#delete repeat
            if format_bit(port[2])==format_bit(port[3]):#msb=lsb
                bit_info=""
            else:
                bit_info="["+str(format_bit(port[2]))+str(":")+str(format_bit(port[3]))+"]"
            if re.search(r'((clock)|(clk)|(rst)|(reset))',port[0].lower()) and port[1]==0:
                global_clk_rst.append(dict(direction="input",name=port[0],bit_info=bit_info))
            elif port[1]==0:#input 
                global_port_list.append(dict(direction="input",name=port[0],bit_info=bit_info))
            elif port[1]==1:#output
                global_port_list.append(dict(direction="output",name=port[0],bit_info=bit_info))
            elif port[1]==2: #inout
                global_port_list.append(dict(direction="inout",name=port[0],bit_info=bit_info))
            else:#default input 
                ERROR("port  #default input ")
                global_port_list.append(dict(direction="input",name=port[0],bit_info=bit_info))
        template=self.env.get_template(self.harness_template)
        content=template.render(MODULE=self.dut_name,
        global_param_list=global_param_list,global_clk_rst=global_clk_rst,global_port_list=global_port_list,
        agt_list=self.render_agent_list)
        with open("./"+str(self.dut_name)+str(self.harness_template).split(".")[0]+str(".sv"),"w") as fp:
            fp.write(content)
        os.chdir(self.out_dir)
        return

    #generate the file list file 
    @DEBUG()
    def gen_fil_list(self,fil_name="fil.lst"):
        string=""
        dir_list=["sequence"]
        for agt in self.agent_list:
            dir_list.append(agt.name+str("_agent"))
        dir_list.append("env")
        dir_list.append("testcase")
        for dir in dir_list:
            os.chdir(self.out_dir)
            os.chdir(dir)
            string=string+"+incdir+"+str(get_abs_dir("./"))+str("\n")
        os.chdir(self.out_dir)
        if "reg_model" in os.listdir("./"):
            os.chdir("reg_model")
            for agt in self.agent_list:
                if agt.ral.ral_name in os.listdir("./"):
                    os.chdir(agt.ral.ral_name)
                    string=string+"+incdir+"+str(get_abs_dir("./"))+str("\n")
                os.chdir(self.out_dir)
                os.chdir("reg_model")
            os.chdir(self.out_dir)
        os.chdir(self.out_dir)
        string=string+"\n\n"
        for dir in ["rtl","sim"]:
            os.chdir(dir)
            for v_fil in os.listdir("./"):
                if (v_fil!="Makefile") and (v_fil!=fil_name):
                    string=string+get_abs_dir("./")+str("/")+str(v_fil)+str("\n")
            os.chdir(self.out_dir)
        os.chdir(self.out_dir)
        os.chdir("sim")
        file=open(fil_name,"w")
        file.write(string)
        file.close()
        os.chdir(self.out_dir)
        return

    #generate the make file
    @DEBUG()
    def gen_makefile(self):
        os.chdir(self.out_dir)
        os.chdir("sim")
        file=open("Makefile","w")
        test_name="TEST_NAME="+str(self.dut_name)+str("_base_test\n")
        mk_str="""
VPD=+define+DUMP_VPD\nFSDB=+define+DUMP_FSDB
.PHONY:clean\nclean:\n\t-rm -rf simv* csrc *.h *.key
\n.PHONY:cmp\ncmp:\n\tvcs -full64 +v2k -sverilog -f fil.lst -ntb_opts uvm-1.2 -debug_all -timescale=1ns/1ps
\n.PHONY:run\nrun:\n\t./simv +UVM_TESTNAME=$(TEST_NAME)
"""
        file.write(test_name)
        file.write(mk_str)
        os.chdir(self.out_dir)
        return

    #run the flow
    @DEBUG()
    def run_flow(self,cfg_file=""):
        INFO("run_flow: "+"Parse Config & RTL File \n")
        self.parse(cfg_file)
        INFO("run_flow: "+"Build Project Directory\n")
        self.chg_out_dir()
        self.build_dir()
        INFO("run_flow: "+"UVM Project Auto Generate\n")
        self.fill_rtl()
        self.fill_sequence()
        self.fill_agents()
        self.fill_reg()
        self.fill_env()
        self.fill_testcase()
        self.gen_pkg()
        self.gen_harness()
        INFO("run_flow: "+"Simulate File Generate\n")
        self.gen_fil_list()
        self.gen_makefile()
        return
