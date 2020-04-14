`ifndef {{ module.upper() }}_COLLECTOR_SV
`define {{ module.upper() }}_COLLECTOR_SV

class {{ module }}_collector extends uvm_subscriber #({{ module }}_item);
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_config cfg;
  uvm_event_pool events;

  {{ module }}_item item;

  `uvm_component_utils_begin({{ module }}_collector)
  `uvm_component_utils_end

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void connect_phase(uvm_phase phase);
  extern virtual task          run_phase(uvm_phase phase);

  extern virtual function void write({{ module }}_item t);
endclass

function {{ module }}_collector::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_collector::connect_phase(uvm_phase phase);
  this.vif = cfg.vif;
  this.events = cfg.events;
endfunction

task {{ module }}_collector::run_phase(uvm_phase phase);
endtask


function void {{ module }}_collector::write({{ module }}_item t);
endfunction

`endif