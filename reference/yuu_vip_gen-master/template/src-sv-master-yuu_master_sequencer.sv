`ifndef {{ module.upper() }}_MASTER_SEQUENCER_SV
`define {{ module.upper() }}_MASTER_SEQUENCER_SV

class {{ module }}_master_sequencer extends uvm_sequencer #({{ module }}_master_item);
  // Data members
  virtual {{ module }}_master_interface vif;

  {{ module }}_master_config cfg;
  uvm_event_pool events;

  `uvm_component_utils({{ module }}_master_sequencer)

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void connect_phase(uvm_phase phase);
endclass

function {{ module }}_master_sequencer::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_master_sequencer::connect_phase(uvm_phase phase);
  super.connect_phase(phase);

  this.vif = cfg.vif;
  this.events = cfg.events;
endfunction

`endif