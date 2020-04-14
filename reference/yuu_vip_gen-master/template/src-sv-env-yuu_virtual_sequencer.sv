`ifndef {{ module.upper() }}_VIRTUAL_SEQUENCER_SV
`define {{ module.upper() }}_VIRTUAL_SEQUENCER_SV

class {{ module }}_virtual_sequencer extends uvm_virtual_sequencer;
  // Data members
  
  virtual {{ module }}_interface vif;

  {{ module }}_env_config  cfg;
  uvm_event_pool      events;

  {{ module }}_master_sequencer  master_sequencer[];
  {{ module }}_slave_sequencer   slave_sequencer[];

  `uvm_component_utils({{ module }}_virtual_sequencer)

  // Function declarations
  extern function      new(string name, uvm_component parent);
  extern function void connect_phase(uvm_phase phase);
endclass : {{ module }}_virtual_sequencer

function {{ module }}_virtual_sequencer::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_virtual_sequencer::connect_phase(uvm_phase phase);
  super.connect_phase(phase);

  if (cfg == null)
    `uvm_fatal("connect_phase", "Virtual sequencer cannot get env configuration object")

  vif = cfg.vif;
  events = cfg.events;
endfunction


class {{ module }}_virtual_sequence extends uvm_sequence_base;
  // Data members

  `uvm_object_utils({{ module }}_virtual_sequence)
  `uvm_declare_p_sequencer({{ module }}_virtual_sequencer)

  function new(string name="{{ module }}_virtual_sequence");
    super.new(name);
  endfunction
endclass : {{ module }}_virtual_sequence

`endif