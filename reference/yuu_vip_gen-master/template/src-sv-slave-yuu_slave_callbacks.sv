`ifndef {{ module.upper() }}_SLAVE_CALLBACKS_SV
`define {{ module.upper() }}_SLAVE_CALLBACKS_SV

typedef class {{ module }}_slave_driver;
typedef class {{ module }}_slave_monitor;

class {{ module }}_slave_driver_callback extends uvm_callback;
  // Data members

  `uvm_object_utils({{ module }}_slave_driver_callback)

  function new(string name="{{ module }}_slave_driver_callback");
    super.new(name);
  endfunction

  virtual task pre_send({{ module }}_slave_driver driver, {{ module }}_slave_item item);
  endtask

  virtual task post_send({{ module }}_slave_driver driver, {{ module }}_slave_item item);
  endtask
endclass


class {{ module }}_slave_monitor_callback extends uvm_callback;
  // Data members
  
  `uvm_object_utils({{ module }}_slave_monitor_callback)

  function new(string name="{{ module }}_slave_monitor_callback");
    super.new(name);
  endfunction

  virtual task pre_collect({{ module }}_slave_monitor monitor, {{ module }}_slave_item item);
  endtask

  virtual task post_collect({{ module }}_slave_monitor monitor, {{ module }}_slave_item item);
  endtask
endclass

`endif