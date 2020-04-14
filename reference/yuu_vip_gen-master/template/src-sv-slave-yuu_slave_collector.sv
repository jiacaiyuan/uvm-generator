`ifndef {{ module.upper() }}_SLAVE_COLLECTOR_SV
`define {{ module.upper() }}_SLAVE_COLLECTOR_SV

class {{ module }}_slave_collector extends uvm_subscriber #({{ module }}_slave_item);
  // Data members
  virtual {{ module }}_slave_interface vif;

  {{ module }}_slave_config cfg;
  uvm_event_pool events;

  {{ module }}_slave_item item;

  `uvm_component_utils_begin({{ module }}_slave_collector)
  `uvm_component_utils_end

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void connect_phase(uvm_phase phase);
  extern virtual task          run_phase(uvm_phase phase);

  extern virtual function void write({{ module }}_slave_item t);
endclass

function {{ module }}_slave_collector::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_slave_collector::connect_phase(uvm_phase phase);
  this.vif = cfg.vif;
  this.events = cfg.events;
endfunction

task {{ module }}_slave_collector::run_phase(uvm_phase phase);
endtask


function void {{ module }}_slave_collector::write({{ module }}_slave_item t);
endfunction

`endif