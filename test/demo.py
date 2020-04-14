import sys
sys.path.append("../src")
from interface import *
from agent import *
from jinja2 import Environment,FileSystemLoader
#-------------------------------------
#data info 
#-------------------------------------
name_bus=["PCLK","PCLKG","PRESETn","PSEL","pAddr","penable","PWRite","PWDATA","prdata","pready","pslverr"]
dir_bus=[0,0,0,0,0,0,0,0,1,1,1]
msb_bus=[0,0,"0","0x0","ADDR_WIDTH<<2-1","0X0",0,"DATA_WIDTH-1",31,0,0]
lsb_bus=[0,0,"0","0x0","2","0X0",0,0,0,0,0]
param_dict={"ADDR_WIDTH":32,"DATA_WIDTH":32}


name_master=["RXD","data_st","addr_st","control","request","valid","data_ld","addr_ld"]
dir_master=[0,0,0,0,1,1,1,1]
msb_master=[0,31,31,7,0,2,31,31]
lsb_master=[0,0,0,0,0,0,0,0]

name_slave=["TXD","data_wrt","addr_wrt","regrant","confirm","data_rd","addr_rd"]
dir_slave=[1,1,1,1,0,0,0]
msb_slave=[0,7,7,0,3,7,7]
lsb_slave=[0,0,0,0,0,0,0,0]


#-------------------------------------
#data struct build
#-------------------------------------


#bus----------------------------------
bus_port_all_list=[]
for i in range(len(name_bus)):
    sig=SIGNAL()
    sig.name=name_bus[i]
    sig.direction=dir_bus[i]
    sig.msb=msb_bus[i]
    sig.lsb=lsb_bus[i]
    bus_port_all_list.append(sig)
bus_inf=INTERFACE()
bus_inf.parameter=param_dict
bus_inf.clk_rst=bus_port_all_list[0:3]
bus_inf.port_list=bus_port_all_list[3:]

bus_reg=REGISTER()
bus_reg.ral_name="UART"
bus_reg.auto_predict=True  #initial config 
#bus_reg.auto_predict=False

bus_reg.ral_content=open("UART_uvm.sv","r").read()

bus_agent=AGENT()
bus_agent.name="bus"
bus_agent.interface=bus_inf
bus_agent.is_active=True
bus_agent.response=True  #initial config 
#bus_agent.response=False
bus_agent.ral=bus_reg




#master----------------------------------
master_port_all_list=[]
for i in range(len(name_master)):
    sig=SIGNAL()
    sig.name=name_master[i]
    sig.direction=dir_master[i]
    sig.msb=msb_master[i]
    sig.lsb=lsb_master[i]
    master_port_all_list.append(sig)
master_inf=INTERFACE()
master_inf.clk_rst=bus_port_all_list[0:3]
master_inf.port_list=master_port_all_list

master_agent=AGENT()
master_agent.name="master"
master_agent.interface=master_inf
master_agent.is_active=True
master_agent.response=True    #initial config 
#master_agent.response=False 

#slave-----------------------------------
slave_port_all_list=[]
for i in range(len(name_slave)):
    sig=SIGNAL()
    sig.name=name_slave[i]
    sig.direction=dir_slave[i]
    sig.msb=msb_slave[i]
    sig.lsb=lsb_slave[i]
    slave_port_all_list.append(sig)
slave_inf=INTERFACE()
slave_inf.clk_rst=bus_port_all_list[0:3]
slave_inf.port_list=slave_port_all_list

slave_agent=AGENT()
slave_agent.name="slave"
slave_agent.interface=slave_inf
slave_agent.is_active=False
slave_agent.response=False

agent_list=[bus_agent,master_agent,slave_agent] #initial config
#agent_list=[bus_agent]
render_agent_list=[]
for agt in agent_list:
    render_agent_list.append(agt.render_agent())







#-------------------------------------
#genearte
#-------------------------------------
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