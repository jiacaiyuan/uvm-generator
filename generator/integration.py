class INTEGRATION(object):
	def __init__(self):
		self.cfg_file=""
		self.dut_name=""
		self.outdir=""
		self.agent_list=[]
		self.env=Environment(loader = FileSystemLoader("../template/"))
		self.agt_template_list=["_interface.svh","_transaction.svh","_driver.svh",
		"_monitor.svh","_sequencer.svh","_agent_cfg.svh","_agent.svh","_reg_adapter.svh",
		"_sequence_base.svh"]
		self.global_template_list=["_sequence_cfg.svh","_virtual_sequencer.svh",
		"_env_cfg.svh","_env.svh",
		"_base_test.svh","_harness.svh"]

	def parse(self,cfg_file):
		if cfg_file!="":
			self.cfg_file=cfg_file
		self.cfg_file=get_abs_dir(del_content(str(self.cfg_file)))
            if not path_exists(self.cfg_file):
				ERROR("------------------------")
				exit()
		jscfg=JSONCFG_PARSE(self.cfg_file)
		jscfg.parse()
		dut_parse=DUT_PARSE()
		dut_parse.parse(jscfg.top_module,jscfg.top_name)
		if dut_parse.module_name!="":
			self.dut_name=dut_parse.module_name
		else:
			self.dut_name="AUTO_DUT"
		self.agent_list=jscfg.agent_list
		if len(self.agent_list)==0:
			agt=AGENT()
			agt.name="AUTO_AGENT"
			self.agent_list.append(agt)
		for i in range(len(self.agent_list)):
			self.agent_list[i].interface.format_inf(dut_parse.parameter,dut_parse.port_list,
	                                         dut_parse.direction_list,dut_parse.msb_list,
											 dut_parse.lsb_list)
			self.agent_list[i].ral.format_ral()
		return

	def build_proj_dir(self,outdir):
		self.outdir=get_abs_dir(outdir)
		if not os.path.exists(self.outdir):
			os.mkdirs(self.outdir)
		os.chdir(self.outdir)
		os.mkdir(str(self.dut_name)+"_verify")
		os.chdir(str(self.dut_name)+"_verify")
		self.outdir=get_abs_dir("./")
		return

	def build_agents(self,outdir):
	
	
	
	
	def build_env(self,outdir):
	
	
	
	def build_sim(self,outdir):
	
	
	
	def build_cases(self,outdir):
	
	
	
	def build_package(self,outdir):
	
	
	
	def build_file_list(self,outdir):
	
	def build_makefie(self,outdir):
	



	def integrate_render(self):
		render_agent_list=[]
		for agt in self.agent_list:
			render_agent_list.append(agt.render_agent())
		for agent in self.agent_list:
			os.chdir(self.outdir)
			os.mkdir(agent.name)
			os.chdir(agent.name)
			if agent.ral.ral_name!="":
				UVM_RAL=True
			else:
				UVM_RAL=False
			for t in self.agt_template_list:
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