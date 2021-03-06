//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
//Auto Generated by UVM-Generator
//Author: Jiacai Yuan
//E-mail: yuan861025184@163.com
//Contents:{{MODULE}}_{{MASTER_SLAVE_BUS}}_driver
//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
class {{MODULE}}_{{MASTER_SLAVE_BUS}}_driver extends uvm_driver 
{%-if response-%}#({{MASTER_SLAVE_BUS}}_req,{{MASTER_SLAVE_BUS}}_rsp);
{%-else-%}#({{MASTER_SLAVE_BUS}}_req);
{%endif%}
	`uvm_component_utils({{MODULE}}_{{MASTER_SLAVE_BUS}}_driver)
	`uvm_register_cb({{MODULE}}_{{MASTER_SLAVE_BUS}}_driver,{{MODULE}}_callback)

	//Config	//Interface
	{{MASTER_SLAVE_BUS}}_driver_config drv_cfg;
	virtual {{MODULE}}_{{MASTER_SLAVE_BUS}}_inf {{MASTER_SLAVE_BUS}}_inf;

	//TLM 
	//default seq_item_port

	//Transaction Sequence item
	{{MASTER_SLAVE_BUS}}_req  drv_req;
	{%if response%}{{MASTER_SLAVE_BUS}}_rsp  drv_rsp;{%endif%}
	
	//Constructor Function
	function new(string name="{{MODULE}}_{{MASTER_SLAVE_BUS}}_driver",uvm_component parent=null);
		super.new(name,parent);
	endfunction
	
	//Phase Methods
	extern virtual function void build_phase(uvm_phase phase);
	extern virtual function void connect_phase(uvm_phase phase);
	extern virtual task run_phase(uvm_phase phase);
	
	//Task Function Methods
	extern task drv_init();
	extern task drv_request();
	
	{{method}}
	// Add user method here
	//e.g. task function
	// User method ends
endclass

function void {{MODULE}}_{{MASTER_SLAVE_BUS}}_driver::build_phase(uvm_phase phase);
	super.build_phase(phase);
	`uvm_info(get_name(),"Build Phase is Called",UVM_LOW)
//	if(!uvm_config_db#({{MASTER_SLAVE_BUS}}_driver_config)::get(this,"","drv_cfg",drv_cfg))
//	begin
//		`uvm_fatal(get_name(),"Failed Get {{MASTER_SLAVE_BUS}} Driver Config")
//	end
	{{build_phase}}
	// Add user build here
	//e.g. TLM build
	// User build ends
endfunction

function void {{MODULE}}_{{MASTER_SLAVE_BUS}}_driver::connect_phase(uvm_phase phase);
	super.connect_phase(phase);
	`uvm_info(get_name(),"Connect Phase is Called",UVM_LOW)
	{{connect_phase}}
	// Add user connect here
	//e.g. TLM  interface connect
	// User connect ends
endfunction

task {{MODULE}}_{{MASTER_SLAVE_BUS}}_driver::run_phase(uvm_phase phase);
	super.run_phase(phase);
	`uvm_info(get_name(),"Run Phase is Called",UVM_LOW)
	drv_init();
	fork
		drv_request();
		{{run_phase_fork}}
		// Add user logic here

		// User logic ends
	join
	{{run_phase_main}}
	// Add user logic here
	//e.g. task function `uvm_do_callbacks
	// User logic ends	
endtask

task {{MODULE}}_{{MASTER_SLAVE_BUS}}_driver::drv_init();
	{{drv_init}}
	// Add user logic here
	//e.g. initialize interface
	// User logic ends	
endtask

task {{MODULE}}_{{MASTER_SLAVE_BUS}}_driver::drv_request();
	forever
	begin
		// Add user logic here
		#1;
		// User logic ends
		seq_item_port.get_next_item(drv_req);
		{{drv_request}}
		// Add user logic here
		//e.g. drive interface
		// User logic ends	
		{%-if response%}
		drv_rsp={{MASTER_SLAVE_BUS}}_rsp::type_id::create("drv_rsp",this);
		// Add user logic here
		//e.g. rsp processse
		// User logic ends
		drv_rsp.set_id_info(drv_req);
		seq_item_port.item_done(drv_rsp);
		{%-else-%}
		seq_item_port.item_done();
		{%-endif%}
	end
endtask
