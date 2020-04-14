`ifndef {{ module.upper() }}_ENV_SV
`define {{ module.upper() }}_ENV_SV

class {{ module }}_env extends uvm_env;
  // Data members
  {{ module }}_env_config    cfg;

  {{ module }}_master_agent       master[];
  {{ module }}_slave_agent        slave[];
  {{ module }}_virtual_sequencer  vsequencer;
  {{ module }}_env_checker        bus_checker;

  `uvm_component_utils({{ module }}_env)

  // Function declarations
  extern function      new(string name, uvm_component parent);
  extern function void build_phase(uvm_phase phase);
  extern function void connect_phase(uvm_phase phase);
endclass

function {{ module }}_env::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_env::build_phase(uvm_phase phase);
  super.build_phase(phase);

  if (!uvm_config_db #({{ module }}_env_config)::get(null, get_full_name(), "cfg", cfg)) begin
    `uvm_fatal("build_phase", "Cannot get env configuration.");
  end
  if (cfg == null)
    `uvm_fatal("build_phase", "Get a null env configuration")

  vsequencer = {{ module }}_virtual_sequencer::type_id::create("vsequencer", this);
  if (cfg.protocol_check_enable)
    bus_checker = {{ module }}_env_checker::type_id::create("bus_checker", this);

  master = new[cfg.mst_cfg.size()];
  vsequencer.master_sequencer = new[cfg.mst_cfg.size()];
  foreach (master[i]) begin
    if (cfg.mst_cfg[i].index != -1) begin
      uvm_config_db#({{ module }}_master_config)::set(this, $sformatf("master_%s", cfg.mst_cfg[i].get_name()), "cfg", cfg.mst_cfg[i]);
      master[i] = {{ module }}_master_agent::type_id::create($sformatf("master_%s", cfg.mst_cfg[i].get_name()), this);
    end
  end

  slave = new[cfg.slv_cfg.size()];
  vsequencer.slave_sequencer = new[cfg.slv_cfg.size()];
  foreach (slave[i]) begin
    if (cfg.slv_cfg[i].index != -1) begin
      uvm_config_db#({{ module }}_slave_config)::set(this, $sformatf("slave_%s", cfg.slv_cfg[i].get_name()), "cfg", cfg.slv_cfg[i]);
      slave[i] = {{ module }}_slave_agent::type_id::create($sformatf("slave_%s", cfg.slv_cfg[i].get_name()), this);
    end
  end

  vsequencer.cfg = cfg;
  if (cfg.protocol_check_enable)
    bus_checker.cfg = cfg;
endfunction

function void {{ module }}_env::connect_phase(uvm_phase phase);
  foreach (cfg.mst_cfg[i]) begin
    cfg.mst_cfg[i].events = cfg.events;
    vsequencer.master_sequencer[i] = master[i].sequencer;
  end
  foreach (cfg.slv_cfg[i]) begin
    cfg.slv_cfg[i].events = cfg.events;
    vsequencer.slave_sequencer[i] = slave[i].sequencer;
  end
endfunction

`endif