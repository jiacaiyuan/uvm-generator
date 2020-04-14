`ifndef {{ module.upper() }}_MASTER_ADAPTER_SV
`define {{ module.upper() }}_MASTER_ADAPTER_SV

class {{ module }}_reg_extension extends uvm_object;
  // Data members
  `uvm_object_utils({{ module }}_reg_extension)

  function new(string name="{{ module }}_reg_extension");
    super.new(name);
  endfunction
endclass : {{ module }}_reg_extension


class {{ module }}_master_adapter extends uvm_reg_adapter;
  // Data members
  {{ module }}_master_config cfg;

  `uvm_object_utils({{ module }}_master_adapter)

  function new(string name="{{ module }}_master_adapter");
    super.new(name);
  endfunction

  virtual function uvm_sequence_item reg2bus(const ref uvm_reg_bus_op rw);
  endfunction

  virtual function void bus2reg(uvm_sequence_item bus_item,
                                ref uvm_reg_bus_op rw);
  endfunction
endclass : {{ module }}_master_adapter

`endif