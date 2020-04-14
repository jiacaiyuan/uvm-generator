`ifndef {{ module.upper() }}_ENV_CHECKER_SV
`define {{ module.upper() }}_ENV_CHECKER_SV

class {{ module }}_env_checker extends uvm_component;
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_env_config cfg;
  uvm_event_pool events;

  `uvm_component_utils({{ module }}_env_checker)
  
  // Function declarations  
  extern         function      new(string name, uvm_component parent);
  extern virtual function void connect_phase(uvm_phase phase);
endclass

function {{ module }}_env_checker::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_env_checker::connect_phase(uvm_phase phase);
  if (cfg == null)
    `uvm_fatal("connect_phase", "Env checker cannot get env configuration object")

  vif = cfg.vif;
  events = cfg.events;
endfunction

`endif
