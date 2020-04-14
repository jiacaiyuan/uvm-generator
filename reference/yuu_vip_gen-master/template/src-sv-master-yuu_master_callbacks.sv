`ifndef {{ module.upper() }}_MASTER_CALLBACKS_SV
`define {{ module.upper() }}_MASTER_CALLBACKS_SV

typedef class {{ module }}_master_driver;
typedef class {{ module }}_master_monitor;

class {{ module }}_master_driver_callback extends uvm_callback;
  // Data members

  `uvm_object_utils({{ module }}_master_driver_callback)

  function new(string name="{{ module }}_master_driver_callback");
    super.new(name);
  endfunction

  virtual task pre_send({{ module }}_master_driver driver, {{ module }}_master_item item);
  endtask

  virtual task post_send({{ module }}_master_driver driver, {{ module }}_master_item item);
  endtask
endclass


class {{ module }}_master_monitor_callback extends uvm_callback;
  // Data members
  
  `uvm_object_utils({{ module }}_master_monitor_callback)

  function new(string name="{{ module }}_master_monitor_callback");
    super.new(name);
  endfunction

  virtual task pre_collect({{ module }}_master_monitor monitor, {{ module }}_item item);
  endtask

  virtual task post_collect({{ module }}_master_monitor monitor, {{ module }}_item item);
  endtask
endclass

`endif