`ifndef {{ module.upper() }}_MASTER_SEQUENCE_LIB_SV
`define {{ module.upper() }}_MASTER_SEQUENCE_LIB_SV

typedef class {{ module }}_master_sequencer;
class {{ module }}_master_sequence_base extends uvm_sequence #({{ module }}_master_item);
  // Data members
  virtual {{ module }}_master_interface vif;

  {{ module }}_master_config cfg;
  uvm_event_pool events;

  `uvm_object_utils_begin({{ module }}_master_sequence_base)
  `uvm_object_utils_end
  `uvm_declare_p_sequencer({{ module }}_master_sequencer)

  function new(string name="{{ module }}_master_sequence_base");
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