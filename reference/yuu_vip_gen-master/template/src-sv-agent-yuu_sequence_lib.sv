`ifndef {{ module.upper() }}_SEQUENCE_LIB_SV
`define {{ module.upper() }}_SEQUENCE_LIB_SV

typedef class {{ module }}_sequencer;
class {{ module }}_sequence_base extends uvm_sequence #({{ module }}_item);
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_config cfg;
  uvm_event_pool events;

  `uvm_object_utils_begin({{ module }}_sequence_base)
  `uvm_object_utils_end
  `uvm_declare_p_sequencer({{ module }}_sequencer)

  function new(string name="{{ module }}_sequence_base");
    super.new(name);
  endfunction

  virtual task pre_start();
    cfg = p_sequencer.cfg;
    vif = cfg.vif;
    events = cfg.events;
  endtask

  virtual task body();
    return;
  endtask
endclass

`endif