`ifndef {{ module.upper() }}_BUS_CHECKER_SV
`define {{ module.upper() }}_BUS_CHECKER_SV

class {{ module }}_bus_checker extends uvm_component;
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_config cfg;
  uvm_event_pool events;

  `uvm_component_utils({{ module }}_bus_checker)
  
  // Function declarations  
  extern         function      new(string name, uvm_component parent);
  extern virtual function void connect_phase(uvm_phase phase);
endclass

function {{ module }}_bus_checker::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_bus_checker::connect_phase(uvm_phase phase);
  if (cfg == null)
    `uvm_fatal("connect_phase", "bus checker cannot get configuration object")

  vif = cfg.vif;
  events = cfg.events;
endfunction

`endif
