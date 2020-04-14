`ifndef {{ module.upper() }}_ENV_CONFIG_SV
`define {{ module.upper() }}_ENV_CONFIG_SV

class {{ module }}_env_config extends uvm_object;
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_master_config  mst_cfg[$];
  {{ module }}_slave_config   slv_cfg[$];
  uvm_event_pool events;

  boolean protocol_check_enable = False;

  // Constraints

  `uvm_object_utils_begin({{ module }}_env_config)
    `uvm_field_enum         (boolean, protocol_check_enable,  UVM_PRINT | UVM_COPY)
    `uvm_field_queue_object (         mst_cfg,                UVM_PRINT | UVM_COPY)
    `uvm_field_queue_object (         slv_cfg,                UVM_PRINT | UVM_COPY)
  `uvm_object_utils_end

  // Function declarations
  extern         function      new(string name="{{ module }}_env_config");
  extern virtual function void set_config({{ module }}_agent_config cfg);
  extern virtual function void set_configs({{ module }}_agent_config cfg[]);
endclass

function {{ module }}_env_config::new(string name="{{ module }}_env_config");
  super.new(name);
endfunction

function void {{ module }}_env_config::set_config({{ module }}_agent_config cfg);
  {{ module }}_master_config m_cfg;
  {{ module }}_slave_config  s_cfg;

  if (cfg == null)
    `uvm_fatal("set_config", "Which {{ module }} agent config set is null")

  cfg.events = events;
  if ($cast(m_cfg, cfg)) begin
    if(m_cfg.index >= 0)
      m_cfg.vif = vif.get_master_if(m_cfg.index);
    mst_cfg.push_back(m_cfg);
  end
  else if ($cast(s_cfg, cfg))begin
    if (s_cfg.index >= 0)
      s_cfg.vif = vif.get_slave_if(s_cfg.index);
    slv_cfg.push_back(s_cfg);
  end
  else
    `uvm_fatal("set_config", "Invalid {{ module }} agent configure object type")
endfunction

function void {{ module }}_env_config::set_configs({{ module }}_agent_config cfg[]);
  foreach (cfg[i])
    set_config(cfg[i]);
endfunction

`endif