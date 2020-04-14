`ifndef {{ module.upper() }}_MONITOR_SV
`define {{ module.upper() }}_MONITOR_SV

class {{ module }}_monitor extends uvm_monitor;
  // Data members
  virtual {{ module }}_interface  vif;
  uvm_analysis_port #({{ module }}_item) out_monitor_ap;

  {{ module }}_config cfg;
  uvm_event_pool events;

  `uvm_register_cb({{ module }}_monitor, {{ module }}_monitor_callback)

  `uvm_component_utils({{ module }}_monitor)

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void build_phase(uvm_phase phase);
  extern virtual function void connect_phase(uvm_phase phase);
  extern virtual task          run_phase(uvm_phase phase);
endclass

function {{ module }}_monitor::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_monitor::build_phase(uvm_phase phase);
  out_monitor_ap = new("out_monitor_ap", this);
endfunction

function void {{ module }}_monitor::connect_phase(uvm_phase phase);
  this.vif = cfg.vif;
  this.events = cfg.events;
endfunction

task {{ module }}_monitor::run_phase(uvm_phase phase);
endtask

`endif