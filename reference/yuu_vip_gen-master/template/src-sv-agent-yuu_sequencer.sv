`ifndef {{ module.upper() }}_SEQUENCER_SV
`define {{ module.upper() }}_SEQUENCER_SV

class {{ module }}_sequencer extends uvm_sequencer #({{ module }}_item);
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_config cfg;
  uvm_event_pool events;

  `uvm_component_utils({{ module }}_sequencer)

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void connect_phase(uvm_phase phase);
endclass

function {{ module }}_sequencer::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_sequencer::connect_phase(uvm_phase phase);
  super.connect_phase(phase);

  this.vif = cfg.vif;
  this.events = cfg.events;
endfunction

`endif