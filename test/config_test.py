import sys
sys.path.insert(0,"../")
from generator.interface import *
from generator.agent import *
from generator.jsoncfg_parse import *
from generator.base_func import *
from generator.dut_parse import *
from jinja2 import Environment,FileSystemLoader



#-------------------------------------
#config
#-------------------------------------
jscfg=JSONCFG_PARSE("./dut.json")
jscfg.parse()
dut_parse=DUT_PARSE()
dut_parse.parse(jscfg.top_module,jscfg.top_name)
name=dut_parse.module_name
agent_list=jscfg.agent_list
if len(agent_list)==0:
    agt=AGENT()
    agt.name="AUTO_AGENT"
    agent_list.append(agt)
for i in range(len(agent_list)):
    agent_list[i].interface.format_inf(dut_parse.parameter,dut_parse.port_list,
                                             dut_parse.direction_list,dut_parse.msb_list,
                                             dut_parse.lsb_list)
    agent_list[i].ral.format_reg()

#-------------------------------------
#ral 
#-------------------------------------
bus_reg=REGISTER()
bus_reg.ral_name="UART"
bus_reg.auto_predict=True  #initial config 
#bus_reg.auto_predict=False
bus_reg.ral_content=open("UART_uvm.sv","r").read()
for i in range(len(agent_list)):
    if agent_list[i].name=="bus":
        agent_list[i].ral=bus_reg

#-------------------------------------
#display 
#-------------------------------------
print("---------------------------------------------")
print(name)
for agt in agent_list:
     agt.display_agt()



#-------------------------------------
#render 
#-------------------------------------
render_agent_list=[]
for agt in agent_list:
    render_agent_list.append(agt.render_agent())
















#-------------------------------------
#genearte
#-------------------------------------
if name!="":
    MODULE=name
else:
    MODULE="dut"

env=Environment(loader = FileSystemLoader("../template/"))
agt_template_list=["_interface.svh","_transaction.svh","_driver.svh",
"_monitor.svh","_sequencer.svh","_agent_cfg.svh","_agent.svh","_reg_adapter.svh",
"_sequence_base.svh"]

global_template_list=["_sequence_cfg.svh","_virtual_sequencer.svh",
"_env_cfg.svh","_env.svh",
"_base_test.svh","_harness.svh"]
for agent in agent_list:
    if agent.ral.ral_name!="":
        UVM_RAL=True
    else:
        UVM_RAL=False
    for t in agt_template_list:
        if (t=="_reg_adapter.svh") and UVM_RAL==False:
            continue
        template=env.get_template(t)
        content=template.render(
        MODULE=MODULE,
        MASTER_SLAVE_BUS=agent.name,
        param_list=agent.interface.render_param(),
        clk_rst=agent.interface.render_signals(agent.interface.clk_rst),
        port_list=agent.interface.render_signals(agent.interface.port_list),
        response=agent.response,
        UVM_RAL=UVM_RAL,
        agt_list=render_agent_list,
        ral=agent.ral.render_reg()
        )
        with open("./"+str(agent.name)+str(t).split(".")[0]+str(".sv"),"w") as fp:
            fp.write(content)
for t in global_template_list:
    template=env.get_template(t)
    content=template.render(
    MODULE=MODULE,
    MASTER_SLAVE_BUS=agent.name,
    param_list=agent.interface.render_param(),
    clk_rst=agent.interface.render_signals(agent.interface.clk_rst),
    port_list=agent.interface.render_signals(agent.interface.port_list),
    response=agent.response,
    UVM_RAL=UVM_RAL,
    agt_list=render_agent_list,
    ral=agent.ral.render_reg()
    )
    with open("./"+str(MODULE)+str(t).split(".")[0]+str(".sv"),"w") as fp:
        fp.write(content)








